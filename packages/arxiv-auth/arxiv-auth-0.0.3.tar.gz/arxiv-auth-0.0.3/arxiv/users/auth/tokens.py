"""
Functions for working with authn/z tokens on user/client requests.

Encrypted JSON Web Tokens can be used inside the arXiv system to securely
convey authn/z information about each request. These tokens will usually be
generated by the :mod:`authorizer` in response to an
authorization subrequest from the web server, and contain information about
the identity of the user and/or client as well as authorization information
(e.g. :mod:`arxiv.users.auth.scopes`).

It is essential that these JWTs are encrypted and decrypted precisely the same
way in all arXiv services, so we include these routines here for convenience.

"""

import jwt
from . import exceptions
from .. import domain


def encode(session: domain.Session, secret: str) -> str:
    """
    Encode session information as an encrypted JWT.

    Parameters
    ----------
    session : :class:`.domain.Session`
        User or client session data, including authorization information.
    secret : str
        A secret key used to encrypt the token. This secret is required to
        decode the token later on (e.g. in the application handling the
        request).

    Returns
    -------
    str
        An encrypted JWT.

    """
    return jwt.encode(domain.to_dict(session), secret).decode('ascii')


def decode(token: str, secret: str) -> domain.Session:
    """Decode an auth token to access session information."""
    try:
        data = dict(jwt.decode(token, secret, algorithms=['HS256']))
    except jwt.exceptions.DecodeError as e:  # type: ignore
        raise exceptions.InvalidToken('Not a valid token') from e
    session: domain.Session = domain.from_dict(domain.Session, data)
    return session
