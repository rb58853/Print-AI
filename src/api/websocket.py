from src.api.app import app, WebSocket
from src.app.chat.chat import Chat
import logging
import json


@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        # await websocket.send_text(f"connected")

    except Exception as e:
        logging.error(f"websocket.accept failed: {e}")
        return

    chat = Chat()

    try:
        while True:
            logging.info(f"waiting query from user")
            try:
                query = await websocket.receive_text()
                response = await chat.send_query(query)
                #  chat.process_query(query)
                await websocket.send_text(response)

            except:
                logging.warning("internal server error")
                await websocket.send_text(
                    json.dumps("internal server error, try resend your question")
                )

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
