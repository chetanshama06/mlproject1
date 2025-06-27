import logging
import os
from datetime import datetime

# Generate the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs path under the desired structure
logs_path = os.path.join(os.getcwd(), "logs", "mlprojects.egg-info", "src")
os.makedirs(logs_path, exist_ok=True)  # Create directories if they don't exist

# Complete path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


