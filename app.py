import streamlit as st
import joblib
import numpy as np
import os

# --- 1. CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="ImmoPredict 2025", 
    page_icon="🏡", 
    layout="centered"
)

# --- 2. STYLE PERSONNALISÉ (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { 
        background-color: #2e7d32; 
        color: white; 
        border-radius: 8px; 
        width: 100%; 
        height: 3em;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
        color: white;
    }
    .result-box {
        padding: 25px; 
        border-radius: 12px; 
        background-color: #e8f5e9; 
        border: 2px solid #2e7d32; 
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CHARGEMENT DU MODÈLE ---
# Chemin vers le modèle sauvegardé par train.py
MODEL_PATH = 'models/immo_model.pkl'

@st.cache_resource
def load_trained_model():
    if os.path.exists(MODEL_PATH):
        try:
            return joblib.load(MODEL_PATH)
        except Exception as e:
            st.error(f"Erreur lors de la lecture du fichier : {e}")
            return None
    return None

model = load_trained_model()

# --- 4. INTERFACE UTILISATEUR ---
st.title("🏡 ImmoPredict : L'IA au service de votre projet")
st.subheader("Estimez la valeur d'un bien basée sur les transactions réelles de 2025.")
st.divider()

if model is None:
    st.warning("⚠️ **Modèle introuvable ou invalide.**")
    st.info("""
    **Pour corriger cela :**
    1. Assurez-vous d'avoir un fichier nommé `train.py` à la racine.
    2. Lancez la commande : `python train.py` dans votre terminal.
    3. Vérifiez que le fichier `models/immo_model.pkl` a bien été créé.
    """)
else:
    # Formulaire de saisie
    col1, col2 = st.columns(2)

    with col1:
        type_bien = st.selectbox("Type de bien", ["Appartement", "Maison"])
        surface = st.number_input("Surface habitable (m²)", min_value=10, max_value=500, value=50)

    with col2:
        pieces = st.slider("Nombre de pièces", 1, 15, 3)

    st.write("") # Espacement

    # --- 5. LOGIQUE DE PRÉDICTION ---
    if st.button("🚀 Estimer le prix de vente"):
        try:
            # Préparation de l'entrée (doit être identique au format d'entraînement)
            # Entrée : [[Surface reelle bati, Nombre pieces principales]]
            entree = np.array([[float(surface), float(pieces)]])
            
            # Calcul de la prédiction
            prediction = model.predict(entree)[0]
            
            # Affichage festif et résultat
            st.balloons()
            st.markdown(f"""
                <div class="result-box">
                    <h2 style="color:#2e7d32; margin:0;">Estimation : {prediction:,.0f} €</h2>
                    <p style="color:#666; margin-top:10px;">
                        Basé sur les dernières tendances du marché (S1 2025)<br>
                        <strong>Type :</strong> {type_bien} | <strong>Surface :</strong> {surface}m² | <strong>Pièces :</strong> {pieces}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Une erreur est survenue lors de la prédiction : {e}")

# --- 6. PIED DE PAGE ---
st.divider()
st.caption("Projet Data Science - Données DVF 2025 - Réalisé par Innocent ALLAMADJI")