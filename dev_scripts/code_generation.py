import os

print("Welcome to code Generation tool 🚀")
var = input("Please enter feature name in lowercase (ex: users, products, items): ")
print("You entered: " + var)
mode = 0o666
parent_directory = os.getcwd()
print(parent_directory)

# root folder creation
root_path = os.path.join(parent_directory, "app/" + var)
os.mkdir(root_path)
print("root folder created: " + root_path)
root_files_names = ["__init__.py", var + "_router.py"]
for root_file_name in root_files_names:
    with open(os.path.join(root_path, root_file_name), 'w') as fp:
        pass
print("root files created")

# sub folders creation

sub_folders = ["data", "dto", "repository", "service"]
sub_files_names = [var + ".py", var + "_dto.py", var + "_repository.py", var + "_service.py"]

for i, sub_folder in enumerate(sub_folders):
    sub_path = os.path.join(root_path, sub_folder)
    os.mkdir(sub_path)
    # Creating a file at specified location
    with open(os.path.join(sub_path, sub_files_names[i]), 'w') as fp:
        pass

print("sub folders created 😀 ")

# writing to data model file:
data_model_file_path = root_path + "/" + sub_folders[0] + "/" + sub_files_names[0]
with open(data_model_file_path, "w") as file1:
    # Writing data to a file
    file1.write("from typing import Optional\nfrom sqlmodel import SQLModel, Field \n\n\n")
    L = [f"class {var.capitalize()}(SQLModel, table=True):\n\t",
         f"__tablename__ = \"{var}\"\n\t"
         "id: Optional[int] = Field(default=None, primary_key=True)\n\t",
         "name: str",
         "\n"]
    file1.writelines(L)

# writing to dto file:
dto_model_file_path = root_path + "/" + sub_folders[1] + "/" + sub_files_names[1]
with open(dto_model_file_path, "w") as file1:
    # Writing data to a file
    file1.write("from sqlmodel import SQLModel\n\n\n")
    L = [f"class {var.capitalize()}DTO(SQLModel):\n\t",
         "name: str\n",
         "\n"]
    file1.writelines(L)

# writing to repository file:
repository_model_file_path = root_path + "/" + sub_folders[2] + "/" + sub_files_names[2]
with open(repository_model_file_path, "w") as file1:
    # Writing data to a file
    file1.write("from fastapi import Depends\n")
    L = [f"from sqlmodel import Session, select\n",
         "from app.common.db.session import get_db\n",
         f"from app.{var}.dto.{var}_dto import {var.capitalize()}DTO\n",
         "from app.common.repo.sql_repo import SQLRepository\n",
         f"from app.{var}.data.{var} import {var.capitalize()}\n\n\n",
         f"class {var.capitalize()}Repository(SQLRepository):\n\n\t",
         "def __init__(self, db: Session = Depends(get_db)):\n\t\t",
         f"super().__init__({var.capitalize()}, db)",
         "\n\n"
         ]
    file1.writelines(L)

    # get entity by id
    get_entity_by_id = [
        f"\tdef get_{var}_by_id(self, {var}_id):\n",
        f"\t\treturn self.get_entity_by_id({var}_id)\n",
        "\n"
    ]
    file1.writelines(get_entity_by_id)

    # create entity
    create_entity = [
        f"\tdef create_{var}(self, {var}_dto: {var.capitalize()}DTO):\n",
        f"\t\t{var} = {var.capitalize()}(name={var}_dto.name)\n",
        f"\t\treturn self.create_entity({var})\n",
        "\n"
    ]
    file1.writelines(create_entity)

    # get all entities
    get_all_entities = [
        f"\tdef get_all_{var}(self):\n",
        f"\t\treturn self.get_all_entities()\n",
        "\n"
    ]
    file1.writelines(get_all_entities)


# writing to service file:
service_file_path = root_path + "/" + sub_folders[3] + "/" + sub_files_names[3]
with open(service_file_path, "w") as file1:
    L = ["from fastapi import Depends, HTTPException\n\n",
         f"from app.{var}.dto.{var}_dto import {var.capitalize()}DTO\n",
         f"from app.{var}.repository.{var}_repository import {var.capitalize()}Repository\n\n\n",
         f"class {var.capitalize()}Service:\n\n\t",
         f"def __init__(self, repo: {var.capitalize()}Repository = Depends({var.capitalize()}Repository)):\n\t\t",
         f"self.repo = repo",
         "\n\n"
         ]
    file1.writelines(L)

    # get entity by id
    get_entity_by_id = [
        f"\tdef get_{var}_by_id(self, {var}_id):\n",
        "\t\ttry:\n",
        f"\t\t\treturn self.repo.get_{var}_by_id({var}_id)\n",
        "\t\texcept:\n",
        f"\t\t\traise HTTPException(404, \"No {var} found\")\n",
        "\n"
    ]
    file1.writelines(get_entity_by_id)

    # create entity
    create_entity = [
        f"\tdef create_{var}(self, {var}_dto: {var.capitalize()}DTO):\n",
        f"\t\treturn self.repo.create_{var}({var}_dto)\n",
        "\n"
    ]
    file1.writelines(create_entity)

    # get all entities
    get_all_entities = [
        f"\tdef get_all_{var}(self):\n",
        "\t\ttry:\n",
        f"\t\t\treturn self.repo.get_all_{var}()\n",
        "\t\texcept:\n",
        f"\t\t\traise HTTPException(404, \"No {var} found\")\n",
        "\n"
    ]
    file1.writelines(get_all_entities)


# writing to router file:
router_file_path = root_path + f"/{var}_router.py"
with open(router_file_path, "w") as file1:
    file1.write("from fastapi import APIRouter, Depends\n")
    L = [
         f"from app.{var}.data.{var} import {var.capitalize()}\n",
         f"from app.{var}.dto.{var}_dto import {var.capitalize()}DTO\n",
         f"from app.{var}.service.{var}_service import {var.capitalize()}Service\n\n",
         "router = APIRouter()\n\n\n",
         ]
    file1.writelines(L)

    # get router by id
    get_entity_by_id = [
        f"@router.get(\"/{var}_id\", response_model={var.capitalize()})\n",
        f"def get_{var}_by_id({var}_id: str, service: {var.capitalize()}Service = Depends({var.capitalize()}Service)):\n",
        f"\treturn service.get_{var}_by_id({var}_id={var}_id)\n",
        "\n\n"
    ]
    file1.writelines(get_entity_by_id)

    # create entity
    create_entity = [
        f"@router.post(\"\", response_model={var.capitalize()})\n",
        f"def create_{var}({var}_dto: {var.capitalize()}DTO, service: {var.capitalize()}Service = Depends({var.capitalize()}Service)):\n",
        f"\treturn service.create_{var}({var}_dto)\n",
        "\n\n"
    ]
    file1.writelines(create_entity)

    # get all entities
    get_all_entities = [
        f"@router.get(\"\", response_model=list[{var.capitalize()}])\n",
        f"def get_all_{var}(service: {var.capitalize()}Service = Depends({var.capitalize()}Service)):\n",
        f"\treturn service.get_all_{var}()\n",
        "\n\n"
    ]
    file1.writelines(get_all_entities)

print("All files and folders are created. Happy coding 😀")