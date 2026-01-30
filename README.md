# 🏡 ImmoPredict 2025 : L'IA au service de l'immobilier français

![Version](https://img.shields.io/badge/Donn%C3%A9es-DVF%202025%20(S1)-green)
![Tech](https://img.shields.io/badge/Stack-Python%20%7C%20Scikit--Learn%20%7C%20Streamlit-blue)

> **"Peut-on estimer la valeur d'un bien en 1 seconde grâce aux données réelles de l'État ?"** > Ce projet transforme plus de 500 000 transactions du premier semestre 2025 en un outil d'aide à la décision fluide et intuitif.

---

## 🎯 Pourquoi ce projet ?
Accéder à la réalité des prix immobiliers est souvent un parcours du combattant entre estimations gonflées et données complexes. **ImmoPredict** simplifie tout cela. J'ai conçu cette interface pour offrir une prédiction instantanée basée sur les données officielles (DVF), rendant l'information transparente et accessible à tous.

## 📊 Ce que les données nous disent (S1 2025)
Mon analyse exploratoire a révélé des mécaniques de marché fascinantes :
* **Le prix du mètre carré :** Les appartements affichent un prix médian au m² **40% supérieur** aux maisons.
* **Le moteur principal :** La surface habitable reste le facteur n°1, avec une corrélation forte de **0.81** sur le prix final.
* **Tension géographique :** Une concentration extrême des valorisations sur Paris et la petite couronne.

## 🧠 Ma Démarche Data
Pour passer de fichiers bruts à une application fonctionnelle, j'ai suivi une pipeline rigoureuse :
1. **Nettoyage "Real-World" :** Traitement des fichiers DVF (gestion des types, filtrage des valeurs aberrantes).
2. **Exploration (EDA) :** Visualisation des disparités territoriales pour comprendre les biais du marché.
3. **Modélisation :** Utilisation d'un algorithme **Random Forest** pour sa robustesse face à l'hétérogénéité des biens.
4. **Déploiement :** Création d'une Web App avec **Streamlit** pour transformer l'IA en outil concret.

## 📈 État du modèle & Roadmap
Actuellement, le modèle sert de **"Baseline"**. Avec un score initial de 10%, il prouve scientifiquement que la surface seule ne suffit pas : l'immobilier est une affaire de détails.

**Je travaille déjà sur la V2 pour faire bondir la précision :**
* 📍 **Géolocalisation :** Intégrer les codes postaux pour capturer l'effet "quartier".
* 🏙️ **Caractéristiques fines :** Différencier les étages et l'état du bien (neuf/ancien).
* ⚡ **Optimisation :** Fine-tuning des hyperparamètres pour réduire l'erreur moyenne (MAE).

---

## 🚀 Installation & Utilisation

1. **Cloner le projet :**
   ```bash
   git clone [https://github.com/ton-pseudo/ImmoPredict2025.git](https://github.com/ton-pseudo/ImmoPredict2025.git)