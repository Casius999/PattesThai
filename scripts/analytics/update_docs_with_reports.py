#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour mettre à jour la documentation avec les rapports générés.

Note: Ce projet est 100% réel. Toute simulation ou action fictive est strictement interdite.
"""

import os
import shutil
from datetime import datetime

# Configuration
REPORTS_DIR = 'reports'
DOCS_REPORTS_DIR = 'docs/reports'

def update_documentation_with_reports():
    """
    Copie les rapports générés dans le répertoire de documentation
    et met à jour l'index des rapports.
    """
    # Création du répertoire de rapports dans la documentation s'il n'existe pas
    os.makedirs(DOCS_REPORTS_DIR, exist_ok=True)
    
    # Vérification que les rapports existent
    if not os.path.exists(REPORTS_DIR):
        print(f"Le répertoire {REPORTS_DIR} n'existe pas. Aucun rapport à copier.")
        return
    
    # Copie des rapports
    files_copied = []
    for filename in os.listdir(REPORTS_DIR):
        if filename.endswith('.md') or filename.endswith('.png'):
            source = os.path.join(REPORTS_DIR, filename)
            destination = os.path.join(DOCS_REPORTS_DIR, filename)
            shutil.copy2(source, destination)
            files_copied.append(filename)
    
    if not files_copied:
        print("Aucun rapport trouvé à copier.")
        return
    
    # Mise à jour de l'index des rapports
    index_content = f"""# Rapports du Projet PattesThai

*Dernière mise à jour: {datetime.now().strftime('%d/%m/%Y %H:%M')}*

Cette section contient les rapports générés automatiquement concernant le projet PattesThai.

## Rapports Disponibles

"""
    
    # Liste des rapports par catégorie
    funding_reports = [f for f in files_copied if 'funding' in f.lower() and f.endswith('.md')]
    social_reports = [f for f in files_copied if 'social' in f.lower() and f.endswith('.md')]
    other_reports = [f for f in files_copied if f.endswith('.md') and f not in funding_reports and f not in social_reports]
    
    # Ajout des rapports de financement
    if funding_reports:
        index_content += "### Rapports de Financement\n\n"
        for report in funding_reports:
            report_name = report.replace('_', ' ').replace('.md', '').title()
            index_content += f"- [{report_name}](./{report})\n"
        index_content += "\n"
    
    # Ajout des rapports de réseaux sociaux
    if social_reports:
        index_content += "### Rapports des Réseaux Sociaux\n\n"
        for report in social_reports:
            report_name = report.replace('_', ' ').replace('.md', '').title()
            index_content += f"- [{report_name}](./{report})\n"
        index_content += "\n"
    
    # Ajout des autres rapports
    if other_reports:
        index_content += "### Autres Rapports\n\n"
        for report in other_reports:
            report_name = report.replace('_', ' ').replace('.md', '').title()
            index_content += f"- [{report_name}](./{report})\n"
        index_content += "\n"
    
    # Informations sur l'automatisation
    index_content += """## À Propos des Rapports

Tous ces rapports sont générés automatiquement par notre système d'intégration continue. Ils sont mis à jour quotidiennement pour refléter l'état actuel du projet.

Pour toute question ou suggestion concernant ces rapports, veuillez ouvrir une issue sur notre [dépôt GitHub](https://github.com/Casius999/PattesThai).
"""
    
    # Écriture du fichier d'index
    with open(os.path.join(DOCS_REPORTS_DIR, 'index.md'), 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"Documentation mise à jour avec {len(files_copied)} rapports.")

def main():
    print("Mise à jour de la documentation avec les rapports...")
    update_documentation_with_reports()
    print("Terminé!")

if __name__ == "__main__":
    main()