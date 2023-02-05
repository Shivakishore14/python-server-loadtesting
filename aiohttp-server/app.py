from aiohttp import web
import asyncio
import boto3


routes = web.RouteTableDef()
client = boto3.client('dynamodb')


@routes.get('/hello')
async def hello_handler(request):
    return web.Response(text="Hello, world from aiohttp")

@routes.get('/sleep')
async def sleep_handler(request):
    await asyncio.sleep(0.5)
    return web.Response(text="sleep .5 from aiohttp")

@routes.get('/ddb_get')
async def ddb_get_handler(request):
    response = client.get_item(TableName="LoadTestingTable",
                    Key={
                        "pk": {"S": "test"},
                        "sk": {"S": "test1"}
                    })
    data = response.get("Item").get("data").get("S")
    return web.Response(text=f"ddb_get response from aiohttp {data}")

app = web.Application()
app.add_routes(routes)
web.run_app(app)
