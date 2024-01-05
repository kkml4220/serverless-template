# Third Party Library
from aws_lambda_powertools import Logger


def set_logger() -> Logger:
    """Set logger for lambda function.

    Returns:
        Logger: Logger object.
    """
    return Logger(child=True)
