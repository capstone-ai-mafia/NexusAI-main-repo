import logging
import os
from pathlib import Path


LOG_DIR = Path(os.getenv("LOG_DIR", "logs")).expanduser()
LOG_DIR.mkdir(exist_ok=True, parents=True)


logging.basicConfig(
    filename=str(LOG_DIR / "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger("nexus_ai")