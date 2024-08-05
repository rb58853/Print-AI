from client import APIClient
from utils import clear_console
import asyncio

client: APIClient = APIClient()

def chating():
    clear_console()
    return asyncio.run(client.websocket_chat())


chating()
