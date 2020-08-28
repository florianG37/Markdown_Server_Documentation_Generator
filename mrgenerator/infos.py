from mrgenerator.model.readme import ReadmeModel
from mrgenerator.utils import get_readme_json, create_json


def get_info_readme():
    data = get_readme_json()
    return ReadmeModel.from_json(data)


def create_info_json():
    readme = ReadmeModel(
        nom_serveur=" ",
        marque_serveur=" ",
        emplacement_serveur=" ",
        status_serveur=" ",
        markdown_role_principal="## Role 1 \n bla bla 2 \n ## Role 2 \n blabla",
        markdown_infogerence=" ",
        markdown_mode_operatoire=" ",
        markdown_evaluation_todo=" "
        )
    create_json(readme.to_json())

