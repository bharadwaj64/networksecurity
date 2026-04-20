import logging 
import os 
from datetime import datetime 

log_file = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(),'logs',log_file)

os.makedirs(os.path.dirname(logs_path),exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    filename= logs_path,
    format= '%(asctime)s - %(levelname)s - %(message)s',   
)
