import time

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

from app.storage import client_requests


class RateLimitMiddleware(BaseHTTPMiddleware):

    LIMIT = 9

    WINDOW = 10

    async def dispatch(self, request, call_next):

        client_id = request.headers.get("X-Client-Id", "anonymous")

        now = time.time()

        timestamps = client_requests[client_id]

        timestamps[:] = [
            t for t in timestamps
            if now - t < self.WINDOW
        ]

        if len(timestamps) >= self.LIMIT:
            return JSONResponse(
                status_code=429,
                content={
                    "detail": "Rate limit exceeded"
                }
            )

        timestamps.append(now)

        response = await call_next(request)

        return response
    
