# 🏡 ImmoPredict 2025 : L'IA au service de l'immobilier français

![Version](https://img.shields.io/badge/Donn%C3%A9es-DVF%202025%20(S1)-green)
![Tech](https://img.shields.io/badge/Stack-Python%20%7C%20Scikit--Learn%20%7C%20Streamlit-blue)

> **"Peut-on estimer la valeur d'un bien en 1 seconde grâce aux données réelles de l'État ?"** > Ce projet transforme plus de 500 000 transactions du premier semestre 2025 en un outil d'aide à la décision intuitif.

---

## 🎯 Le Problème & La Solution
L'accès aux données immobilières est souvent complexe. **ImmoPredict** démocratise l'information en offrant une interface de prédiction basée sur un modèle de Machine Learning entraîné sur les données officielles (DVF).

## 📊 Insights Clés du Marché
Mon analyse exploratoire a révélé des tendances majeures :
* **Volatilité Urbaine :** Les appartements affichent un prix au m² médian 40% supérieur aux maisons.
* **Moteurs de Prix :** La surface habitable reste le facteur prédictif n°1 (Corrélation de 0.81 avec le nombre de pièces).
* **Zones de Tension :** Paris et la petite couronne dominent largement les valorisations du S1 2025.

## 🧠 Ma Démarche Data
1. **Sourcing & Nettoyage :** Traitement des fichiers DVF 2025 (gestion des types, filtrage des outliers).
2. **Analyse Exploratoire (EDA) :** Visualisation des disparités territoriales et structurelles.
3. **Modélisation :** Algorithme **Random Forest** pour sa robustesse face aux données hétérogènes.
4. **Déploiement :** Web App interactive avec **Streamlit** pour une expérience utilisateur fluide.

# 🏡 ImmoPredict 2025 : L'IA au service de l'immobilier français

![Version](https://img.shields.io/badge/Donn%C3%A9es-DVF%202025%20(S1)-green)
![Tech](https://img.shields.io/badge/Stack-Python%20%7C%20Scikit--Learn%20%7C%20Streamlit-blue)


## 📈 État actuel & Perspectives d'amélioration

Le modèle actuel sert de **"Baseline"** (référence de base). Avec un score de précision initial, il démontre que la surface seule ne suffit pas à capturer la complexité du marché français.

### 🛠️ Ce que je prépare pour la V2 :
Pour faire bondir la précision du modèle, je travaille sur l'intégration des variables suivantes :
* **📍 Géolocalisation par Code Postal :** Intégrer la dimension territoriale pour capturer l'effet "quartier".
* **🏙️ Type de Bien & Étage :** Différencier plus finement les caractéristiques structurelles.
* **📉 Analyse Temporelle :** Étudier l'évolution des prix mois par mois sur l'année 2025.
* **⚡ Optimisation des Hyperparamètres :** Fine-tuning du modèle Random Forest pour réduire l'erreur moyenne (MAE).

> **Note de l'auteur :** Ce projet est en évolution constante. Mon objectif est d'affiner l'IA pour qu'elle reflète au plus près les réalités du terrain immobilier.

## 🚀 Installation & Utilisation
1. **Cloner le projet :**
   ```bash
   git clone [https://github.com/ton-pseudo/MonProjetImmo.git](https://github.com/ton-pseudo/MonProjetImmo.git)