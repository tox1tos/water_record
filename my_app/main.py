import uvicorn

from my_app.setup.setup import setup_app

if __name__ == "__main__":
    app = setup_app()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )


import logging
import logging.handlers
import sys

logger = logging.getLogger("main")

log_file = open("log.txt", "a")

handler = logging.StreamHandler(sys.stderr)
file_handler = logging.StreamHandler(log_file)

logging.basicConfig(
    level=logging.DEBUG,
    style="{",
    format="[{asctime}] {levelname} {name}: {message}",
    datefmt="%H:%M:%S",
)
logging.log(logging.INFO, "My_message")
logging.info("Information message")
logging.error("Some error")
logging.debug("Just debug message")

log_file.close()
