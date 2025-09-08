from fastapi import FastAPI
from http_src.controllers.chat_controller import router as chat_router
from http_src.middlewares.auth import RequestContextMiddleware

def create_app() -> FastAPI:
    app = FastAPI(
        title="Chat API", 
        version="1.0",
        prefix="/api"
    )
    app.add_middleware(RequestContextMiddleware, require_auth=True)
    app.include_router(chat_router)
    return app

app = create_app()
