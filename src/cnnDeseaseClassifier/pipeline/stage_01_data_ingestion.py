from cnnDeseaseClassifier import logger
from cnnDeseaseClassifier.config.configuration import ConfigurationManager
from cnnDeseaseClassifier.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion"


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def __call__(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started >>>>>>")
        obj = DataIngestionTrainingPipeline()
        obj()
        logger.info(f">>>>> Stage {STAGE_NAME} completed! >>>>>>> \n\nx===========x")
    except Exception as e:
        raise e
