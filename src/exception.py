import sys # any exception happens sys haves that information..# to work with system level operations
#and interactions of python interpreter sys can be used

import logger
from logger import *

def error_message_detail(error,error_detail:sys): #error_detail is a reference to the sys module, 
    #allowing access to information about the exception.
    
    _,_,exc_tb=error_detail.exc_info() #uses the exc_info() method from the sys module to retrieve 
    #information about the current exception being handled. It returns a tuple containing information
    # about the exception currently being handled, including its type, value, and traceback. 
    
    file_name =exc_tb.tb_frame.f_code.co_filename  #This line extracts the file name from the traceback
    #object (exc_tb). It navigates through the traceback to get the filename where the exception occurred.
    
    error_message="Error Occured in python script file :[{0}] line number:[{1}] error message: [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)   
    ) #This line constructs the error message string using string formatting.
    #It includes placeholders {0}, {1}, and {2} for the file name, line number, and error message,
    # respectively.
    #[] used here is just for aesthetic purposes
    
    return error_message

class CustomException(Exception): #It inherits from the built-in Exception class, making it possible 
    #to raise and handle instances of this custom exception like any other exception.
    
     def __init__(self,error_message,error_detail:sys):
          super().__init__(error_message) #This line calls the constructor of the base class
          #(Exception) using super(), passing the error_message to initialize the exception 
          # with the provided error message.
          self.error_message = error_message_detail(error_message,error_detail=error_detail) #This line 
          #invokes the error_message_detail function to generate a detailed error message based on
          # the provided error_message and the sys module reference (error_detail). 
          # The detailed error message is then assigned to the error_message attribute
          # of the CustomException object (self).
          
     def __str__(self): #This line defines the __str__ method, which is called when the object is 
         #converted to a string (e.g., when using str(exception)). 
         # It overrides the default behavior of the __str__ method inherited from the Exception class.
         
         return self.error_message #This line returns the detailed error message stored
         #in the error_message attribute when the CustomException object is converted to a string.
         # This allows the custom exception to provide a meaningful representation of itself 
         # when converted to a string.

#Overall, this code defines a custom exception class (CustomException) that extends
# the functionality of the built-in Exception class by providing a mechanism to generate 
# and store detailed error messages. The __init__ method initializes the exception
# with an error message, 
# 
# ===>>>Important===>>while the __str__ method ensures that the detailed error message
# is returned when the exception object is converted to a string

#test
# try:
#     h=738/0
# except Exception as e:
#     logging.info("Zero division error Arshad")
#     raise CustomException(e,sys)