#Data Ingestion-Y we need?A data will be scraped and stored in diffrent different places 
#We will connect and use that data for our project purposes

#a data ingestion module serves as a foundational component
# in data pipelines, enabling organizations
# =>to efficiently "collect",
# =>"process",
# =>"utilize data"
# for various "analytical", 
# "operational" purposes

import os
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass #The dataclasses module in Python provides a decorator from 3.7 python
# and functions for automatically generates special methods
# such as __init__() or constructor method of a classor instance method or initializer method 
# and __repr__() or __eq__()to user-defined classes, making it easier to create classes that primarily store data.

@dataclass
class DataingestionConfig(): #any input i require i ll put it here in dataingestion config
    train_data_path: str = os.path.join('artifacts','train.csv') #we are using dataclasses module,so little bit different we dont need to initialize the __init_
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','raw_data.csv')
    #Note:@dataclass does not handle not None Part =>>VERY VERY IMPORTANT
    #IF WE ARE ONLY DEFINING VARIABLES INSIDE THE CLASS =>USE DATACLASSES MODULE
    #If we have some other functions inside the class go with constructor method/init method/instance method/initializer method

#WITHOUT USING DATACLASS THE NORMALCONVENTION CLASS DEFINING
class DataingesttionConfig_():
    def __init__(self,train_data_path=None,test_data_path=None,raw_data_path=None):
        if train_data_path is not None: #None means empty or absence of value ,"not None"=>means not empty or not null
            self.train_data_path=train_data_path
        else:
            self.train_data_path=os.path.join('artifacts','train.csv')
        if test_data_path is not None:
            self.test_data_path=test_data_path
        else:
            self.test_data_path=os.path.join('artifacts','test.csv')
        if raw_data_path is not None:
            self.raw_data_path=raw_data_path
        else:
            self.raw_data_path=os.path.join('artifacts','raw_data.csv')

class Dataingestion():
    def __init__(self):
        self.ingestion_config=DataingestionConfig() #self.ingestion_config holds all three paths: train_data_path, test_data_path, and raw_data_path.

