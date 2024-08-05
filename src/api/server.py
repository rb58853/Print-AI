from dotenv import load_dotenv
from src.config.loggingConfig import get_logger
load_dotenv()
logger = get_logger(__name__)

from src.api.websocket import app
# from src.api.app import app
