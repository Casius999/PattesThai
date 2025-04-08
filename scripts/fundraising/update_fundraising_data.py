#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour récupérer les données de financement depuis GoFundMe et mettre à jour la documentation.

Note: Ce projet est 100% réel. Toute simulation ou action fictive est strictement interdite.
"""

import os
import json
import requests
from datetime import datetime

# Configuration
GOFUNDME_API_KEY = os.environ.get('GOFUNDME_API_KEY')
GOFUNDME_CAMPAIGN_ID = os.environ.get('GOFUNDME_CAMPAIGN_ID', 'placeholder_id')  # À remplacer par l'ID réel
OUTPUT_DIR = 'docs/campaign/data'

def fetch_gofundme_data():
    """
    Récupère les données de la campagne GoFundMe via leur API.
    Dans une phase initiale où l'API n'est pas encore configurée, génère des données d'exemple.
    """
    if not GOFUNDME_API_KEY or GOFUNDME_API_KEY == 'placeholder':
        print("Clé API GoFundMe non configurée. Utilisation de données d'exemple.")
        # En attendant l'accès à l'API réelle, nous utilisons des données d'exemple
        sample_data = {
            "campaign_title": "PattesThai - Refuge pour animaux en Thaïlande",
            "goal_amount": 10000,
            "current_amount": 0,
            "donor_count": 0,
            "last_updated": datetime.now().isoformat(),
            "status": "En attente de lancement"
        }
        return sample_data
    
    # Code pour l'API réelle (à implémenter une fois l'accès obtenu)
    try:
        url = f"https://api.gofundme.com/campaigns/{GOFUNDME_CAMPAIGN_ID}"
        headers = {"Authorization": f"Bearer {GOFUNDME_API_KEY}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erreur lors de la récupération des données GoFundMe: {e}")
        # Fallback à des données d'exemple
        sample_data = {
            "campaign_title": "PattesThai - Refuge pour animaux en Thaïlande",
            "goal_amount": 10000,
            "current_amount": 0,
            "donor_count": 0,
            "last_updated": datetime.now().isoformat(),
            "status": "Erreur de connexion"
        }
        return sample_data

def update_funding_documentation(data):
    """
    Met à jour la documentation avec les dernières données de financement.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Sauvegarde des données brutes pour référence
    with open(f"{OUTPUT_DIR}/funding_data.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Mise à jour du markdown
    markdown_content = f"""# État du Financement

*Dernière mise à jour: {datetime.now().strftime('%d/%m/%Y %H:%M')}*

## Campagne GoFundMe: {data['campaign_title']}

- **Objectif**: {data['goal_amount']} €
- **Montant actuel**: {data['current_amount']} €
- **Nombre de donateurs**: {data['donor_count']}
- **Status**: {data['status']}

## Progression

![Progression](https://progress-bar.dev/{int((data['current_amount'] / data['goal_amount']) * 100) if data['goal_amount'] > 0 else 0})

## Détails de l'Utilisation des Fonds

Tous les fonds collectés sont utilisés transparemment selon la répartition suivante:

- Soins vétérinaires: 40%
- Nourriture et fournitures: 30%
- Logistique et transport: 20%
- Administration et communication: 10%

Des rapports détaillés sont publiés régulièrement dans la section Rapports.
"""
    
    with open(f"{OUTPUT_DIR}/funding_status.md", 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Documentation mise à jour avec les données de financement du {datetime.now().strftime('%d/%m/%Y %H:%M')}")

def main():
    print("Récupération des données de financement...")
    data = fetch_gofundme_data()
    print("Mise à jour de la documentation...")
    update_funding_documentation(data)
    print("Terminé!")

if __name__ == "__main__":
    main()