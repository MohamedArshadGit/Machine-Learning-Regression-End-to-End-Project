# Data Transformation used for converting categorical to numerical and continous values
# to standarization etc

import os
import sys

import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer #responsible for handling missing values ,It do imputation like mean,median,mode etc
from sklearn.pipeline import Pipeline #to combine all imputations in one go
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

@dataclass
class DataTransformation_Config():
    preprocessor_obj_file_path= os.path.join('artifacts','preprocessor.pkl') #we can use without 
    # mentioning data type str also or preprocessor_obj_file_path :str 
    #if not used ,if suppose we need to have a check only str should other data type
    # should not come it will not check if we mention data type like str and other
    # data type has came then it will raise error
    
    #PICKLE FILES CAN BE USED TO SAVE THE RESULTS OF CATEGORICAL ENCODING OR OTHER 
       # DATA PREPROCESSING STEPS
       
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
       
   def initiate_transformation(self,train_path,test_path):
       
       train_df=pd.read_csv(train_path)
       test_df=pd.read_csv(test_path)
       
       logging.info("Read Train and test data completed")
       
       logging.info("Obtaining Preprocessor object")
       
       preprocessor_obj= self.get_data_transformer_object()
       
       target_column_name='math_score'
       numerical_column=['reading_score', 
                           'writing_score']
       
       input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
       target_feature_train_df =train_df[target_column_name]
       
       input_feature_test_df =test_df.drop(columns=[target_column_name],axis=1)
       target_feature_test_df =test_df[target_column_name]
       
       logging.info(
           f"Applying preprocessing object on training dataframe and testing dataframe"
       )
       
       input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
       input_feature_test_arr =preprocessor_obj.transform(input_feature_test_df)
       
       train_arr = np.c_[input_feature_train_arr,
                         np.array(target_feature_train_df)] 
       
       test_arr = np.c_[input_feature_test_arr,
                        np.array(target_feature_test_df)] #np.c_ in inbuilt from numpy that
       #allows to Concatenates the arrays array1 and array2 along their second axis (columns).
       # This means it stacks the arrays horizontally, joining the columns together.