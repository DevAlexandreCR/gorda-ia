from fastapi import FastAPI, status, Depends
from fastapi.security import HTTPBearer
from http_src.controllers.chat_controller import router as chat_router
from http_src.middlewares.auth import RequestContextMiddleware

# Global security scheme
security = HTTPBearer()

def create_app() -> FastAPI:
    api: FastAPI = FastAPI(
        title="Chat API", 
        version="0.0.1",
        root_path="/api"
    )
    
    # Add middleware and protected routes
    api.add_middleware(RequestContextMiddleware, require_auth=True)
    api.include_router(chat_router, dependencies=[Depends(security)])
    return api

app = create_app()

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"}

