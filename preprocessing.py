import pandas as pd

def clean_dvf_data(filepath):
    print("⏳ Chargement des données")
    
    # ASTUCE EXPERT : Utiliser le séparateur '|' et low_memory=False pour éviter les warnings
    df = pd.read_csv(
        filepath, 
        sep='|', 
        encoding='utf-8', 
        low_memory=False
    )

    # 1. Sélection des colonnes stratégiques
    keep_cols = [
        'Valeur fonciere', 'Code postal', 'Nombre pieces principales', 
        'Surface reelle bati', 'Type local'
    ]
    df = df[keep_cols]

    # 2. Nettoyage des prix (virgules -> points) et conversion en numérique
    df['Valeur fonciere'] = df['Valeur fonciere'].str.replace(',', '.').astype(float)

    # 3. Filtrage : On ne garde que les Maisons et Appartements (on exclut les dépendances/locaux)
    df = df[df['Type local'].isin(['Appartement', 'Maison'])]

    # 4. Suppression des données manquantes sur les colonnes clés
    df = df.dropna(subset=['Valeur fonciere', 'Surface reelle bati'])

    # 5. Suppression des "Outliers" (Valeurs aberrantes) pour ne pas fausser le ML
    # On garde les biens entre 50k€ et 2M€, et moins de 300m²
    df = df[(df['Valeur fonciere'] > 50000) & (df['Valeur fonciere'] < 2000000)]
    df = df[df['Surface reelle bati'] < 300]

    print(f"✅ Nettoyage terminé ! {len(df)} lignes prêtes pour l'analyse.")
    return df

# Test rapide
if __name__ == "__main__":
    path = "data/ValeursFoncieres-2025-S1.txt"
    data = clean_dvf_data(path)
    print(data.head())