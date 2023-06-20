import os
import sys
import logging

# logger string format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # writes the logs into runninglog
        logging.StreamHandler(sys.stdout),  # writes the logs into the terminal
    ],
)

logger = logging.getLogger("cnnClassifierLogger")
