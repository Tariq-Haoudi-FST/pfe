import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
import base64


# Fonction pour charger le modèle et les objets nécessaires
def load_model_and_objects():
    # Charger le modèle
    model = load_model('my_model.h5')

    # Charger l'encoder
    with open('encoder.pkl', 'rb') as f:
        encoder = pickle.load(f)

    # Charger le tfidf_vectorizer
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        tfidf_vectorizer = pickle.load(f)

    return model, encoder, tfidf_vectorizer


# Chargement des données et du modèle
model, encoder, tfidf_vectorizer = load_model_and_objects()


# Fonction pour charger l'image en base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string


# Charger le logo en base64
logo_base64 = get_base64_image('logo.jpg')

# Ajout de styles CSS
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: #f0f2f6;
    }}
    .sidebar .sidebar-content {{
        background: #004a99;
    }}
    .stButton>button {{
        color: white;
        background: #007bff;
    }}
    .stTextInput>div>div>input {{
        color: #007bff;
    }}
    .logo {{
        display: flex;
        align-items: center;
    }}
    .logo img {{
        width: 50px;
        height: 50px;
        margin-right: 15px;
    }}
    .logo h1 {{
        color: #007bff;
        font-size: 24px;
    }}
    .prediction-card {{
        background: white;
        padding: 20px;
        margin: 20px 0;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        color: #333;
    }}
    .prediction-card h2 {{
        color: #007bff;
        margin-bottom: 15px;
    }}
    .prediction-card p {{
        font-size: 20px;
        margin: 0;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Ajout du logo et du titre
st.markdown(
    f"""
    <div class="logo">
        <img src="data:image/jpg;base64,{logo_base64}" alt="Logo">
        <h1>Prédiction du nombre de vues et d'utilisateurs d'une annonce</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialiser l'état des entrées si elles ne sont pas encore définies
if 'titre_input' not in st.session_state:
    st.session_state['titre_input'] = ""
if 'type_news_input' not in st.session_state:
    st.session_state['type_news_input'] = ""

# Interface utilisateur avec Streamlit
titre_input = st.text_input("Titre de l'annonce", value=st.session_state['titre_input'])
type_news_input = st.text_input("Type de l'annonce", value=st.session_state['type_news_input'])

if st.button("Prédire"):
    # Sauvegarder les entrées dans l'état de session
    st.session_state['titre_input'] = titre_input
    st.session_state['type_news_input'] = type_news_input

    # Faire la prédiction
    titre_tfidf_input = tfidf_vectorizer.transform([titre_input]).toarray()
    type_news_encoded_input = encoder.transform([[type_news_input]]).toarray()
    X_input = np.concatenate((titre_tfidf_input, type_news_encoded_input), axis=1)
    prediction = model.predict(X_input)

    st.markdown(
        f"""
        <div class="prediction-card">
            <h2>Résultats de la prédiction</h2>
            <p>Prédiction du nombre de vues : {prediction[0][0]:.0f} Vues</p>
            <p>Prédiction du nombre d'utilisateurs : {prediction[0][1]:.0f} Utilisateurs</p>
        </div>
        """,
        unsafe_allow_html=True
    )
 # streamlit run app.py
 #ngrok http 8501

