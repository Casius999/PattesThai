#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests unitaires pour le module de financement participatif.

Note: Ce projet est 100% réel. Toute simulation ou action fictive est strictement interdite.
"""

import unittest
import os
import sys
import json
from unittest.mock import patch, MagicMock
from datetime import datetime

# Ajout du répertoire parent au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import du module à tester
try:
    from scripts.fundraising.update_fundraising_data import fetch_gofundme_data, update_funding_documentation
except ImportError:
    # Si le module n'existe pas encore, ce test sera skippé
    pass

class TestFundraising(unittest.TestCase):
    """Tests pour les fonctionnalités liées au financement participatif."""

    def setUp(self):
        """Préparation des tests."""
        # Données de test
        self.test_data = {
            "campaign_title": "PattesThai Test Campaign",
            "goal_amount": 10000,
            "current_amount": 2500,
            "donor_count": 15,
            "last_updated": datetime.now().isoformat(),
            "status": "Active"
        }
        
        # Création d'un répertoire temporaire pour les tests
        self.test_output_dir = 'test_output'
        os.makedirs(self.test_output_dir, exist_ok=True)

    def tearDown(self):
        """Nettoyage après les tests."""
        # Suppression des fichiers de test
        if os.path.exists(f"{self.test_output_dir}/funding_data.json"):
            os.remove(f"{self.test_output_dir}/funding_data.json")
        if os.path.exists(f"{self.test_output_dir}/funding_status.md"):
            os.remove(f"{self.test_output_dir}/funding_status.md")
        
        # Suppression du répertoire de test
        if os.path.exists(self.test_output_dir):
            os.rmdir(self.test_output_dir)

    @unittest.skipIf('scripts.fundraising.update_fundraising_data' not in sys.modules, 
                    "Module de financement non disponible")
    def test_fetch_gofundme_data_without_api_key(self):
        """Test de la récupération des données sans clé API."""
        with patch.dict('os.environ', {'GOFUNDME_API_KEY': ''}):
            data = fetch_gofundme_data()
            self.assertEqual(data['status'], 'En attente de lancement')
            self.assertEqual(data['current_amount'], 0)

    @unittest.skipIf('scripts.fundraising.update_fundraising_data' not in sys.modules, 
                    "Module de financement non disponible")
    @patch('requests.get')
    def test_fetch_gofundme_data_with_api_key(self, mock_get):
        """Test de la récupération des données avec une clé API."""
        # Configuration du mock
        mock_response = MagicMock()
        mock_response.json.return_value = self.test_data
        mock_get.return_value = mock_response
        
        with patch.dict('os.environ', {'GOFUNDME_API_KEY': 'test_key', 
                                     'GOFUNDME_CAMPAIGN_ID': 'test_id'}):
            data = fetch_gofundme_data()
            self.assertEqual(data, self.test_data)

    @unittest.skipIf('scripts.fundraising.update_fundraising_data' not in sys.modules, 
                    "Module de financement non disponible")
    def test_update_funding_documentation(self):
        """Test de la mise à jour de la documentation."""
        # Redirection de la sortie vers le répertoire de test
        with patch('scripts.fundraising.update_fundraising_data.OUTPUT_DIR', self.test_output_dir):
            update_funding_documentation(self.test_data)
            
            # Vérification que les fichiers ont été créés
            self.assertTrue(os.path.exists(f"{self.test_output_dir}/funding_data.json"))
            self.assertTrue(os.path.exists(f"{self.test_output_dir}/funding_status.md"))
            
            # Vérification du contenu du fichier JSON
            with open(f"{self.test_output_dir}/funding_data.json", 'r', encoding='utf-8') as f:
                saved_data = json.load(f)
                self.assertEqual(saved_data, self.test_data)
            
            # Vérification que le markdown contient les informations essentielles
            with open(f"{self.test_output_dir}/funding_status.md", 'r', encoding='utf-8') as f:
                markdown_content = f.read()
                self.assertIn(self.test_data['campaign_title'], markdown_content)
                self.assertIn(str(self.test_data['goal_amount']), markdown_content)
                self.assertIn(str(self.test_data['current_amount']), markdown_content)

if __name__ == '__main__':
    unittest.main()