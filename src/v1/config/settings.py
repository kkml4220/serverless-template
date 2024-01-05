# Third Party Library
from decouple import config

# API settings
API_VERSION = config("API_VERSION", default="v1", cast=str)
API_CORS_ALLOWED_ORIGINS = config("API_CORS_ALLOWED_ORIGINS", default="*", cast=str)
