from fastapi import FastAPI, status
from http_src.controllers.chat_controller import router as chat_router
from http_src.middlewares.auth import RequestContextMiddleware

def create_app() -> FastAPI:
    app = FastAPI(
        title="Chat API", 
        version="0.0.1",
        root_path="/api"
    )
    app.add_middleware(RequestContextMiddleware, require_auth=True)
    app.include_router(chat_router)
    return app

app = create_app()

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"}
