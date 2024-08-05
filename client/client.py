import asyncio
import websockets
import json
import logging


class APIClient:
    def __init__(
        self,
        http_url: str = "http://127.0.0.1:8080",
        ws_url="ws://127.0.0.1:8080",
    ) -> None:
        self.http_url = f"{http_url}"
        self.ws_url = f"{ws_url}"

    async def websocket_chat(self):
        uri = f"{self.ws_url}/ws/chat"

        async with websockets.connect(uri, ping_interval=None) as websocket:
            while True:
                try:
                    query = input("> ")
                    await websocket.send(query)
                    response = await asyncio.wait_for(websocket.recv(), timeout=100)

                    try:
                        response = json.loads(response)
                        print(f"< {response['response']}")
                    except:
                        print(f"< {response}")

                except Exception as e:
                    logging.error(e)
                    break
