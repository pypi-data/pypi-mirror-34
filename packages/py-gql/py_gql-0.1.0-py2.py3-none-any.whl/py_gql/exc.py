# -*- coding: utf-8 -*-
# pylint: disable = too-many-ancestors
""" All exceptions for this library are defined in the :mod:`py_gql.exc`
module. """

from ._string_utils import highlight_location, index_to_loc, stringify_path
from ._utils import cached_property


class GraphQLError(Exception):
    """ Base GraphQL exception from which all other inherit. """

    def __init__(self, message):
        super(GraphQLError, self).__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class GraphQLResponseError(GraphQLError):
    """ Implementors of this are suitable for usage in GraphQL responses and
    exposing to end users. """

    def to_dict(self):
        raise NotImplementedError()


class GraphQLSyntaxError(GraphQLResponseError):
    """ The GraphQL document is invalid.

    Args:
        message (str): Explanatory message
        position (int): 0-indexed position locating the syntax error
        source (str): Source string from which the syntax error originated

    Attributes:
        message (str): Explanatory message
        position (int): 0-indexed position locating the syntax error
        source (str): Source string from which the syntax error originated
    """

    def __init__(self, message, position, source):
        super(GraphQLSyntaxError, self).__init__(message)
        self.source = source
        self.position = position

    @cached_property
    def highlighted(self):
        """ str: Message followed by a view of the source document pointing at
        the exact location of the error. """
        if self.source is not None:
            return (
                self.message
                + " "
                + highlight_location(self.source, self.position)
            )
        return self.message

    def __str__(self):
        return self.highlighted

    def to_dict(self):
        """ Convert the exception to a dictionnary that can be serialized to
        JSON and exposed in a graphql response.

        Returns:
            dict: Dict representation of the error.
        """
        line, col = index_to_loc(self.source, self.position)
        return {
            "message": str(self),
            "locations": [{"line": line, "columne": col}],
        }


class InvalidCharacter(GraphQLSyntaxError):
    pass


class UnexpectedCharacter(GraphQLSyntaxError):
    pass


class UnexpectedEOF(GraphQLSyntaxError):
    """
    Args:
        position (int): 0-indexed position locating the syntax error
        source (str): Source string from which the syntax error originated
    """

    def __init__(self, position, source):
        super(UnexpectedEOF, self).__init__(
            "Unexpected <EOF>", position, source
        )


class NonTerminatedString(GraphQLSyntaxError):
    pass


class InvalidEscapeSequence(GraphQLSyntaxError):
    pass


class UnexpectedToken(GraphQLSyntaxError):
    pass


class GraphQLLocatedError(GraphQLResponseError):
    """ Error that can be traced back to specific position(s) in the source
    document.

    Args:
        message (str): Explanatory message
        nodes (Optional[List[py_gql.lang.ast.Node]]):
            Node or nodes relevant to the exception
        path (list): Location of the error during execution

    Attributes:
        message (str): Explanatory message
        nodes (List[py_gql.lang.ast.Node]): Node or nodes relevant to the exception
        path (list): Location of the error during execution
    """

    def __init__(self, message, nodes=None, path=None):
        super(GraphQLLocatedError, self).__init__(message)
        self.path = path
        self.nodes = nodes[:] if nodes else []

    def __str__(self):
        return self.message

    def to_dict(self):
        """ Convert the exception to a dictionnary that can be serialized to
        JSON and exposed in a graphql response.

        Returns:
            dict: Dict representation of the error.
        """
        kv = (
            ("message", str(self)),
            (
                "locations",
                [
                    {"line": line, "column": col}
                    for line, col in (
                        index_to_loc(node.source, node.loc[0])
                        for node in self.nodes
                        if node.loc and node.source
                    )
                ],
            ),
            ("path", self.path if self.path is not None else None),
        )
        return {k: v for k, v in kv if v}


class InvalidValue(GraphQLLocatedError, ValueError):
    pass


