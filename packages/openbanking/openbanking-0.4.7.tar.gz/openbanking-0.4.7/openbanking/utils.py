import os
import uuid
import json
import time
import base64
import hashlib
import requests
from jwcrypto import jwk, jwt, jws
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from .exceptions import PathFileError, DecodeError, SSAError, AlgorithmError


def make_uuid_4122() -> str:
    """Returns UUID layout given in RFC 4122. https://docs.python.org/2/library/uuid.html#uuid.RFC_4122 """
    return str(uuid.uuid4())


def default_headers():
    """
    :rtype: requests.structures.CaseInsensitiveDict
    """
    return "test"


def base64url_decode(input):
    if isinstance(input, str):
        input = input.encode('ascii')

    rem = len(input) % 4

    if rem > 0:
        input += b'=' * (4 - rem)

    return base64.urlsafe_b64decode(input)


def load_key_from_file_as_string(key_path: str) -> str:
    """
    Loads a key from file and returns the sting value.
    """
    if not os.path.isfile(key_path):
        raise PathFileError("Cannot find signing key path {}".format(key_path))

    return open(key_path, "r").read()


def get_kid(signing_public):
    """Return the kid, X.509 Certificate SHA-1 Thumbprint of the signing certificate."""
    signing_key_string = load_key_from_file_as_string(signing_public)
    key_obj = jwk.JWK.from_pem(signing_key_string.encode('latin-1'))
    kid = key_obj.thumbprint(hashalg=hashes.SHA1())
    return kid


def sign(header: str, claims: str, signing_key) -> str:
    """
    Creates a JWT object.

    :param header: A dict or a JSON string with the JWT Header data.
    :param claims: A dict or a string with the JWT Claims data.
    :param signing_key: Private RSA key to sign the JWT.

    :return: Serialized token.
    """

    token = jwt.JWT(header=header, claims=claims)
    signing_key_string = load_key_from_file_as_string(signing_key)
    key_obj = jwk.JWK.from_pem(signing_key_string.encode('latin-1'))
    # create a signed token with the generated key
    token.make_signed_token(key_obj)
    signed_token = token.serialize()
    return signed_token


def make_header_claims(kid: str, iss: str, aud: str, more_claims=None, scope=None, client_id=None, exp=120,
                       response_type=None, redirect_uri=None, state=None, nonce=None, sub=None) -> (dict, dict):
    """
    Generic function that returns a dict of claims and headers, used to create a signed JWT.
    """
    jwt_iat = int(time.time())
    jwt_exp = jwt_iat + exp
    header = dict(alg='RS256', kid=kid, typ='JWT')
    # Common
    claims = dict(
        iss=iss,
        aud=aud,
        jti=str(uuid.uuid4()),
        iat=jwt_iat,
        exp=jwt_exp
    )

    if scope:
        claims['scope'] = scope
    if sub:
        claims['sub'] = sub
    if more_claims:
        claims['claims'] = more_claims
    if client_id:
        claims['client_id'] = client_id
    if response_type:
        claims['response_type'] = response_type
    if redirect_uri:
        claims['redirect_uri'] = redirect_uri
    if state:
        claims['state'] = state
    if nonce:
        claims['nonce'] = nonce

    # print("headers \b {}".format(header))
    # print("claims \b {}".format(claims))
    return header, claims


def make_onboarding_token(kid: str, aud: str, ssa: str, exp=None, scope="openid accounts payments") -> (dict, dict):
    """
    OpenID Dynamic Client Registration Specification

    A TPP MAY use automated client registration to submit an SSA to an ASPSP in exchange for client credentials
    for use as a client against an OAuth 2.0 Authorization Server.

    - Notes:
        https://openid.net/specs/openid-connect-registration-1_0.html
        Redirect URLs MUST match or be a subset of the software_redirect_uris claim in the SSA.


    :param kid: kept the same as the "x5t" parameter. (X.509 Certificate SHA-1 Thumbprint) of the signing certificate.
    :param exp: Request Expiration time [RFC7519].
    :param aud: Request audience (the ASPSP) [RFC7519].
    :param ssa: SSA identifier, issued by Open Banking [RFC7519].
    :param scope: Scopes the client is asking for (if not specified, default scopes are assigned by the AS)


    :return: header dict and claims dict
    """

    # TODO: Checking the SSA could be a useful API on its own, maybe think about adding it.
    # Do checks on SSA and get software redirects.
    try:
        signing_input, crypto_segment = ssa.rsplit('.', 1)
        header_segment, payload_segment = signing_input.split('.', 1)
    except ValueError:
        raise DecodeError('Not enough segments')

    try:
        header_data = base64url_decode(header_segment)
    except:
        raise DecodeError('Invalid header padding')

    try:
        payload = base64url_decode(payload_segment)
    except:
        raise DecodeError('Invalid payload padding')

    payload = json.loads(payload.decode('utf-8'))
    redirect_uris = payload.get('software_redirect_uris', None)
    software_client_id = payload.get('software_client_id', None)

    # Some error checking on the redirect URL before trying to use it.
    if not redirect_uris:
        raise SSAError("No redirect URL found in the supplied SSA.")
    if type(redirect_uris) != list:
        raise SSAError("Invalid redirect URLs in SSA. Not of type list {}".format(redirect_uris))
    if not software_client_id:
        raise SSAError("No software_client_id found in SSA.")

    # jti provides a unique identifier for the JWT.
    jti = str(uuid.uuid4())
    # iat time SSA issued [RFC7519].
    iat = int(time.time())
    if not exp:
        exp = iat + 3600

    # The SSA header MUST comply with [RFC7519].
    header = dict(
        kid=kid,
        alg='RS256',
        typ='JWT'
    )

    claims = dict(
        iss=software_client_id,  # MUST match software ID. Identifies the principal that issued the JWT [RFC7519].
        exp=exp,
        iat=iat,
        aud=aud,
        jti=jti,  # [RFC7519].
        software_statement=ssa,
        scope=scope,
        redirect_uris=redirect_uris,
        application_type="web",  # MUST be web if specified [OIDC-R].
        subject_type="public",  # MUST be public if specified [OIDC-R].
        response_types=["code", "code id_token"],  # Returned from the ASPSP authorisation endpoint [RFC7591]
        grant_types=["authorization_code", "refresh_token", "client_credentials"],
        id_token_signed_response_alg="RS256",  # Algorithm to sign the id_token, if one is returned. [OIDC-R]
        request_object_signing_alg="RS256",  # Algorithm to sign the request object if part of the authorisation.
        token_endpoint_auth_signing_alg="RS256",
        token_endpoint_auth_method="private_key_jwt",
        # request_object_encryption_alg="RSA-OAEP-256",
        # request_object_encryption_enc="A128CBC-HS256",

    )

    return header, claims


