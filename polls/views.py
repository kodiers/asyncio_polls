from aiohttp import web
import aiohttp_jinja2


async def index(request):
    return web.Response(text='Hello aiohttp')


# TODO: complete views
# @aiohttp_jinja2.template('detail.html')
# async def poll(request):
#     async with request.app['db'].acquire() as conn:
#         question_id = request.match_info['question_id']
#         try:
#             question, choices = await db.get_question(conn)
