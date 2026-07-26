class MeaningFirstError(Exception):
    """Base exception for expected domain failures."""


class ParseError(MeaningFirstError):
    """A content block or project file could not be parsed."""


class ValidationFailure(MeaningFirstError):
    """Validation finished with one or more errors."""