class UnknownEnumValue(InvalidValue):
    pass


class UnknownVariable(InvalidValue):
    pass


class ScalarSerializationError(GraphQLError, ValueError):
    pass


class ScalarParsingError(InvalidValue):
    pass


class SchemaError(GraphQLError):
    pass


class UnknownType(SchemaError, KeyError):
    pass


class ValidationError(GraphQLLocatedError):
    pass


class ExecutionError(GraphQLResponseError):
    """ Error that prevented execution.

    Args:
        message (str): Explanatory message

    Attributes:
        message (str): Explanatory message
    """

    def to_dict(self):
        """ Convert the exception to a dictionnary that can be serialized to
        JSON and exposed in a graphql response.

        Returns:
            dict: Dict representation of the error.
        """
        return {"message": str(self)}


class VariableCoercionError(GraphQLLocatedError):
    pass


class VariablesCoercionError(GraphQLError):
    """ Collection of multiple :class:`VariableCoercionError`.

    Args:
        errors (List[VariableCoercionError]): Wrapped errors

    Attributes:
        errors (List[VariableCoercionError]): Wrapped errors
    """

    def __init__(self, errors):
        super(VariablesCoercionError, self).__init__("%d errors" % len(errors))
        self.errors = errors

    def __str__(self):
        if len(self.errors) == 1:
            return str(self.errors[0])
        return ",\n".join([str(err) for err in self.errors])


class CoercionError(GraphQLLocatedError):
    def __init__(self, message, node=None, path=None, value_path=None):
        super(CoercionError, self).__init__(message, node, path)
        self.value_path = value_path

    def __str__(self):
        if self.value_path:
            return "%s at %s" % (self.message, stringify_path(self.value_path))
        return self.message


class MultiCoercionError(CoercionError):
    """ Collection of multiple :class:`CoercionError`.

    Args:
        errors (List[CoercionError]): Wrapped errors

    Attributes:
        errors (List[CoercionError]): Wrapped errors
    """

    def __init__(self, errors):
        super(MultiCoercionError, self).__init__("%d errors" % len(errors))
        self.errors = errors

    def __str__(self):
        if len(self.errors) == 1:
            return str(self.errors[0])
        return ",\n".join([str(err) for err in self.errors])


class ResolverError(GraphQLLocatedError):
    """ Raised when an expected error happens during field resolution.

    Subclass or raise this exception directly for use in your own
    resolvers in order for them to report errors instead of crashing execution.
    If your exception exposes an ``extensions`` attribute it will be included
    in the serialized version without the need to override :meth:`to_dict`.

    Args:
        message (str): Explanatory message
        nodes (Optional[Union[List[py_gql.lang.ast.Node], py_gql.lang.ast.Node]]):
            Node or nodes relevant to the exception
        path (list): Location of the error during execution
        extensions (Optional[dict]): Error extensions

    Attributes:
        message (str): Explanatory message
        nodes (List[py_gql.lang.ast.Node]): Node or nodes relevant to the exception
        path (list): Location of the error during execution
        extensions (Optional[dict]): Error extensions

    """

    def __init__(self, message, nodes=None, path=None, extensions=None):
        super(ResolverError, self).__init__(message, nodes, path)
        self.extensions = extensions

    def to_dict(self):
        """ Convert the exception to a dictionnary that can be serialized to
        JSON and exposed in a graphql response.

        Returns:
            dict: Dict representation of the error.
        """
        dict_ = super(ResolverError, self).to_dict()
        if self.extensions:
            dict_["extensions"] = dict(self.extensions)
        return dict_


class SDLError(GraphQLLocatedError):
    """ Error that occured when parsing and / or applying a schema definition
    document (SDL). """

    pass


class ExtensionError(SDLError):
    """ Error that occured when applying a schema or type extension node
    to an existing schema. """

    pass


class SchemaDirectiveError(SDLError):
    pass
