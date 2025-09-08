import time, uuid
from typing import Optional, Dict, Any
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

# --- Replace with real JWT validation in prod ---
def verify_token(token: str) -> Dict[str, Any]:
    if token == "admin-token":
        return {"sub": "42", "roles": ["admin", "driver"]}
    if token == "driver-token":
        return {"sub": "99", "roles": ["driver"]}
    raise ValueError("invalid token")

class RequestContextMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, require_auth: bool = True):
        super().__init__(app)
        self.require_auth = require_auth

    async def dispatch(self, request: Request, call_next):
        start = time.time()
        req_id = str(uuid.uuid4())
        request.state.request_id = req_id

        # --- Auth (skip for docs/health if you want) ---
        user: Optional[Dict[str, Any]] = None
        auth = request.headers.get("authorization", "")
        if auth.lower().startswith("bearer "):
            token = auth.split(" ", 1)[1]
            try:
                user = verify_token(token)
            except Exception:
                return Response(status_code=401, content='{"detail":"invalid token"}',
                                media_type="application/json")
        elif self.require_auth and request.url.path.startswith("/api"):
            return Response(status_code=401, content='{"detail":"missing token"}',
                            media_type="application/json")

        request.state.user = user

        # Continue pipeline
        response: Response = await call_next(request)
        # Add request id and timing
        response.headers["X-Request-ID"] = req_id
        response.headers["X-Response-Time-ms"] = f"{(time.time()-start)*1000:.2f}"
        return response

def add_middlewares(app):
    app.add_middleware(RequestContextMiddleware, require_auth=True)
