import logging
import sys

import uvicorn

from my_app.setup.setup import setup_app

logger = logging.getLogger("main")
handler = logging.StreamHandler(sys.stderr)
logging.basicConfig(
    level=logging.DEBUG,
    style="{",
    format="[{asctime}] {levelname} {name}: {message}",
    datefmt="%H:%M:%S",
    handlers=[handler],
)

if __name__ == "__main__":
    app = setup_app()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )
