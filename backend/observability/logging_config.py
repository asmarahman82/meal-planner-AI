import logging
import structlog

def setup_logging():
    logging.basicConfig(
        format="%(message)s",
        level=logging.INFO
    )

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ]
    )

