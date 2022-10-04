class TheFileIsEmpty(Exception):
    """The exception base class TheFileIsEmpty"""


class MismatchedNumberOfColumns(Exception):
    """The exception base class MismatchedNumberOfColumns"""


class TheFileIsTooLarge(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
