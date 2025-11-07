from src.datascience_project.config.configuration import ConfigurationManager
from src.datascience_project.components.data_transformation import DataTransformation
from src.datascience_project import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            if status == "True":
               logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
               config = ConfigurationManager()
               data_transformation_config = config.get_data_transformation_config()
               data_transformation = DataTransformation(config=data_transformation_config)
               data_transformation.train_test_splitting()
            else:
               raise Exception("Your Data scheme is not valid") 

               logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
        except Exception as e:
            logger.exception(e)
            raise e