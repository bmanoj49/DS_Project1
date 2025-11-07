import os
import urllib.request as request
from src.datascience_project import logger
import zipfile
from src.datascience_project.entity.config_entity import (DataIngestionConfig)

##component-Data_ingestion  
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    ##Download the zip file
    def download_file(self):
        # logic to download data from self.config.source_url
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with info: \n{headers}")
        else:
            logger.info(f"File already exists")
    
    ##Unzip the downloaded file
    def extract_zip_file(self):
        # logic to unzip the file to self.config.unzip_dir
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"File extracted to {unzip_path}")
    
