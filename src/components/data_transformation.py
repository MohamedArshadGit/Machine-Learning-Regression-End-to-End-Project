# Data Transformation used for converting categorical to numerical and continous values
# to standarization etc

import os
import sys

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer #responsible for handling missing values ,It do imputation like mean,median,mode etc
from sklearn.pipeline import Pipeline #to combine all imputations in one go
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

@dataclass
class DataTransformation_Config():
    preprocessor_obj_file_path= os.path.join('artifacts','preprocessor.pkl') 
    
class DataTransformation():
   def __init__(self):
       self.Data_Transformation_config = DataTransformation_Config()
  
   def get_data_transformer_object(self): 
       #this function is responsible to convert categorical into numerical or standard scaler etc
       #NOTES:
       #PICKLE FILES CAN BE USED TO SAVE THE RESULTS OF CATEGORICAL ENCODING OR OTHER 
       # DATA PREPROCESSING STEPS
       
       #Once the categorical data has been transformed into numerical form or standard scaling
       # you can then choose to save the resulting models, transformers, or other objects 
       # to pickle files using Python's pickle module, if needed. This allows you to persist
       # the trained models or preprocessing steps for later use without needing to retrain
       # or recompute them.
       #  WHILE PICKLE FILES CAN BE USED TO SAVE THE RESULTS OF CATEGORICAL ENCODING
       # OR OTHER DATA PREPROCESSING STEPS
       try:
           
            numerical_columns=['math_score',
                           'reading_score', 
                           'writing_score']
            categorical_columns=['gender',
                                'race_ethnicity',
                                'parental_level_of_education',
                                'lunch', 'test_preparation_course']
            
            num_pipeline =Pipeline(
                steps=[
                    ("Imputer",SimpleImputer(strategy='median')), #imputation in ML means filling missing values
                    ('scaler',StandardScaler())
                ]
            )
            
            cat_pipeline =Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")) #most_frequent means mode
                    ('One_hot_encoder',OneHotEncoder()),
                    ('scaler',StandardScaler())
                    
                ]
            )
            logging.info(f'Numerical columns:{numerical_columns}')
            logging.info(f'Categorical columns:{categorical_columns}')
            
            #use columnTransformer to combine all pipelines
            preprocessor =ColumnTransformer(                               
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )
            
            return preprocessor
       except Exception as e:
           raise CustomException(e,sys)

       