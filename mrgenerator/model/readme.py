class ReadmeModel:
    def __init__(self,
                 nom_serveur: str =None,
                 marque_serveur: str =None,
                 emplacement_serveur: str=None,
                 status_serveur: str=None,
                 markdown_role_principal: str=None,
                 markdown_infogerence: str=None,
                 markdown_mode_operatoire: str=None,
                 markdown_evaluation_todo: str=None
                 ):
        self.nom_serveur = nom_serveur
        self.marque_serveur = marque_serveur
        self.emplacement_serveur = emplacement_serveur
        self.status_serveur = status_serveur
        self.markdown_role_principal = markdown_role_principal
        self.markdown_infogerence = markdown_infogerence
        self.markdown_mode_operatoire = markdown_mode_operatoire
        self.markdown_evaluation_todo = markdown_evaluation_todo


    def to_json(self):
        return {
            'nom_serveur': self.nom_serveur,
            'marque_serveur': self.marque_serveur,
            'emplacement_serveur': self.emplacement_serveur,
            'status_serveur': self.status_serveur,
            'markdown_role_principal': self.markdown_role_principal,
            'markdown_infogerence': self.markdown_infogerence,
            'markdown_mode_operatoire': self.markdown_mode_operatoire,
            'markdown_evaluation_todo': self.markdown_evaluation_todo
        }

    @staticmethod
    def from_json(data: dict):
        return ReadmeModel(
            nom_serveur=data.get("nom_serveur", None),
            marque_serveur=data.get("marque_serveur", None),
            emplacement_serveur=data.get("emplacement_serveur", None),
            status_serveur=data.get("status_serveur", None),
            markdown_role_principal=data.get("markdown_role_principal", None),
            markdown_infogerence=data.get("markdown_infogerence", None),
            markdown_mode_operatoire=data.get("markdown_mode_operatoire", None),
            markdown_evaluation_todo=data.get("markdown_evaluation_todo", None)
        )
