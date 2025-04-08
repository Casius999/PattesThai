#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour générer des suggestions de contenu TikTok pour le projet PattesThai.

Note: Ce projet est 100% réel. Toute simulation ou action fictive est strictement interdite.
"""

import os
import json
import requests
from datetime import datetime

# Configuration
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OUTPUT_DIR = 'output/social'

def generate_tiktok_ideas():
    """
    Génère des idées de contenu TikTok à l'aide de l'API d'OpenAI.
    À adapter en fonction des besoins spécifiques du projet.
    """
    if not OPENAI_API_KEY or OPENAI_API_KEY == 'placeholder':
        print("Clé API OpenAI non configurée. Utilisation de suggestions par défaut.")
        # Suggestions de contenu par défaut
        ideas = [
            {
                "title": "Un jour au refuge",
                "description": "Vidéo montrant une journée typique au refuge, du nourrissage matinal aux soins vétérinaires.",
                "hashtags": ["#AnimalRescue", "#Thailand", "#DogsOfTikTok", "#CatsOfTikTok", "#PattesThai"],
                "music_suggestion": "Musique apaisante ou joyeuse qui met en valeur le travail quotidien",
                "duration": "15-60 secondes"
            },
            {
                "title": "Avant/Après sauvetage",
                "description": "Montrer la transformation d'un animal depuis son sauvetage jusqu'à sa réhabilitation.",
                "hashtags": ["#BeforeAndAfter", "#RescueDog", "#AnimalTransformation", "#PattesThai"],
                "music_suggestion": "Musique émotionnelle qui accompagne la métamorphose",
                "duration": "15-30 secondes"
            },
            {
                "title": "Rencontrez notre équipe",
                "description": "Présentation des bénévoles et de leur travail au refuge.",
                "hashtags": ["#MeetTheTeam", "#Volunteers", "#AnimalLovers", "#PattesThai"],
                "music_suggestion": "Musique énergique et positive",
                "duration": "30-60 secondes"
            },
            {
                "title": "Appel aux dons",
                "description": "Vidéo montrant comment les dons sont utilisés concrètement pour aider les animaux.",
                "hashtags": ["#Donation", "#HelpAnimals", "#MakeDifference", "#PattesThai"],
                "music_suggestion": "Musique inspirante qui appelle à l'action",
                "duration": "30-60 secondes"
            },
            {
                "title": "Les coulisses vétérinaires",
                "description": "Montrer les soins vétérinaires fournis aux animaux du refuge (en respectant l'éthique et sans images choquantes).",
                "hashtags": ["#VetLife", "#AnimalCare", "#VetTech", "#PattesThai"],
                "music_suggestion": "Musique calme et professionnelle",
                "duration": "15-60 secondes"
            }
        ]
        return ideas
    
    # Si l'API est configurée, utiliser OpenAI pour générer des suggestions
    try:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-4",
            "messages": [
                {
                    "role": "system",
                    "content": "Vous êtes un expert en marketing sur TikTok pour des organisations à but non lucratif dédiées aux animaux."
                },
                {
                    "role": "user",
                    "content": "Générez 5 idées de contenu TikTok pour notre projet PattesThai, un refuge pour chiens et chats errants en Thaïlande. Pour chaque idée, fournissez un titre, une description, des hashtags suggérés, des suggestions musicales et une durée optimale. Concentrez-vous sur du contenu qui peut devenir viral tout en sensibilisant à notre cause et en encourageant les dons. N'oubliez pas que ce projet est 100% réel et que nous mettons l'accent sur la transparence et l'authenticité. Formatez votre réponse en JSON."
                }
            ],
            "temperature": 0.7
        }
        
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        content = response.json()['choices'][0]['message']['content']
        
        # Extraire le JSON de la réponse
        if content.startswith("```json"):
            content = content.split("```json")[1].split("```")[0].strip()
        elif content.startswith("```"):
            content = content.split("```")[1].split("```")[0].strip()
            
        ideas = json.loads(content)
        return ideas
        
    except Exception as e:
        print(f"Erreur lors de la génération d'idées via OpenAI: {e}")
        # Fallback aux suggestions par défaut
        ideas = [
            {
                "title": "Un jour au refuge",
                "description": "Vidéo montrant une journée typique au refuge, du nourrissage matinal aux soins vétérinaires.",
                "hashtags": ["#AnimalRescue", "#Thailand", "#DogsOfTikTok", "#CatsOfTikTok", "#PattesThai"],
                "music_suggestion": "Musique apaisante ou joyeuse qui met en valeur le travail quotidien",
                "duration": "15-60 secondes"
            },
            # ... (autres idées par défaut)
        ]
        return ideas

def save_content_ideas(ideas):
    """
    Sauvegarde les idées de contenu générées dans des fichiers
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Sauvegarde au format JSON
    with open(f"{OUTPUT_DIR}/tiktok_ideas.json", 'w', encoding='utf-8') as f:
        json.dump(ideas, f, ensure_ascii=False, indent=2)
    
    # Création d'un fichier Markdown plus lisible
    markdown_content = f"""# Idées de Contenu TikTok pour PattesThai

*Généré le {datetime.now().strftime('%d/%m/%Y %H:%M')}*

"""
    
    for i, idea in enumerate(ideas, 1):
        markdown_content += f"""## {i}. {idea['title']}

**Description:** {idea['description']}

**Hashtags:** {', '.join(idea.get('hashtags', []))}

**Suggestion musicale:** {idea.get('music_suggestion', 'N/A')}

**Durée optimale:** {idea.get('duration', 'N/A')}

---

"""
    
    with open(f"{OUTPUT_DIR}/tiktok_ideas.md", 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Idées de contenu TikTok sauvegardées dans {OUTPUT_DIR}")

def main():
    print("Génération d'idées de contenu TikTok...")
    ideas = generate_tiktok_ideas()
    print("Sauvegarde des idées de contenu...")
    save_content_ideas(ideas)
    print("Terminé!")

if __name__ == "__main__":
    main()