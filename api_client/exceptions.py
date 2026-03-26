class APIClientError(Exception):
    pass

class ValidationError(APIClientError):
    pass

class NetworkError(APIClientError):
    pass

class APIResponseError(APIClientError):
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code=status_code

class UnauthorizedError(APIResponseError):
    pass

class NotFoundError(APIResponseError):
    pass

class ServerError(APIResponseError):
    pass

