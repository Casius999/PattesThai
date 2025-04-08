#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour récupérer les données de financement depuis GoFundMe et mettre à jour la documentation.

Note: Ce projet est 100% réel. Toute simulation ou action fictive est strictement interdite.
"""

import os
import json
import sys
from datetime import datetime

# Configuration
OUTPUT_DIR = 'docs/campaign/data'

def get_fundraising_data():
    """
    Récupère les données de financement de la campagne GoFundMe.
    
    Dans cette version initiale, utilise des données de démonstration.
    À remplacer par l'intégration API réelle une fois la campagne lancée.
    """
    print("Récupération des données de financement...")
    
    # Données de démonstration
    return {
        "campaign_title": "PattesThai - Refuge pour animaux en Thaïlande",
        "goal_amount": 10000,
        "current_amount": 0,
        "donor_count": 0,
        "last_updated": datetime.now().isoformat(),
        "status": "En préparation"
    }

def update_documentation(data):
    """
    Met à jour la documentation avec les données de financement.
    """
    print("Mise à jour de la documentation...")
    
    # S'assurer que le répertoire existe
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Enregistrer les données brutes au format JSON
    with open(f"{OUTPUT_DIR}/funding_data.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Créer une page Markdown pour la visualisation
    markdown = f"""# État du Financement

*Dernière mise à jour: {datetime.now().strftime('%d/%m/%Y %H:%M')}*

## Campagne GoFundMe: {data['campaign_title']}

- **Objectif**: {data['goal_amount']} €
- **Montant actuel**: {data['current_amount']} €
- **Nombre de donateurs**: {data['donor_count']}
- **Statut**: {data['status']}

## Progression

![Progression](https://progress-bar.dev/{int((data['current_amount'] / data['goal_amount']) * 100) if data['goal_amount'] > 0 else 0})

## Utilisation des Fonds

Les fonds collectés seront utilisés selon la répartition suivante:

- Soins vétérinaires: 40%
- Nourriture et fournitures: 30%
- Logistique et transport: 20% 
- Administration et communication: 10%

Des rapports détaillés sur l'utilisation des fonds seront publiés régulièrement.
"""
    
    with open(f"{OUTPUT_DIR}/funding_status.md", 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"Documentation mise à jour avec succès - {datetime.now().strftime('%d/%m/%Y %H:%M')}")

def main():
    try:
        data = get_fundraising_data()
        update_documentation(data)
        return 0
    except Exception as e:
        print(f"Erreur: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())