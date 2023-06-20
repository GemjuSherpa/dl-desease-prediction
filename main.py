from cnnDeseaseClassifier import logger
from cnnDeseaseClassifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started >>>>>>")
    obj = DataIngestionTrainingPipeline()
    obj()
    logger.info(f">>>>> Stage {STAGE_NAME} completed! >>>>>>> \n\nx===========x")
except Exception as e:
    raise e
