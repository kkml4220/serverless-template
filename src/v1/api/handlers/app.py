# Third Party Library
from api.middlewares.common import event_middleware
from api.routes import user
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, CORSConfig
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent
from aws_lambda_powertools.utilities.typing import LambdaContext
from config.settings import API_CORS_ALLOWED_ORIGINS, API_VERSION

logger = Logger()

api_prefix: str = f"/api/{API_VERSION}"

cors_config = CORSConfig(allow_origin=API_CORS_ALLOWED_ORIGINS, max_age=300)
app = APIGatewayRestResolver(cors=cors_config, debug=True)
app.include_router(user.router, prefix=f"{api_prefix}/users")


@event_middleware
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: APIGatewayProxyEvent, context: LambdaContext) -> dict[str, str | int]:
    return app.resolve(event, context)


@app.get("/healthcheck", cors=True)
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
