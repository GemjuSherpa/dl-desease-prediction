from typing import Any
from cnnDeseaseClassifier.config.configuration import ConfigurationManager
from cnnDeseaseClassifier.components.prepare_base_model import PrepareBaseModel
from cnnDeseaseClassifier import logger


STAGE_NAME = " Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def __call__(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
