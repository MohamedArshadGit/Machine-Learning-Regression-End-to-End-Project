import logging
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log" #IMP=>.log": This is the suffix of the filename. It's a literal string indicating that the file will have a .log extension.
#%I for 12 hour format and %H for 24 hrs format
#datetime.now(): This calls the now() method of the datetime class from the datetime module. It returns a datetime object representing the current date and time.
#.strftime() string format time is a method in Python used to format datetime objects into strings. It stands for "string format time". This method takes a format string as an argument and returns a string representing the datetime object according to the specified format.

# _By using underscores (_) as separators, the resulting formatted string will have clear visual separation between different components of the date and time, making it easier to interpret and work with.
# The choice of separator depends on your preference and the readability of the formatted output.
#For example, instead of underscores, you could use hyphens (-), slashes (/), dots (.), or any other character to separate the components. Here's an example of using hyphens as separators:
#code example
#LOG_FILE = f"Time:{datetime.now().strftime('%m-%d-%y-%h-%m-%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #, the string "logs" is used as a directory name(IMP=>Directory name not file name Note it). This line of code constructs a file path by joining the current working directory (os.getcwd()) with the directory name "logs" and the log file name LOG_FILE.
os.makedirs(logs_path,exist_ok=True) #When exist_ok is set to True, it tells the function not to raise an error if the directory already exists. If exist_ok is False (the default), and the directory already exists, makedirs will raise a FileExistsError.

LOG_FILE_PATH =os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__=="__main__": # Important =>The line if __name__ == "__main__": is a common idiom used in Python scripts to check if the script is being run as the main program or if it's being imported as a module into another script.
# Important=>If the script is being imported as a module into another script, __name__ is set to the name of the module instead of "__main__"
    logging.info("Logging has started Now")