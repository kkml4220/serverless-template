# Standard Library
import json
from enum import Enum

# Third Party Library
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, Response
from aws_lambda_powertools.event_handler.api_gateway import Router

app = APIGatewayRestResolver(debug=True)
router = Router()


class UserResponseMessage(Enum):
    USER_NOT_FOUND = "user not found"
    USER_DELETED_SUCCESSFULLY = "user deleted successfully"
    USER_DELETED_SUCCESSFULLY_COMPLETLY = "user deleted successfully completely"


@router.get("/", cors=True)
def health_check() -> Response[str]:
    return Response(status_code=200, body=json.dumps({"message": "OK"}))
