"""Module for authentication and authorization to resource operations."""

# Copyright © 2017–2018 Paul Bryan.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import binascii
import roax.context as context

from base64 import b64decode
from roax.resource import Forbidden, Unauthorized


class SecurityRequirement:
    """
    Performs authorization of resource operations.
    """

    def __init__(self, scheme=None, scopes=[]):
        """
        Initialize security requirement.

        If the requirement is associated with a security scheme, both the security
        requirement and the security scheme will be included in any generated
        OpenAPI document.

        :param scheme: Security scheme to associate with the security requirement.
        :param scope: Scheme-specific scope names required for authorization.
        """
        super().__init__()
        self.scheme = scheme
        self.scopes = scopes

    def authorize(self):
        """
        Determine authorization for the operation. Raises an exception if authorization
        is not granted. The exception raised should be a ResourceError (like
        Unauthorized), or be meaningful relative to its associated security scheme.        
        """
        raise NotImplementedError

    @property
    def json(self):
        if self.scheme:
            return {self.scheme.name: self.scopes}


class SecurityScheme:
    """
    Base class for security schemes.
    
    A security scheme is only required if security requirements and security
    schemes should be published in OpenAPI documents.
    """

    def __init__(self, name, type, *, description=None, **kwargs):
        """
        Initialize the HTTP authentication security scheme.
        
        :param name: The name of the security scheme.
        :param type: The type of security scheme.
        """
        super().__init__()
        self.name = name
        self.type = type
        self.description = description

    @property
    def context(self):
        """Context that the scheme pushes onto the context stack."""
        result = {}
        result["context_type"] = "security"
        result["security_name"] = self.name
        result["security_type"] = self.type
        return result

    @property
    def json(self):
        """JSON representation of the security scheme."""
        result = {}
        result["type"] = self.type
        if self.description is not None:
            result["description"] = self.description
        return result


class HTTPSecurityScheme(SecurityScheme):
    """Base class for HTTP authentication security scheme."""

    def __init__(self, name, scheme, **kwargs):
        """
        Initialize the HTTP authentication security scheme.
        
        :param name: The name of the security scheme.
        :param scheme: The name of the HTTP authorization scheme.
        """
        super().__init__(name, "http", **kwargs)
        self.scheme = scheme

    @property
    def context(self):
        """Context that the scheme pushes onto the context stack."""
        result = super().context
        result["security_scheme"] = self.scheme
        return result

    @property
    def json(self):
        """JSON representation of the security scheme."""
        result = super().json
        result["scheme"] = self.scheme
        return result


class HTTPBasicSecurityScheme(HTTPSecurityScheme):
    """Base class for HTTP basic authentication security scheme."""

    def __init__(self, name, realm=None, **kwargs):
        """
        Initialize the HTTP basic authentication security scheme.
        
        :param name: The name of the security scheme.
        :param realm: The realm to include in the challenge. (default: name)
        """
        super().__init__(name, "basic", **kwargs)
        self.realm = realm or name

    def Unauthorized(self, detail=None):
        """Return an Unauthorized exception populated with scheme and realm."""
        return Unauthorized(detail, "Basic realm={}".format(self.realm))

    def filter(self, request, chain):
        """
        Filters the incoming HTTP request. If the request contains credentials in the
        HTTP Basic authentication scheme, they are passed to the authenticate method.
        If authentication is successful, a context is added to the context stack.  
        """
        auth = None
        if request.authorization and request.authorization[0].lower() == "basic":
            try:
                user_id, password = b64decode(request.authorization[1]).decode().split(":", 1)
            except (binascii.Error, UnicodeDecodeError):
                pass
            auth = self.authenticate(user_id, password)
            if auth:
                with context.push({**auth, **self.context}):
                    return chain.next(request)
        return chain.next(request)

    def get_context(self):
        """Return the context that this scheme pushes on the stack."""
        return context.last(self.context)

    @property
    def context(self):
        """Context that the scheme pushes onto the context stack."""
        result = super().context
        result["http_realm"] = self.realm
        return result

    def authenticate(user_id, password):
        """
        Perform authentication of credentials supplied in the HTTP request. If
        authentication is successful, a dict is returned, which is added
        to the context that is pushed on the context stack. If authentication
        fails, None is returned. This method should not raise an exception
        unless an unrecoverable error occurs.
        """
        raise NotImplementedError


class ContextSecurityRequirement(SecurityRequirement):
    """
    Authorizes an operation if a context with the specified properies exists on the
    context stack.
    """

    def __init__(self, *args, **varargs):
        """
        Initialize context security requirement.

        The context value to search for can be expressed as follows:
        - ContextSecurityRequirement(mapping): Mapping object's key-value pairs.
        - ContextSecurityRequirement(**kwargs): Name-value pairs in keyword arguments. 

        """
        super().__init__()
        self.context = dict(*args, **varargs)

    def authorize(self):
        if not context.last(self.context):
            raise Forbidden


class CLISecurityRequirement(ContextSecurityRequirement):
    """
    Security requirement that authorizes an operation if it was initiated (directly
    or indirectly) from the command line interface.
    """
    def __init__(self):
        super().__init__(context_type="cli")


class NestedSecurityRequirement(SecurityRequirement):
    """
    Authorizes an operation if it's called (directly or indirectly) from another
    operation.
    """
    def authorize(self):
        if len(context.find(context_type="operation")) < 2:
            raise Forbidden


cli = CLISecurityRequirement()

nested = NestedSecurityRequirement()
