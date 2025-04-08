# PattesThai

![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-En%20d%C3%A9veloppement-orange.svg)
![Workflow](https://github.com/casius999/PattesThai/actions/workflows/main.yml/badge.svg)
![Documentation](https://github.com/casius999/PattesThai/actions/workflows/deploy-docs.yml/badge.svg)

## Projet 100% Réel et Transparent

PattesThai est un projet **100% réel** visant à créer un refuge temporaire pour chiens et chats errants en danger en Thaïlande, débutant à Khon Kaen, avec une extension prévue à Rayong et potentiellement dans d'autres villes grâce à la mobilisation de bénévoles.

> **IMPORTANT** : Toute simulation, contenu fictif ou action factice est strictement interdite à tous les niveaux du projet et continuellement évitée.

## Missions

- Sauvetage et soins des animaux errants en danger
- Hébergement temporaire et réhabilitation
- Recherche de familles d'accueil
- Sensibilisation sur la cause animale en Thaïlande
- Formation de bénévoles locaux

## Financement Participatif

Le projet est financé par une campagne de financement participatif via GoFundMe (et potentiellement Leetchi) pour collecter les fonds nécessaires aux soins, équipements et à la logistique du projet.

## Documentation

La documentation complète du projet est disponible sur [GitHub Pages](https://casius999.github.io/PattesThai/).

## Stratégie de Visibilité

Une part importante de notre stratégie est la diffusion virale sur TikTok et autres réseaux sociaux pour maximiser la visibilité du projet et attirer des donateurs et bénévoles.

## Structure du Dépôt

- `/.github/workflows/` - Configuration CI/CD
- `/docs/` - Documentation du projet
- `/scripts/` - Scripts d'automatisation (collecte de données, génération de rapports, etc.)
- `/tests/` - Tests unitaires et d'intégration

## Installation et Configuration

### Prérequis
- Python 3.11 ou supérieur
- Git
- Accès à GitHub Actions

### Installation locale
1. Clonez le dépôt
   ```bash
   git clone https://github.com/Casius999/PattesThai.git
   cd PattesThai
   ```

2. Créez un environnement virtuel
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows: venv\Scripts\activate
   ```

3. Installez les dépendances
   ```bash
   pip install -r requirements.txt
   ```

### Configuration des clés API
Pour utiliser toutes les fonctionnalités du projet, vous devrez configurer les secrets suivants dans votre dépôt GitHub :

1. `GOFUNDME_API_KEY` - Clé d'API pour accéder aux données de la campagne GoFundMe
2. `OPENAI_API_KEY` - Clé d'API pour générer du contenu TikTok avec l'IA

Pour configurer ces secrets, allez dans `Settings > Secrets and variables > Actions` de votre dépôt GitHub.

## Exécution des Workflows

Les workflows sont configurés pour s'exécuter automatiquement sur certains événements, mais vous pouvez aussi les déclencher manuellement :

1. Allez dans l'onglet "Actions" du dépôt
2. Sélectionnez le workflow que vous souhaitez exécuter
3. Cliquez sur "Run workflow" et sélectionnez la branche

## Contribuer

Nous accueillons toute aide sur ce projet! Voici comment vous pouvez contribuer:

1. Forker le dépôt
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/amazing-feature`)
3. Committer vos changements (`git commit -m 'Add some amazing feature'`)
4. Pousser vers la branche (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

Plus de détails dans [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

Le code source de ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Contact

Pour toute question ou suggestion, veuillez ouvrir une issue sur ce dépôt GitHub.

---

&copy; 2025 PattesThai. Tous droits réservés.