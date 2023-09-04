from aiohttp import web

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response(text="@SL_Bots_Updates")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app