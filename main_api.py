from fastapi import FastAPI
from api.routes import router
from api.exceptions import APIException, api_exception_handler
from config.logging_config import configure_logging

app = FastAPI(
    title="Smart Travel Planning System",
    version="2.0.0"
)

configure_logging()

# include routes
app.include_router(router)

# register exception handler
app.add_exception_handler(APIException, api_exception_handler)