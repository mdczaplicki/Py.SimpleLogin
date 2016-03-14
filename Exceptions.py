class RecordsNumberException(Exception):
    def __init__(self, msg):
        super(Exception, self).__init__(msg)


class UserAlreadyExistsException(Exception):
    def __init__(self, msg):
        super(Exception, self).__init__(msg)