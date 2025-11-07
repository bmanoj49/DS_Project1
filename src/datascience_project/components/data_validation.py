import os
from src.datascience_project import logger
from src.datascience_project.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data=pd.read_csv(self.config.unzip_dir)
            all_cols=list(data.columns)
            all_schema=self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation_status: {validation_status}\n")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation_status: {validation_status}\n")
            return validation_status
        except Exception as e:
            logger.exception(e)
            raise e

