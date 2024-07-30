import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
if __name__ == "__main__":
    logging.info("The execution has started.")
    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_tranformation = DataTransformation()
        train_arr, test_arr,_ = data_tranformation.initiate_data_transformation(train_data_path, test_data_path)
        print(train_arr, test_arr)
    except Exception as e:
        raise CustomException(e, sys)