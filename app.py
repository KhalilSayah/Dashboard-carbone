import streamlit as st
import csv
import os

# Appliquer du CSS personnalisé pour améliorer le style
st.markdown("""
    <style>
    .title { text-align: center; font-size: 36px; color: #2E8B57; }
    .header { font-size: 24px; font-weight: bold; color: #4169E1; text-align: center; }
    .stButton>button { width: 100%; border-radius: 10px; font-size: 18px; }
    .progress-bar { height: 10px; border-radius: 10px; background: linear-gradient(to right, #4CAF50, #8BC34A); }
    </style>
""", unsafe_allow_html=True)

# File to store responses
CSV_FILE = "data.csv"

# Function to save data to CSV
def save_data():
    """Saves user responses to a CSV file."""
    data = [
        st.session_state.get("name", ""),
        st.session_state.get("email", ""),
        st.session_state.get("campus", ""),
        st.session_state.get("mode_transport", ""),
        st.session_state.get("type_carburant", ""),
        st.session_state.get("freq_voyage", ""),
        st.session_state.get("distance_quotidienne", ""),
        st.session_state.get("type_logement", ""),
        st.session_state.get("superficie", ""),
        st.session_state.get("conso_energie", ""),
        st.session_state.get("nb_personnes", ""),
        st.session_state.get("source_energie", ""),
        st.session_state.get("type_regime", ""),
        st.session_state.get("origine_aliments", ""),
        st.session_state.get("consommation_viande", ""),
        st.session_state.get("produits_recond", ""),
        st.session_state.get("type_produit", ""),
        st.session_state.get("conso_numerique", ""),
        st.session_state.get("nb_appareils", ""),
        st.session_state.get("achats_vetements", ""),
        st.session_state.get("temps_streaming", ""),
        st.session_state.get("renouvellement_appareils", ""),
        st.session_state.get("temps_ia", ""),
    ]

    # Check if file exists
    file_exists = os.path.isfile(CSV_FILE)

    # Open CSV file and write data
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write header if file is new
        if not file_exists:
            writer.writerow([
                "Campus", "Mode Transport", "Type Carburant", "Fréquence Voyages", "Distance Quotidienne",
                "Type Logement", "Superficie", "Consommation Énergie", "Nb Personnes", "Source Énergie",
                "Type Régime", "Origine Aliments", "Consommation Viande", 
                "Produits Reconditionnés", "Type Produit", "Conso Numérique", "Nb Appareils", 
                "Achats Vêtements", "Temps Streaming", "Renouvellement Appareils", "Temps IA"
            ])
        
        writer.writerow(data)

    st.success("✅ Données enregistrées avec succès !")

def main():
    st.markdown('<h1 class="title">🌱 Formulaire de calcul d\'empreinte carbone</h1>', unsafe_allow_html=True)

    if 'page' not in st.session_state:
        st.session_state.page = 0

    def change_page(delta):
        st.session_state.page += delta

    pages = ["Informations générales", "🚆 Transports", "🏠 Logement", "🥗 Alimentation", "💻 Numérique & Consommation", "✅ Résumé"]
    
    st.markdown(f'<div class="header">{pages[st.session_state.page]}</div>', unsafe_allow_html=True)

    # Barre de progression
    st.progress((st.session_state.page + 1) / len(pages))

    with st.container():
        if st.session_state.page == 0:
            st.session_state.name = st.text_input("👤 Nom")
            st.session_state.email = st.text_input("📧 Email")
            st.session_state.campus = st.selectbox("📍 Campus", ["Lyon", "Paris", "Toulouse"])
        
        elif st.session_state.page == 1:
            st.session_state.mode_transport = st.selectbox("🚗 Mode de transport principal", ["Voiture", "Transport en commun", "Moto", "Vélo", "Marche"])
            if st.session_state.mode_transport == "Voiture":
                st.session_state.type_carburant = st.selectbox("⛽ Type de carburant", ["Essence", "Diesel", "Électrique", "Hybride"])
            st.session_state.freq_voyage = st.selectbox("✈️ Fréquence des voyages longue distance", ["Rarement", "1-2 fois/an", "3-5 fois/an", "Plus de 5 fois/an"])
            st.session_state.distance_quotidienne = st.number_input("📏 Distance quotidienne parcourue (km)", min_value=0.0, step=0.1)

        elif st.session_state.page == 2:
            st.session_state.type_logement = st.selectbox("🏡 Type de logement", ["Appartement", "Maison", "Colocation"])
            st.session_state.superficie = st.number_input("📐 Superficie (m²)", min_value=0.0, step=1.0)
            st.session_state.conso_energie = st.number_input("⚡ Consommation énergétique mensuelle (kWh)", min_value=0.0, step=1.0)
            st.session_state.nb_personnes = st.number_input("👨‍👩‍👦‍👦 Nombre de personnes dans le foyer", min_value=1, step=1)
            st.session_state.source_energie = st.selectbox("🔋 Source d’énergie", ["Gaz", "Électricité", "Renouvelable", "Mixte"])

        elif st.session_state.page == 3:
            st.session_state.type_regime = st.selectbox("🍽️ Type de régime alimentaire", ["Végétarien", "Vegan", "Omnivore", "Flexitarien"])
            st.session_state.origine_aliments = st.selectbox("🌍 Origine des aliments", ["Local", "Importé", "Bio", "Conventionnel"])
            st.session_state.consommation_viande = st.number_input("🥩 Consommation de viande et produits laitiers (repas/semaine)", min_value=0, step=1)

        elif st.session_state.page == 4:
            st.session_state.produits_recond = st.selectbox("♻️ Utilisation de produits reconditionnés", ["Oui", "Non"])
            st.session_state.type_produit = st.text_input("💻 Type de produit numérique utilisé")
            st.session_state.conso_numerique = st.number_input("⚡ Consommation énergétique numérique (kWh/mois)", min_value=0.0, step=1.0)
            st.session_state.nb_appareils = st.number_input("📱 Nombre d’appareils électroniques", min_value=0, step=1)
            st.session_state.achats_vetements = st.text_input("🛍️ Achats de vêtements (fréquence et provenance)")
            st.session_state.temps_streaming = st.number_input("📺 Temps passé en streaming par jour (heures)", min_value=0.0, step=0.1)
            st.session_state.renouvellement_appareils = st.text_input("🔄 Fréquence de renouvellement des appareils numériques")
            st.session_state.temps_ia = st.number_input("🤖 Temps d'utilisation de l'IA (heures/mois)", min_value=0.0, step=1.0)

        elif st.session_state.page == 5:
            st.success("🎉 Données enregistrées avec succès !")

    # Navigation stylisée
    col1, col2 = st.columns([1,1])
    with col1:
        if st.session_state.page > 0:
            st.button("⬅️ Précédent", on_click=lambda: change_page(-1))
    with col2:
        if st.session_state.page < len(pages) - 1:
            st.button("➡️ Suivant", on_click=lambda: change_page(1))
        else:
            st.button("🚀 Envoyer", on_click=save_data)

if __name__ == "__main__":
    main()
