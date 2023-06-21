from cnnDeseaseClassifier.config.configuration import ConfigurationManager
from cnnDeseaseClassifier.components.model_evaluation import Evaluation
from cnnDeseaseClassifier import logger


STAGE_NAME = "Evaluation"


class EvaluationPipeline:
    def __init__(self):
        pass

    def __call__(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
