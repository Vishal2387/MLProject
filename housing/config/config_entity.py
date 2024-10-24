from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",
                                 ["data_set_download_url","tgz_download_dir","raw+data+dir","ingested_train_dir","ingested_test_dir"])
DataValidationConfig = namedtuple("DataValidation",["schema_file_path"])
DataTransformationConfig = namedtuple("DataTransformationConfig",
                                      ["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_objest_file_path"])
ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])
ModelPusherConfig = namedtuple("ModelPusherConfg",["export_dir_path"])