def get_ca_bundle_location(ca=None):
    """
    Util that returns the location of the ca certs for ob or None if not required.

    Returns:
        `boolean` False or 'string' url path.

    Raises:
        exception `~openbanking.exceptions.PathFileError` - cannot find path to file
    """
    if ca is None:
        return False

    if ca == "all":
        return True

    # TODO: Make this smarter to work with other ca's.
    if ca == "OB":
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'ca_ob_sandbox.pem')
        return filename


def make_request(method, url, payload=None, headers=None, cert=None, verify=True):
    """
    Using Requests, make a HTTP call and record the response and status codes.
    :param method: the method i.e. get, post, delete.
    :param url: the resource url.
    :param verify: (optional), boolean, controls whether we verify the server's TLS certificate. Defaults to True.
    :return:
    """
    r = None
    if method == "get":
        r = requests.get(url, verify=verify, headers=headers, cert=cert)
    if method == "post":
        r = requests.post(url, data=payload, headers=headers, cert=cert, verify=verify)
    if method == "delete":
        r = requests.delete(url, data=payload, headers=headers, cert=cert, verify=verify)

    # TODO: move response to class.
    # set the response regardless or errors
    try:
        response = r.json()
    except json.decoder.JSONDecodeError:
        response = {"error": "Json decoding error", "raw": r.content}

    status_code = r.status_code
    return response, status_code


def is_c_hash_valid(code: str, id_token: str):
    """Util to compare the token hash value against the c_hash attribute in an ID Token.

    Notes:
        Code hash value. Value is the base64url encoding of the left-most half of the hash of the octets of the
        ASCII representation of the code value, where the hash algorithm used is the hash algorithm used in the alg
        Header Parameter of the ID Token's JOSE Header. For instance, if the alg is HS512, hash the code value with
        SHA-512, then take the left-most 256 bits and base64url encode them.

        The c_hash value is a case sensitive string.

        Ref - http://openid.net/specs/openid-connect-core-1_0.html#HybridIDToken

        Steps to generate c_hash from the token:

        1. Hash the ASCII representation of the token using the same alg as the Token itself, i.e. SHA-256.
        2. Truncate the hash to the first half of the raw hash value (importantly: not the string hex representation of the hash).
        3. Base64url encode (without padding) the truncated hash bytes.
        4. Compare c_hash value

    Args:
        code: the code token
        id_token: the full id_token to check must have alg and c_hash values.


    Returns:
        class: `boolean`. True if c_hash claims matches encode code value.

        Raises:
           exception `~openbanking.exceptions.DecodeError` - Issue decoding string.
           exception `~openbanking.exceptions.AlgorithmError` - Unsupported algorithm in claims.
    """

    # Get header and claims from the token to review later.
    id_token_header = json.loads(jws.base64url_decode(id_token.split(".")[0]))
    id_token_claims = json.loads(jws.base64url_decode(id_token.split(".")[1]))
    # Store the 'alg' and 'c_hash' values from the id_token we are to compare.
    id_alg = id_token_header.get("alg")
    id_c_hash = id_token_claims.get("c_hash")
    # Hash the token (code).
    if id_alg == 'RS256':
        hash = hashlib.sha256(code.encode('utf-8'))
        # get the hash digest bytes (NOT a hex string)!
        digest = hash.digest()
    else:
        raise AlgorithmError('Missing or unsupported algorithm in id_token claims')
    # Truncate the hash digest to the first half.
    digest_truncated = digest[:(int(len(digest) / 2))]
    # base64url encodes the truncated hash digest bytes.
    token_hash_computed = base64.urlsafe_b64encode(digest_truncated)
    # Last compare values to see if they match and return boolean result.
    return True if id_c_hash == token_hash_computed.decode() else False
