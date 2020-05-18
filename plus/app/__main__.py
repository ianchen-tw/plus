import logging

import uvicorn
from app.main import server

# This is the entrypoint of this package
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.info("Manually running this script.... for debug usage'")
