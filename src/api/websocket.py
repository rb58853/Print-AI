from src.api.app import app, WebSocket
from src.app.chat.chat import Chat
import logging
import json


@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        await websocket.send_text(f"connected")

    except Exception as e:
        logging.error(f"websocket.accept failed: {e}")
        return

    chat = Chat()

    try:
        while True:
            logging.info(f"waiting query from user")
            try:
                query = await websocket.receive_text()
                await chat.send_query(query)
            except:
                logging.warning("internal server error")
                response = {
                    "response": "internal server error, try resend your question",
                    "products": [],
                }
                await websocket.send_text(json.dumps(response))

    except Exception as e:
        logging.error(str(e))
        try:
            await websocket.send_text(f"error: {e}")
        except Exception as e:
            logging.error(f"send error: {e}")
    finally:
        try:
            await websocket.close(code=1000)
        except:
            pass
