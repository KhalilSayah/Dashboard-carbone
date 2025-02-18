import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #f4f4f4;
            color: #333;
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 1px solid #ccc;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def save_to_csv(data):
    file_path = "data.csv"
    df = pd.DataFrame([data])
    if not os.path.exists(file_path):
        df.to_csv(file_path, mode='w', index=False, header=True)
    else:
        df.to_csv(file_path, mode='a', index=False, header=False)

def informations_personnelles():
    st.title("📌 Informations personnelles")
    add_custom_css()
    st.session_state.nom_prenom = st.text_input("Votre nom / prénom :")
    st.session_state.campus = st.selectbox("Votre campus :", ["Paris", "Toulouse", "Lyon", "Lille", "Nantes", "Montpellier", "Bordeaux", "Aix-en-provence"])
    if st.button("Suivant ➡️"):
        st.session_state.page = "transport"

def transport():
    st.title("🚗 Transport")
    add_custom_css()
    st.session_state.transport_quotidien = st.selectbox("Quel type de moyen de transport utilisez-vous habituellement ?", ["Voiture", "Bus", "Métro", "Train", "Vélo"])
    if st.session_state.transport_quotidien == "Voiture":
        st.session_state.carburant = st.selectbox("Quel est le carburant de votre moyen de transport ?", ["Diesel / Gazoil", "Essence", "Ethanol", "Hybride"])
    st.session_state.covoiturage = st.radio("Pratiquez-vous le covoiturage ?", ["Oui régulièrement", "De temps en temps", "Rarement", "Jamais"])
    st.session_state.avion = st.selectbox("À quelle fréquence prenez-vous l’avion ?", ["1 à 2 fois par an", "3 à 5 fois par an", "+ de 5 fois par an"])
    st.session_state.distance_ecole = st.number_input("Combien de km séparent votre lieu d’habitation de votre lieu de travail / école :", 0, 100, 5)
    if st.button("⬅️ Précédent"):
        st.session_state.page = "informations_personnelles"
    if st.button("Suivant ➡️"):
        st.session_state.page = "habitudes_de_vie"

def habitudes_de_vie():
    st.title("🛋️ Habitudes de vie")
    add_custom_css()
    st.session_state.repas_viande = st.selectbox("Combien de fois mangez-vous de la viande par semaine", ["Tous les jours", "2 à 3 fois par semaine", "0"])
    st.session_state.appareils = st.selectbox("Combien d'appareils électroniques détenez-vous ?", ["1 (téléphone par exemple)", "2 (tel + ordi)", "3 (tel + ordi + tablette)", "+ de 3"])
    st.session_state.achat_appareils = st.selectbox("Vous achetez vos appareils électroniques :", ["Neufs", "Reconditionnés", "Recyclage des appareils de mes proches"])
    st.session_state.tabac = st.selectbox("Consommez-vous du tabac ?", ["Oui tous les jours", "Seulement en soirée", "Rarement (en période de stress par exemple)", "Jamais"])
    st.session_state.achats_vetements = st.selectbox("À quelle fréquence achetez-vous de nouveaux vêtements / objets ?", ["Toutes les semaines", "Tous les mois", "Tous les 6 mois", "Une à deux fois par an", "Très rarement"])
    if st.button("⬅️ Précédent"):
        st.session_state.page = "transport"
    if st.button("Suivant ➡️"):
        st.session_state.page = "logement"

def logement():
    st.title("🏠 Logement")
    add_custom_css()
    st.session_state.type_logement = st.selectbox("Quel est votre lieu de vie ?", ["Appartement", "Maison", "Studio"])
    st.session_state.localisation = st.selectbox("Où se situe votre lieu de vie ?", ["Hyper centre-ville", "Périphérie du centre-ville", "Campagne"])
    st.session_state.surface_logement = st.number_input("Quelle est la superficie de votre logement ?", 10, 500, 50)
    st.session_state.conso_electricite = st.number_input("Quelle est votre consommation mensuelle d’énergie ? (kWh)", 0, 20000, 3000)
    if st.button("⬅️ Précédent"):
        st.session_state.page = "habitudes_de_vie"
    if st.button("🚀 Calculer mon empreinte carbone"):
        user_data = {
            "Nom / Prénom": st.session_state.nom_prenom,
            "Campus": st.session_state.campus,
            "Transport": st.session_state.transport_quotidien,
            "Carburant": st.session_state.carburant if "carburant" in st.session_state else "N/A",
            "Covoiturage": st.session_state.covoiturage,
            "Avion": st.session_state.avion,
            "Distance école/travail": st.session_state.distance_ecole,
            "Repas viande": st.session_state.repas_viande,
            "Appareils électroniques": st.session_state.appareils,
            "Achat appareils": st.session_state.achat_appareils,
            "Tabac": st.session_state.tabac,
            "Achats vêtements": st.session_state.achats_vetements,
            "Type logement": st.session_state.type_logement,
            "Localisation": st.session_state.localisation,
            "Surface logement": st.session_state.surface_logement,
            "Consommation électricité": st.session_state.conso_electricite,
        }
        save_to_csv(user_data)
        st.success("✅ Données enregistrées avec succès !")

def main():
    st.set_page_config(page_title="Calculateur d'Empreinte Carbone", layout="centered")
    if "page" not in st.session_state:
        st.session_state.page = "informations_personnelles"
    if st.session_state.page == "informations_personnelles":
        informations_personnelles()
    elif st.session_state.page == "transport":
        transport()
    elif st.session_state.page == "habitudes_de_vie":
        habitudes_de_vie()
    elif st.session_state.page == "logement":
        logement()

if __name__ == "__main__":
    main()
