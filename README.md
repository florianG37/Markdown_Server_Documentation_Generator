# Markdown Generator - Generating Server Documentation

Based on [markdown-readme-generator](https://github.com/pedroermarinho/markdown-readme-generator) project by  Pedro Marinho (GitHub : [@pedroermarinho](https://github.com/pedroermarinho/))

Remastered by Florian GIGOT (Github : [@florianG37](https://github.com/florianG37)).

Copyright © 2020 [Florian GIGOT](https://github.com/florianG37).

This project is [MIT](https://github.com/florianG37/Markdown_Server_Documentation_Generator/blob/master/LICENSE) licensed.

# Notice utilisateur

## Installation

- Installez python 3
- Téléchargez generator.zip
- Lancez setup.bat

## Utilisation

- Lancez generateJSON.bat pour générer le JSON associé au template
- Remplissez le readme.json
- Lancez generateMD.bat
- Le résultat est écrit dans le fichier README.md

## Modification du template

- Model/readme.py :  Déclaration des variables
- templates/default.pmd : Déclaration du template
- infos.py : modifier le json généré par défaut
