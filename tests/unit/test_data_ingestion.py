import pytest
from deepClassifier.entity import DataIngestionConfig
from deepClassifier.components import DataIngestion
from pathlib import Path
import os

class Test_DataIngestion_download:
    data_ingestion_config = DataIngestionConfig(
        root_dir= os.path.dirname(os.getcwd())+"/tests/data/", 
        source_URL="https://raw.githubusercontent.com/ArunKumar237/CNN_Image_Classifier/main/tests/data/sample_data.zip", 
        local_data_file= os.path.dirname(os.getcwd())+"/tests/data/sample_data.zip", 
        unzip_dir= os.path.dirname(os.getcwd())+"/tests/data/")

    def test_download(self):
        data_ingestion = DataIngestion(config=self.data_ingestion_config)
        print('=========== started download -------------')
        print(self.data_ingestion_config.root_dir,'\n',
        self.data_ingestion_config.source_URL,'\n',
        self.data_ingestion_config.local_data_file,'\n',
        self.data_ingestion_config.unzip_dir,)
        data_ingestion.download_file()
        print('=========== ended download -------------')
        assert os.path.exists(self.data_ingestion_config.local_data_file)


class Test_DataIngestion_unzip:
    data_ingestion_config = DataIngestionConfig(
        root_dir=os.path.dirname(os.getcwd())+"/tests/data/", 
        source_URL="", 
        local_data_file=os.path.dirname(os.getcwd())+"/tests/data/data.zip", 
        unzip_dir=os.path.dirname(os.getcwd())+"/tests/data/")

    def test_unzip(self):
        data_ingestion = DataIngestion(config=self.data_ingestion_config)
        data_ingestion.unzip_and_clean()
        assert os.path.isdir(Path(os.path.dirname(os.getcwd())+"/tests/data/PetImages"))
        assert os.path.isdir(Path(os.path.dirname(os.getcwd())+"/tests/data/PetImages/Cat"))
        assert os.path.isdir(Path(os.path.dirname(os.getcwd())+"/tests/data/PetImages/Dog"))
