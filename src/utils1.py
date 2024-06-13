import os
import sys
import numpy as np
import pandas as pd
import dill #dill is a powerful tool for serializing and deserializing complex Python objects,
#especially those involving functions, lambdas, and external resources.
# It's particularly useful in scenarios where pickle falls short or encounters limitations.

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dirpath = os.path.dirname(file_path)
        
        os.makedirs(dirpath,exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)