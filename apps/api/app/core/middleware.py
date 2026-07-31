import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class RequestMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        request_id = str(uuid.uuid4())

        request.state.request_id = request_id

        start = time.time()

        response = await call_next(request)

        elapsed = time.time() - start

        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = str(round(elapsed, 4))

        return response