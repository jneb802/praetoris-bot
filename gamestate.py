"""Game state HTTP receiver — accepts POSTs from BepInEx mod, serves state to the bot."""

from datetime import datetime, timezone

from aiohttp import web

_state: dict | None = None


def get_state() -> dict | None:
    return _state


async def _handle_game_state(request: web.Request) -> web.Response:
    global _state

    api_key = request.app["api_key"]
    if request.headers.get("X-API-Key") != api_key:
        return web.json_response({"error": "unauthorized"}, status=401)

    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "invalid json"}, status=400)

    players = data.get("players")
    if not isinstance(players, list):
        return web.json_response({"error": "players must be a list"}, status=422)

    _state = {
        "players": [str(p) for p in players],
        "day": int(data.get("day", 0)),
        "game_time": str(data.get("game_time", "00:00")),
        "is_day": bool(data.get("is_day", True)),
        "last_updated": datetime.now(timezone.utc),
    }

    return web.json_response({"status": "ok"})


async def _handle_health(request: web.Request) -> web.Response:
    has_data = _state is not None
    return web.json_response({"status": "ok", "has_data": has_data})


async def start_server(port: int, api_key: str):
    app = web.Application()
    app["api_key"] = api_key
    app.router.add_post("/api/game-state", _handle_game_state)
    app.router.add_get("/api/health", _handle_health)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Game state server listening on 0.0.0.0:{port}")
