import logging
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log" #IMP=>.log": This is the suffix 
#of the filename. It's a literal string indicating that the file will have a .log extension.
#%I for 12 hour format and %H for 24 hrs format
#datetime.now(): This calls the now() method of the datetime class from the datetime module. 
# It returns a datetime object representing the current date and time.
# IMPORTANT:=> .strftime() string format time is a method in Python used to format datetime objects
# into strings.
# It stands for "string format time". This method takes a format string as an argument 
# and returns a string representing the datetime object according to the specified format.

# _By using underscores (_) as separators, the resulting formatted string will have clear visual separation between different components of the date and time, making it easier to interpret and work with.
# The choice of separator depends on your preference and the readability of the formatted output.
#For example, instead of underscores, you could use hyphens (-), slashes (/), dots (.), or any other character to separate the components. Here's an example of using hyphens as separators:
#code example
#LOG_FILE = f"Time:{datetime.now().strftime('%m-%d-%y-%h-%m-%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) 
#os.path.join() is a versatile and essential tool for CONSTRUCTING FILE PATHS in a
# platform-independent and reliable manner

# The line os.path.join(os.getcwd(),"logs",LOG_FILE) is constructing a file path using
# the os.path.join() function.
# Let's break down what each part of this line is doing:

# os.getcwd(): This function returns the current working directory as a "string". 
# It retrieves the path of the directory from which the Python script is currently being executed.

# "logs": This is a string representing the name of a directory called "logs".
# It's a relative path component that will be joined with the current working directory.

# LOG_FILE: This is likely a variable that holds the name of a log file which is string
# It's another relative path component that will be joined with the previous components.
# Combining these components using os.path.join() results in a complete file path.
# The function intelligently handles the concatenation, taking into account 
# the appropriate path separator for the operating system being used.

# For example, if the current working directory is /home/user, and LOG_FILE contains the
# value "app.log", then the resulting path might be /home/user/logs/app.log.==>>VERY VERY IMPORTANT
# THIS IS THE PURPOSE OF os.path.join()
# This path represents the location of a log file named "app.log" within a directory
# named "logs" in the current working directory.

#VERY VERY IMPORTANT:Inside os.path.join() parameters are expected to be a string
# The os.path.join() function in Python accepts multiple string arguments representing path components. 
# These components can be strings containing directory names, file names, or a combination of both.
# # to os.path.join(), it will be treated as a string and concatenated with the other path
# components provided.
#If LOG_FILE is not a string, you would likely encounter an error unless it can be converted 
# to a string implicitly or explicitly.
# Generally, it's best practice to ensure that all path components passed
# to os.path.join() are strings.

# the string "logs" is used as a directory name(IMP=>Directory name not file name Note it).
# This line of code constructs a file path by joining the current working directory (os.getcwd()) with
# the directory name "logs" and the log file name LOG_FILE.

os.makedirs(logs_path,exist_ok=True) #When exist_ok is set to True, it tells the function
#not to raise an error if the directory already exists.
# If exist_ok is False (the default), and the directory already exists, 
# makedirs will raise a FileExistsError.

LOG_FILE_PATH =os.path.join(logs_path,LOG_FILE) #So, while line 2 constructs the path to the directory 
#logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) where log files are stored,
# line 4 LOG_FILE_PATH =os.path.join(logs_path,LOG_FILE) specifically constructs the full path
# to the individual log file within that directory.

#In essence, line 2 prepares the directory structure, and line 4 specifies the exact location
# of the log file within that directory.

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# if __name__=="__main__": # Important =>The line if __name__ == "__main__": is a common idiom used 
# #in Python scripts to check if the script is being run as the main program or if it's being imported
# # as a module into another script.
# # Important=>If the script is being imported as a module into another script, __name__ is set to the
# # name of the module instead of "__main__"
#     logging.info("Logging has started Now")