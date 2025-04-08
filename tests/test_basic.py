#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests unitaires de base pour le projet PattesThai.

Note: Ce projet est 100% réel. Toute simulation ou action fictive est strictement interdite.
"""

import unittest
import os

class TestBasicProject(unittest.TestCase):
    """Tests de base pour vérifier l'intégrité du projet."""

    def test_project_structure(self):
        """Vérifie que la structure de base du projet existe."""
        # Vérifie que les répertoires principaux existent
        self.assertTrue(os.path.exists("docs"), "Le répertoire docs n'existe pas")
        self.assertTrue(os.path.exists("scripts"), "Le répertoire scripts n'existe pas")
        self.assertTrue(os.path.exists("tests"), "Le répertoire tests n'existe pas")
    
    def test_documentation_files(self):
        """Vérifie que les fichiers de documentation essentiels existent."""
        self.assertTrue(os.path.exists("docs/index.md"), "Le fichier docs/index.md n'existe pas")
        self.assertTrue(os.path.exists("mkdocs.yml"), "Le fichier mkdocs.yml n'existe pas")
    
    def test_basic_functionality(self):
        """Test simple pour s'assurer que les tests fonctionnent."""
        self.assertEqual(1 + 1, 2, "L'arithmétique de base ne fonctionne pas")


if __name__ == "__main__":
    unittest.main()