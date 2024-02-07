# -*- coding: utf-8 -*-
"""streamlit_projet_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kM2bMbF3MzYhxi7OOjg54-tunYiICBNi
"""

# Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import random
import streamlit as st
from streamlit_option_menu import option_menu

# Import dataset
df_ML = pd.read_csv('movie_beforeML.csv')

#Configuration de la page
st.set_page_config(
    page_title="Projet2xCBC",
    layout="wide",
    initial_sidebar_state="collapsed")

#Options Menu
with st.sidebar:
    selected = option_menu('Projet2xCBC', ["Présentation", 'Recommendation','Le petit +'],
    icons=['play-btn','search','info-circle'], menu_icon='intersect', default_index=0)

if selected=="Présentation":
    #Header
    st.title("Le modele d'emploi :")
    st.subheader("Si vous ne suivez pas ces recommendations, c'est à vos risques et périls !")
    st.write("Salut la compagnie !")
    st.write("Attention à la marche")

if selected=="Recommendation":
    #Header
    st.title('Welcome Bitch ! <3')
    st.subheader('Find your perfect film !')

    st.divider()
    # Création de la sidebar et features
    st.sidebar.title('Votre système de recommandation')

    # # Filtrer par film. Le point unique permet de retourner une lsite plutôt que d'avoir à saisir du texte.
    st.sidebar.write("Veuillez choisir un film :")
    selected_film = st.sidebar.multiselect('Sélectionnez votre film', df_ML['french_title'].unique())

    # # Filtrer par acteur
    st.sidebar.write("Veuillez choisir une actrice/un acteur :")
    selected_actor = st.sidebar.multiselect('Sélectionnez le genre', df_ML['actors'].unique())

    # # Filtrer par réal
    st.sidebar.write("Veuillez choisir une réalisatrice/un réalisateur :")
    selected_director = st.sidebar.multiselect('Sélectionnez une personne', df_ML['directors'].unique())

    # # # Filtrer par compositeur
    # st.sidebar.write("Veuillez choisir une compositrice/un compositeur :")
    # selected_composer = st.sidebar.multiselect('Sélectionnez une compositrice/compositeur', df_ML['composers'].unique())
    # # selected_composer = re.sub(r"[:',-]", " ", selected_composer)

    # # # Filtrer par compagnie
    # st.sidebar.write("Veuillez choisir une compagnie :")
    # selected_composer = st.sidebar.multiselect('Sélectionnez une compositrice/compositeur', df_ML['composer'].unique())
    # # selected_composer = re.sub(r"[:',-]", " ", selected_composer)

    # # # Filtrer par compagnie
    # st.sidebar.write("Veuillez choisir une compagnie :")
    # selected_composer = st.sidebar.multiselect('Sélectionnez une compositrice/compositeur', df_ML['composer'].unique())
    # # selected_composer = re.sub(r"[:',-]", " ", selected_composer)


if selected=="Le grand +":
    #Header
    st.title("Le modele d'defdsvdv :")
    st.subheader("Si vo !")
    st.write("Salut la compagnie !\n qsdsqc à la marche")

# Interface visuel
# Voir live coding Florent sur Streamlit pour arranger le visuel des reco films
