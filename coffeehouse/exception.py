class CoffeeHouseError(Exception):
    """
    Exception raised by API errors.
    The exception message is set to the server's response.

    :param status_code: Status code returned by the server
    :type status_code: int
    :param content: Response content returned by the server
    :type content: string
    """
    def __init__(self, message, status_code, content=None):
        super(CoffeeHouseError, self).__init__(message)
        self.status_code = status_code
        self.content = content