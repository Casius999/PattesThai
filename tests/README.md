# Tests pour PattesThai

Ce répertoire contient les tests unitaires et d'intégration pour le projet PattesThai.

## Structure

- `test_fundraising.py` - Tests pour les fonctionnalités de financement participatif
- `test_social.py` - Tests pour les fonctionnalités de médias sociaux
- `test_analytics.py` - Tests pour les fonctionnalités d'analyse de données

## Exécution des Tests

Pour exécuter les tests, utilisez la commande suivante depuis la racine du projet :

```bash
pytest tests/
```

Pour générer un rapport de couverture :

```bash
coverage run -m pytest tests/
coverage report
```

## Création de Nouveaux Tests

Lors de l'ajout de nouvelles fonctionnalités, assurez-vous de créer les tests correspondants dans ce répertoire.