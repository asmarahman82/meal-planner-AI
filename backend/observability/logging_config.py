import logging
import sys

def setup_logging():
    """
    Configure simple application logging.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )

    logging.info("✅ Simple logging initialized (no JSON formatter).")

