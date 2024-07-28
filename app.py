from src.mlproject.logger import logging
import sys
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise CustomException(e, sys)