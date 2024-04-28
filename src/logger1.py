import logging
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%d_%m_%y_%I_%M_%S')}.log" #%I for 12 hour format and %H for 24 hrs format
logs_path= os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH =os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# if __name__=="__main__":
#     print("working")
#     logging.info("Logging has started just now")