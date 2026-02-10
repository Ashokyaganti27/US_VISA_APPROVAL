
import logging
import os
from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_folder = "logs"

log_dir = os.path.join(from_root(),log_folder)

os.makedirs(log_dir,exist_ok=True)

log_path = os.path.join(log_dir,LOG_FILE)


logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger =logging.getLogger("demo")

