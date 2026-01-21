import logging
from rich.logging import RichHandler

_LOGGER = None

def get_logger():
    global _LOGGER
    if _LOGGER:
        return _LOGGER

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )

    _LOGGER = logging.getLogger("QueryBridge")
    return _LOGGER
