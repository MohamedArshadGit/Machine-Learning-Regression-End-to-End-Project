import sys
import os

from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')
    
class DataTransformation:
    def __init__(self):
        self.Data_Transformation_config = DataTransformationConfig() #self.Data_Transformation_config has preprocessor_obj_file_path variable
    
    def get_data_transformer_object(self): #This Function is to convert categorcial into numerical Features,Standard Scaler
        try:
            numerical_columns = [ 'reading_score', 'writing_score']
            categorical_columns = ['gender',
                                   'race_ethnicity',
                                   'parental_level_of_education',
                                   'lunch',
                                   'test_preparation_course']
            
            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]  
            )
            
            cat_pipeline = Pipeline(
                steps= [
                    ("imputer",SimpleImputer(strategy="most_frequent")), # most frequent means mode
                    ("one hot encoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )
            #logging.info('Numerical columns median imputation and Standard scaling completed')
            #logging.info('Categorical columns=> mode imputation and One hot encoding completed')
            logging.info(f'Numerical_Columns:{numerical_columns}')
            logging.info(f'Categorical_Columns:{categorical_columns}')
            
            preprocessor = ColumnTransformer(
                [
                    ('num pipeline',num_pipeline,numerical_columns)
                    ('cat pipeline',cat_pipeline,categorical_columns)
                ]
            )
            
            return preprocessor
            

        except Exception as e :
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            
            train_df =pd.read_csv(train_path)
            test_df =pd.read_csv(test_path)
            
            logging.info('Reading of train and test data completed')
            
            logging.info('Obtaining Preprocessor Object')
            
            preprocessor_obj =self.get_data_transformer_object() #it has all preprocessing techniques
            
            target_column_name = 'math_score'
            
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]
            
            logging.info('Applying Preprocessing Object on training and testing dataframe')
            
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
            
            train_arr =np.c_[input_feature_train_arr,
                             np.array(target_feature_train_df)]
            
            test_arr = np.c_[input_feature_test_arr,
                             np.array(target_feature_test_df)]
            
            logging.info('Saved Preprocessing Object')
            
            return(train_arr,
                   test_arr,
                   self.Data_Transformation_config.preprocessor_obj_file_path) #check what is this line
            
            
            
            
        except:
            pass
        
        
