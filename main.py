from cnnDeseaseClassifier import logger
from cnnDeseaseClassifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from cnnDeseaseClassifier.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)

from cnnDeseaseClassifier.pipeline.stage_03_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started >>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion()
    logger.info(f">>>>> Stage {STAGE_NAME} completed! >>>>>>> \n\nx===========x")
except Exception as e:
    raise e


STAGE_NAME = "Prepare base Model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
