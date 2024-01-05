# Standard Library
from typing import Callable

# Third Party Library
from aws_lambda_powertools.middleware_factory import lambda_handler_decorator


@lambda_handler_decorator
def event_middleware(handler: Callable, event: dict, context: dict) -> Callable:
    """event middleware null body

    Args:
        handler (Callable): lambda handler
        event (dict): lambda event
        context (dict): lambda context

    Returns:
        Callable: lambda handler response
    """
    body: dict | None = event["body"]
    if not body:
        body = {}
    response = handler(event, context)
    return response  # type: ignore
