''' Exceptions for alias manager'''

class Error(Exception):
    pass

class AliasExistsError(Error):
    message = 'Alias already exists'

class AliasNotFoundError(Error):
    message = 'Alias not found'

class InvalidAliasValueError(Error):
    message = 'Invalid alias value'
