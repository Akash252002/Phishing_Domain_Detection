import os
import sys
from dataclasses import dataclass
# setx PYTHONPATH "%PYTHONPATH%;C:\Users\adars\Downloads\Phishing_Domain_Detection\src\components"
import pandas as pd
from sklearn.model_selection import train_test_split

# from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils import export_collection_as_dataframe


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")

    raw_data_path: str = os.path.join("artifacts", "data.csv")
    
    test_data_path: str = os.path.join("artifacts", "test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        # logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            # code to extract data from mongodb and saving

            # code to extract data from notebooks/data in the current directory 
            df=pd.read_csv(os.path.join('notebooks/data','dataset_full.csv'))
            # logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            # Split the data into train and test sets 
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
# continued m/
            # Save the train set DataFrame to a CSV file
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )

            # Save the test set DataFrame to a CSV file
            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )

            # logging.info(
            #     f"Ingested data from mongodb to {self.ingestion_config.raw_data_path}"
            # )

            # logging.info("Exited initiate_data_ingestion method of DataIngestion class")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            # raise CustomException(e, sys)
            pass

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()