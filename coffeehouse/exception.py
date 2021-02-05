import json


__all__ = ["CoffeeHouseError"]


class CoffeeHouseError(Exception):
    """
    Exception raised by API errors.
    The exception message is set to the server's response.

    :param status_code: Status code returned by the server
    :type status_code: int
    :param message: Response content returned by the server
    :type message: str
    :param request_id: The request ID returned by the server
    :type request_id: str
    """

    def __init__(self, status_code, content, request_id):
        self.status_code = status_code
        self.content = content
        self.request_id = request_id
        self.message = content.get("message", None) if content else "Unknown"
        super().__init__(self.message or content)

    @staticmethod
    def parse_and_raise(status_code, content, request_id):
        """
        Raise an exception if applicable, otherwise return the
        response of the method

        :param status_code: Status code returned by the server
        :type status_code: int
        :param content: Response content returned by the server
        :type content: str
        :param request_id: The request ID returned by the server
        :type request_id: str
        :rtype dict
        """

        try:
            response = json.loads(content)
        except json.decoder.JSONDecodeError:
            raise CoffeeHouseError(status_code, None, request_id)
        if status_code != 200:
            raise _mapping.get(
                status_code,
                CoffeeHouseError
            )(
                status_code,
                response,
                request_id
            )
        return response


class InternalServerError(CoffeeHouseError):
    """
    There was an unexpected error while processing your request,
    this is most likely a server issue/bug
    """
    pass


class GenericError(CoffeeHouseError):
    """
    This is a generic error from the API,
    read the message for more details.
    """
    pass


class MissingSessionIDParameter(CoffeeHouseError):
    """
    The server was expecting the parameter ‘session_id’,
    which was not provided by the client
    """
    pass


class MissingInputParameter(CoffeeHouseError):
    """
    The server was expecting the parameter ‘input’,
    which was not provided by the client
    """
    pass


class InvalidInputParameter(CoffeeHouseError):
    """
    The parameter ‘input’ contains an invalid value,
    the value cannot be empty.
    """
    pass


class SessionNotFoundError(CoffeeHouseError):
    """
    The requested session could not be found on the server
    """
    pass


class SessionNotAvailableError(CoffeeHouseError):
    """
    The requested session has expired or an error has raised,
    which enabled the session to no longer be available
    """
    pass


class LanguageError(CoffeeHouseError):
    """
    The given language code is not a valid
    ISO 639-1 Language code/language name that the server is willing to accept.
    """
    pass


class QuotaLimitError(CoffeeHouseError):
    """
    You reached the quota limit of the method/resource,
    if you need more then upgrade your subscription plan
    """
    pass


class SessionError(CoffeeHouseError):
    """
    The session cannot be created because CoffeeHouse is temporarily unavailable.
    If this issues continues then report it to support.
    """
    pass


class SessionAttributeError(CoffeeHouseError):
    """
    You are attempting to get the session attributes of a session that does not contain any attributes,
    likely an old session.
    """
    pass


class ErrorReserved(CoffeeHouseError):
    """
    This error code will not be returned,
    it's reserved for a future update.
    """
    pass


class Base64DataError(CoffeeHouseError):
    """
    The base64 data you provided is not valid or malformed
    """
    pass


class UnSupportedFileTypeError(CoffeeHouseError):
    """
    The file you tried to upload to the API is not supported by the method
    """
    pass


class ServiceUnavailableError(CoffeeHouseError):
    """
    The service is temporarily unavailable,
    because our internal software CoffeeHouse-Utils is not available,
    if this issue continues then report it to support.
    """
    pass


class MissingImageDataError(CoffeeHouseError):
    """
    The API acknowledges that you are attempting to upload a file,
    but does not see any data for the file either in the body request or as a parameter
    """
    pass


class InvalidGeneralizationError(CoffeeHouseError):
    """
    The value you requested for the generalization size is not applicable and invalid,
    it should be number but not less than 1
    """
    pass


class ExceededGeneralizationError(CoffeeHouseError):
    """
    The value you entered for the generalization size
    is more than what your subscription allows
    """
    pass


class MissingGeneralizationSizeError(CoffeeHouseError):
    """
    The expected parameter 'generalization_size' is missing
    """
    pass


class GeneralizationTableError(CoffeeHouseError):
    """
    The requested generalization table provided via the 'generalization_id' parameter was not found
    """
    pass


class InvalidGeneralizationMethodError(CoffeeHouseError):
    """
    This method cannot generalize the results
    """
    pass


class ExceedInputLimitError(CoffeeHouseError):
    """
    The 'input' parameter exceeds the limit that your subscription allows
    """
    pass


class InputEmptyError(CoffeeHouseError):
    """
    The expected parameter 'input' is missing
    """
    pass


class LanguageNotSupportedError(CoffeeHouseError):
    """
    The requested language source has been identified but it's not supported by this method yet
    """
    pass


class InputProcessError(CoffeeHouseError):
    """
    The cannot process the given input due to internal server errors, report this issue to support.
    """
    pass


_mapping = {
    -1: InternalServerError,
    0: GenericError,
    1: MissingSessionIDParameter,
    2: MissingInputParameter,
    3: InvalidInputParameter,
    4: SessionNotFoundError,
    5: SessionNotAvailableError,
    6: QuotaLimitError,
    7: LanguageError,
    8: SessionError,
    9: SessionAttributeError,
    10: ErrorReserved,
    11: Base64DataError,
    12: UnSupportedFileTypeError,
    13: ServiceUnavailableError,
    14: MissingImageDataError,
    15: InvalidGeneralizationError,
    16: ExceededGeneralizationError,
    17: MissingGeneralizationSizeError,
    18: GeneralizationTableError,
    19: InvalidGeneralizationMethodError,
    20: MissingInputParameter,
    21: ExceedInputLimitError,
    22: InputEmptyError,
    23: LanguageNotSupportedError,
    24: InputProcessError,
}
