from litestar import Request
from litestar.exceptions import NotAuthorizedException
from typing import Any
from app.core.auth.jwt import verify_token


async def jwt_guard(request: Request, _: Any) -> None:
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise NotAuthorizedException("Missing or invalid Authorization header")

    token = auth_header.removeprefix("Bearer ").strip()
    payload = verify_token(token)

    request.state.user = payload
