
import os 
from pathlib import Path

project_name = "visa_analyzer"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py.py",
    f"{project_name}/components/data_transformation.py.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py/",
    f"{project_name}/constants/__init__.py/",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/expection/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utiles/usable.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"
]

for files in list_of_files:

    filepath = Path(files)

    folder , files = os.path.split(filepath)

    if folder!="":

        os.makedirs(folder,exist_ok=True)
    
    if (not os.path.exists(filepath) or os.path.getsize(filename=filepath)==0):

        with open(filepath, "w") as file:

            print(f"{filepath} created")
    else:
        print(f"{filepath}, alreadt exists")