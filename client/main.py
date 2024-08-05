from client import APIClient
from utils import clear_console
import asyncio

client: APIClient = APIClient(
    http_url="https://dev.chat.flowychat.com/api",
    ws_url="wss://dev.chat.flowychat.com/api",
    port="8080",
)


def chating():
    clear_console()
    return asyncio.run(client.websocket_chat())


chating()
