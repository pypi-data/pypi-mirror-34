# -*- coding: utf-8 -*-
"""
    flaskbb.core.exceptions
    ~~~~~~~~~~~~~~~~~~~~~~~

    Exceptions raised by flaskbb.core,
    forms the root of all exceptions in
    FlaskBB.

    :copyright: (c) 2014-2018 the FlaskBB Team
    :license: BSD, see LICENSE for more details
"""


class BaseFlaskBBError(Exception):
    """
    Root exception for FlaskBB.
    """


class ValidationError(BaseFlaskBBError):
    """
    Used to signal validation errors for things such as
    token verification, user registration, etc.

    :param str attribute: The attribute the validation error applies to,
        if the validation error applies to multiple attributes or to
        the entire object, this should be set to None
    :param str reason: Why the attribute, collection of attributes or object
        is invalid.
    """

    def __init__(self, attribute, reason):
        self.attribute = attribute
        self.reason = reason
        super(ValidationError, self).__init__((attribute, reason))


class StopValidation(BaseFlaskBBError):
    """
    Raised from validation handlers to signal that
    validation should end immediately and no further
    processing should be done.

    Can also be used to communicate all errors
    raised during a validation run.

    :param reasons: A sequence of `(attribute, reason)` pairs explaining
        why the object is invalid.
    """

    def __init__(self, reasons):
        self.reasons = reasons
        super(StopValidation, self).__init__(reasons)
