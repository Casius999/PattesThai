#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour analyser les données du projet et générer des rapports.

Note: Ce projet est 100% réel. Toute simulation ou action fictive est strictement interdite.
"""

import os
import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
GOFUNDME_API_KEY = os.environ.get('GOFUNDME_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
REPORTS_DIR = 'reports'
DATA_DIR = 'docs/campaign/data'

def load_funding_data():
    """
    Charge les données de financement, soit depuis le fichier JSON existant,
    soit génère des données d'exemple si le fichier n'existe pas encore.
    """
    funding_file = os.path.join(DATA_DIR, 'funding_data.json')
    
    if os.path.exists(funding_file):
        try:
            with open(funding_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erreur lors du chargement des données de financement: {e}")
    
    # Données d'exemple si le fichier n'existe pas
    return {
        "campaign_title": "PattesThai - Refuge pour animaux en Thaïlande",
        "goal_amount": 10000,
        "current_amount": 0,
        "donor_count": 0,
        "last_updated": datetime.now().isoformat(),
        "status": "En attente de lancement"
    }

def generate_funding_report(data):
    """
    Génère un rapport sur l'état du financement.
    """
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    # Création du rapport en Markdown
    report_content = f"""# Rapport de Financement PattesThai

*Généré le {datetime.now().strftime('%d/%m/%Y %H:%M')}*

## État de la Campagne GoFundMe

- **Campagne**: {data['campaign_title']}
- **Objectif**: {data['goal_amount']} €
- **Montant actuel**: {data['current_amount']} €
- **Nombre de donateurs**: {data['donor_count']}
- **Pourcentage atteint**: {(data['current_amount'] / data['goal_amount']) * 100 if data['goal_amount'] > 0 else 0:.2f}%
- **Dernière mise à jour**: {data['last_updated']}
- **Statut**: {data['status']}

## Analyse

- Le financement est actuellement {"en avance", "conforme", "en retard"}[1] par rapport aux objectifs.
- Les principales sources de dons proviennent de {"N/A (données non disponibles)"}
- Recommandations: {"Lancer la campagne dès que possible", "Intensifier la communication sur les réseaux sociaux", "Contacter des influenceurs spécialisés dans la cause animale"}[0 if data['current_amount'] == 0 else 1]

## Prochaines Étapes

1. {"Finaliser la page GoFundMe avec des images et descriptions détaillées", "Remercier personnellement les donateurs importants", "Publier des mises à jour sur l'utilisation des fonds"}[0 if data['current_amount'] == 0 else 2]
2. Préparer du contenu vidéo pour TikTok montrant l'impact des dons
3. Mettre en place un tableau de bord en temps réel pour suivre la progression

"""
    
    with open(f"{REPORTS_DIR}/funding_report.md", 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    # Génération d'un graphique simple (simulation)
    if data['current_amount'] > 0:
        try:
            plt.figure(figsize=(10, 6))
            labels = ['Collecté', 'Restant']
            sizes = [data['current_amount'], max(0, data['goal_amount'] - data['current_amount'])]
            colors = ['#4CAF50', '#F5F5F5']
            
            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            plt.title('Progression de la Campagne de Financement')
            plt.savefig(f"{REPORTS_DIR}/funding_progress.png", dpi=300, bbox_inches='tight')
            plt.close()
        except Exception as e:
            print(f"Erreur lors de la génération du graphique: {e}")
    
    print(f"Rapport de financement généré dans {REPORTS_DIR}/funding_report.md")

def generate_social_media_report():
    """
    Génère un rapport sur la performance des réseaux sociaux.
    À développer avec des données réelles quand disponibles.
    """
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    # Données d'exemple (à remplacer par des données réelles quand disponibles)
    social_data = {
        "tiktok": {
            "followers": 0,
            "views": 0,
            "likes": 0,
            "shares": 0,
            "comments": 0,
            "top_performing_content": []
        }
    }
    
    # Création du rapport en Markdown
    report_content = f"""# Rapport des Réseaux Sociaux PattesThai

*Généré le {datetime.now().strftime('%d/%m/%Y %H:%M')}*

## Performance TikTok

- **Abonnés**: {social_data['tiktok']['followers']}
- **Vues totales**: {social_data['tiktok']['views']}
- **Likes**: {social_data['tiktok']['likes']}
- **Partages**: {social_data['tiktok']['shares']}
- **Commentaires**: {social_data['tiktok']['comments']}

### Contenu le Plus Performant

*La campagne sur TikTok n'a pas encore démarré. Cette section sera mise à jour automatiquement dès que du contenu sera publié.*

## Stratégie Recommandée

1. Publier du contenu montrant les animaux sauvés et leurs histoires
2. Utiliser les hashtags populaires liés aux animaux et à la Thaïlande
3. Collaborer avec des créateurs de contenu animalier
4. Participer aux tendances TikTok en les adaptant à notre cause
5. Publier régulièrement (3-5 fois par semaine) pour maintenir l'engagement

"""
    
    with open(f"{REPORTS_DIR}/social_media_report.md", 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"Rapport des réseaux sociaux généré dans {REPORTS_DIR}/social_media_report.md")

def main():
    print("Génération des rapports analytiques...")
    
    # Création des répertoires nécessaires
    os.makedirs(REPORTS_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # Chargement des données et génération des rapports
    funding_data = load_funding_data()
    generate_funding_report(funding_data)
    generate_social_media_report()
    
    print("Tous les rapports ont été générés avec succès!")

if __name__ == "__main__":
    main()