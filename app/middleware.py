import logging
import time
from uuid import uuid4

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid4())[:8]
        start_time = time.time()

        logger.info("[%s] %s %s - Started", request_id, request.method, request.url.path)

        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000
        logger.info(
            "[%s] %s %s - Status: %s - Time: %.2fms",
            request_id, request.method, request.url.path,
            response.status_code, process_time
        )

        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = f"{process_time:.2f}ms"

        return response
