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
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import MinMaxScaler
import ast
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from ast import literal_eval
from datetime import datetime
from PIL import Image
from fuzzywuzzy import fuzz
import nltk
nltk.download('popular')

#Configuration de la page
st.set_page_config(
    page_title="Creus-émoi",
    layout="wide",
    initial_sidebar_state="expanded")

phrase_chargement = [
    "Immersion au coeur de la matrice en cours",
    "Chargement datant de l'âge du Jurassic",
    "En route vers les 88mph, pour un résultat qui décoiffe !",
    "Élaboration de votre Truman Show personnel",
    "Tentative d'éviter l'iceberg droit devant !",
    "Propulsion dans l'hyper espace cinéphile",
    "Auto-destruction de l'écran de chargement en cours...",
    "Saut dans votre rêve partagé imminent",
    "Ouverture d'une brèche dans votre chargement à la façon de Jack !",
    "Je suis un écran, un écran de chargement",
    "Déchiffrement du Da Vinci Code en cours...",
    "Recrutement des nouveaux Avengers en cours ",
    "Concoction de votre potion de métamorphose cinématographique en cours.",
    "Création de la communauté des cinéphiles",
    "Envolé de l'écran de chargement à vélo",
    "Voyage vers l'inconnu et l'au delà cinématographique !",
    "Exposition à la kryptonite en cours",
    "Transformation des Mugwais en Gremlins"
]

# Import dataset
df_ML = pd.read_csv('movie_beforeML.csv')

# Sidebar
st.divider()
st.sidebar.title('Votre système de recommandation')

#Image sidebar projet
image_path = "C:/Users/costi/Documents/Github/Project2/image/Clap.png"
image = Image.open(image_path)
st.sidebar.image(image, use_column_width=True)

# Autres éléments dans la barre latérale
st.sidebar.title("Creus-émoi")

#Options Menu
with st.sidebar:
    selected = option_menu('Menu', ["Mode d'emploi", 'Recommandation',"L'équipe du site"],
    icons=['play-btn','search','info-circle'], menu_icon='intersect', default_index=0)

if selected=="Mode d'emploi":
    st.title("**Le mode d'emploi :**")
    st.subheader("Bienvenue dans notre Système de Recommandation Cinématographique Inédit !")
    st.write("Afin de vous proposer la meilleure expérience possible notre équipe de Data Analyst, a travaillé d'arrache-pied pour vous, et nous sommes fiers de nous proposer notre outil.")
    st.subheader("**Guide des bonnes pratiques :**")
    st.write("Plongez dans l'univers du cinéma avec notre système de recommandation révolutionnaire, où chaque suggestion est soigneusement élaborée par un algorithme secret, gardé jalousement derrière le voile du mystère. Notre mission est de transformer votre expérience cinématographique en une aventure unique, sur mesure pour vous.")
    st.write("**Pourquoi secret ?**")
    st.write("Parce que la magie réside dans l'inattendu. Notre algorithme ne se contente pas de suivre les tendances ou de se conformer aux attentes habituelles. Au contraire, il explore des horizons inexplorés pour vous surprendre avec des recommandations que vous n'auriez jamais imaginées.")
    st.write("**Comment ça marche ?**")
    st.write("Ah, c'est là que réside toute l'excitation ! Nous combinons l'art et la science du cinéma avec un algorithme élaboré qui analyse vos préférences, vos humeurs et même vos curiosités cachées. Les détails spécifiques restent confidentiels, mais soyez assuré, c'est ce mystère qui rend chaque recommandation spéciale.")
    st.write("**Laissez-vous surprendre !**")
    st.write("Préparez-vous à être émerveillé par des découvertes cinématographiques uniques, des chefs-d'œuvre méconnus et des pépites du septième art que notre algorithme a soigneusement sélectionnées pour vous.")
    st.write("**Explorez, Découvrez, Appréciez**")
    st.write("Bienvenue dans une expérience de recommandation de films qui va au-delà des sentiers battus. Attachez-vous, car chaque recommandation promet une évasion cinématographique inoubliable.")
    st.write("**Encore là ?**")
    st.write("Vous avez eu le courage de lire ce mode d'emploi, vous pouvez donc profitez de notre *easter egg* essentiel à votre passion de cinéphile ! Parcourez nos onglets et vous pourrez profitez d'une option parfaite pour voir le meilleur... du pire !!!")

if selected=="Recommandation":
    loading = st.subheader(random.choice(phrase_chargement))

    def get_top_values(column, top_n=None):
        # Utilisation de la fonction explode pour déplier les listes de genres
        exploded_genres = column.explode()

        # Utilisation de Counter pour compter le nombre d'occurrences de chaque genre
        genre_counts = Counter(exploded_genres)

        # Supprimer les occurrences de chaînes de caractères vides
        genre_counts = {key: value for key, value in genre_counts.items() if key and not pd.isna(key)}

        # Tri des genres par ordre décroissant de fréquence
        sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

        # Si top_n est spécifié, limiter aux N premiers genres
        if top_n is not None:
            sorted_genres = sorted_genres[:top_n]

        # Renvoyer une liste des genres les plus représentés sans apostrophes et sans chaînes de caractères vides
        top_genres = [genre for genre, count in sorted_genres if genre]

        return top_genres

    def count_occurrences(column, top_n=None):
        # Utilisation de la fonction explode pour déplier les listes de genres
        exploded_genres = column.explode()

        # Filtrer les éléments de la colonne qui ne sont ni vides ni NaN
        cleaned_genres = [item for item in exploded_genres if item and not pd.isna(item)]

        # Utilisation de Counter pour compter le nombre d'occurrences de chaque genre
        genre_counts = Counter(cleaned_genres)

        # Tri des genres par ordre décroissant de fréquence
        sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

        # Si top_n est spécifié, limiter aux N premiers genres
        if top_n is not None:
            sorted_genres = sorted_genres[:top_n]

        # Créer un dictionnaire contenant les genres et leurs occurrences
        result = {genre: count for genre, count in sorted_genres}

        return result

    def count_occurrences_old(column, top_n=None):
        # Utilisation de la fonction explode pour déplier les listes de genres
        exploded_genres = column.explode()

        # Utilisation de Counter pour compter le nombre d'occurrences de chaque genre
        genre_counts = Counter(exploded_genres)

        # Tri des genres par ordre décroissant de fréquence
        sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

        # Si top_n est spécifié, limiter aux N premiers genres
        if top_n is not None:
            sorted_genres = sorted_genres[:top_n]

        # Affichage du résultat avec un saut de ligne après chaque genre
        for genre, count in sorted_genres:
            print(genre, count)

    def clean_and_count_genres(column, top_n=None):
        # Définir une fonction pour nettoyer chaque élément de la colonne
        def clean_genre(x):
            try:
                # Utiliser literal_eval pour convertir la chaîne en liste
                return literal_eval(x)
            except (ValueError, SyntaxError):
                # En cas d'erreur, renvoyer une liste vide
                return []

        # Remplacer les valeurs NaN par une liste vide
        df_complet[column] = df_complet[column].fillna('').apply(clean_genre)

        # Utilisation de la fonction explode pour déplier les listes de genres
        exploded_genres = df_complet[column].explode()

        # Utilisation de Counter pour compter le nombre d'occurrences de chaque genre
        genre_counts = Counter(exploded_genres)

        # Trie des genres par ordre décroissant de fréquence
        sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

        # Affichage des N premiers genres
        if top_n is not None:
            sorted_genres = sorted_genres[:top_n]

        # Affichage du résultat
        unique_genres = [genre for genre, count in sorted_genres]

    def is_nan_string(s):
        try:
            # Convertir la chaîne en un nombre à virgule flottante
            num = float(s)
            # Vérifier si le nombre est NaN
            return math.isnan(num)
        except ValueError:
            # Si la conversion échoue, la chaîne n'est pas un nombre
            return False

    def get_episodes(index_movie, df_titre):
        # Définir deux phrases
        liste_episodes=[]
        df_aglo = df_titre.copy()[0:0]
        phrase1 = df_reco.loc[index_movie, 'french_title']
        mots_phrase1 = phrase1.lower().split()
        tokens_phrase1 = []
        for words in mots_phrase1:
            if words not in nltk.corpus.stopwords.words("french") and words not in nltk.corpus.stopwords.words("english"):
                tokens_phrase1.append(words)

        for titre in df_titre.iloc[1:]['french_title']:
            phrase2=titre
            mots_phrase2 = phrase2.lower().split()
            tokens_phrase2 = []
            for words in mots_phrase2:
                if words not in nltk.corpus.stopwords.words("french") and words not in nltk.corpus.stopwords.words("english"):
                    tokens_phrase2.append(words)
            pourcentage_mots_communs = fuzz.token_set_ratio(tokens_phrase1, tokens_phrase2)
            if pourcentage_mots_communs>=55:
                print("Pour le film:",titre, "Pourcentage de mots communs :", pourcentage_mots_communs, "donc je pense que c'est une suite")
                df_aglo = pd.concat([df_aglo, df_titre.loc[df_titre['french_title'] == titre]])
                #df_titre.loc[df_titre['french_title']==titre]
        return(df_aglo)

    def flatten_list(lst):
        """Fonction récursive pour aplatir une liste."""
        flattened_lst = []
        for item in lst:
            if isinstance(item, list):
                flattened_lst.extend(flatten_list(item))
            elif isinstance(item, str) and item.startswith('[') and item.endswith(']'):
                # Si l'élément ressemble à une liste mais est une chaîne de caractères,
                # nous le traitons comme une liste en le découpant et en séparant les éléments.
                items_inside = item[1:-1].split(', ')
                flattened_lst.extend(items_inside)
            else:
                flattened_lst.append(item)
        return flattened_lst
    pd.set_option('display.max_columns', None)
    init=False

    # #choix film
    titre = 'Titanic'

    if init == False:
        df_complet= df_ML
        df_complet = df_complet.dropna(subset=['release_date'])
        df_complet = df_complet.reset_index(drop=True)
        df_complet['release_date'] = pd.to_datetime(df_complet['release_date'])
        clean_and_count_genres('production_countries', top_n=100000)
        clean_and_count_genres('production_companies_name', top_n=100000)
        clean_and_count_genres('actors', top_n=100000)
        clean_and_count_genres('actresses', top_n=100000)
        clean_and_count_genres('directors', top_n=100000)
        clean_and_count_genres('composers', top_n=100000)
        clean_and_count_genres('writers', top_n=100000)
        clean_and_count_genres('producers', top_n=100000)
        clean_and_count_genres('other_crew', top_n=100000)
        df_reco = df_complet.copy()
        # index_movie = df_reco.loc[df_reco['french_title']== titre].index[0]
        df_reco["release_year"] = df_reco['release_date'].apply(lambda x: pd.to_datetime(x).year)
        release_years_unique = df_reco['release_year'].astype(str).unique().tolist()
        genres_unique = df_reco['genres'].astype(str).unique().tolist()
        genres_unique = flatten_list(genres_unique)
        genres_unique = [genre.strip("'") for genre in genres_unique]
        genres_unique = list(set(genres_unique))
        genres_unique = [element for element in genres_unique if element != '']
        production_countries_unique = df_reco['production_countries'].astype(str).unique().tolist()
        production_countries_unique = flatten_list(production_countries_unique)
        production_countries_unique = [genre.strip("'") for genre in production_countries_unique]
        production_countries_unique = list(set(production_countries_unique))
        production_countries_unique = [element for element in production_countries_unique if element != '']
        production_companies_name_unique = df_reco['production_companies_name'].astype(str).unique().tolist()
        production_companies_name_unique = flatten_list(production_companies_name_unique)
        production_companies_name_unique = [genre.strip("'") for genre in production_companies_name_unique]
        production_companies_name_unique = list(set(production_companies_name_unique))
        production_companies_name_unique = [element for element in production_companies_name_unique if element != '']
        french_title_unique = df_reco['french_title'].astype(str).unique().tolist()
        actors_unique = df_reco['actors'].astype(str).unique().tolist()
        actors_unique = flatten_list(actors_unique)
        actors_unique = [genre.strip("'") for genre in actors_unique]
        actors_unique = list(set(actors_unique))
        actors_unique = [element for element in actors_unique if element != '']
        actresses_unique = df_reco['actresses'].astype(str).unique().tolist()
        actresses_unique = flatten_list(actresses_unique)
        actresses_unique = [genre.strip("'") for genre in actresses_unique]
        actresses_unique = list(set(actresses_unique))
        actresses_unique = [element for element in actresses_unique if element != '']
        directors_unique = df_reco['directors'].astype(str).unique().tolist()
        directors_unique = flatten_list(directors_unique)
        directors_unique = [genre.strip("'") for genre in directors_unique]
        directors_unique = list(set(directors_unique))
        directors_unique = [element for element in directors_unique if element != '']
        composers_unique = df_reco['composers'].astype(str).unique().tolist()
        composers_unique = flatten_list(composers_unique)
        composers_unique = [genre.strip("'") for genre in composers_unique]
        composers_unique = list(set(composers_unique))
        composers_unique = [element for element in composers_unique if element != '']
        writers_unique = df_reco['writers'].astype(str).unique().tolist()
        writers_unique = flatten_list(composers_unique)
        writers_unique = [genre.strip("'") for genre in composers_unique]
        writers_unique = list(set(composers_unique))
        writers_unique = [element for element in composers_unique if element != '']
        producers_unique = df_reco['producers'].astype(str).unique().tolist()
        producers_unique = flatten_list(producers_unique)
        producers_unique = [genre.strip("'") for genre in producers_unique]
        producers_unique = list(set(producers_unique))
        producers_unique = [element for element in producers_unique if element != '']
        other_crew_unique = df_reco['other_crew'].astype(str).unique().tolist()
        other_crew_unique = flatten_list(other_crew_unique)
        other_crew_unique = [genre.strip("'") for genre in other_crew_unique]
        other_crew_unique = list(set(other_crew_unique))
        other_crew_unique = [element for element in other_crew_unique if element != '']
        tags_actors = list(set(actors_unique + actresses_unique))
        tags_directors = directors_unique
        tags_crew = list(set(composers_unique + writers_unique + producers_unique + other_crew_unique))
        tags_genres = genres_unique
        # all_tags_unique = release_years_unique + genres_unique + production_countries_unique + production_companies_name_unique + actors_unique + actresses_unique + directors_unique + composers_unique + writers_unique + producers_unique + other_crew_unique
        # list_unique = [release_years_unique,genres_unique,production_countries_unique,production_companies_name_unique,french_title_unique,actors_unique,actresses_unique,directors_unique,composers_unique,writers_unique,producers_unique,other_crew_unique]
        init = True

    df_reco = df_complet.copy()
    index_movie = df_reco.loc[df_reco['french_title']== titre].index[0]

    #Conversion release_date
    df_reco["release_year"] = df_reco['release_date'].apply(lambda x: pd.to_datetime(x).year)

    genres_premiere_ligne = eval(df_reco.iloc[index_movie]['genres'])
    #index_movie = df_complet.loc[df_complet['french_title']== titre].index[0]

    #Partie genres
    df_dummies_genres = pd.DataFrame(columns=genres_premiere_ligne)
    for genre in genres_premiere_ligne:
        df_dummies_genres[genre] = df_reco['genres'].apply(lambda x: genre in eval(x)).astype(int)
        #df_dummies_genres[genre]*=200
    df_reco = pd.concat([df_reco, df_dummies_genres], axis=1)

    #Partie production_countries
    production_countries_premiere_ligne = df_reco.iloc[index_movie]['production_countries']
    df_dummies_actors = pd.DataFrame(columns=production_countries_premiere_ligne)
    for actor in production_countries_premiere_ligne:
        df_dummies_actors[actor] = df_reco['production_countries'].apply(lambda x: actor in x).astype(int)
    df_reco = pd.concat([df_reco, df_dummies_actors], axis=1)

    #production_companies_name
    actors_premiere_ligne = df_reco.iloc[index_movie]['production_companies_name']
    df_dummies_actors = pd.DataFrame(columns=actors_premiere_ligne)
    for actor in actors_premiere_ligne:
        df_dummies_actors[actor] = df_reco['production_companies_name'].apply(lambda x: actor in x).astype(int)
    df_reco = pd.concat([df_reco, df_dummies_actors], axis=1)

    #Partie actors
    actors_premiere_ligne = df_reco.iloc[index_movie]['actors']
    df_dummies_actors = pd.DataFrame(columns=actors_premiere_ligne)
    for actor in actors_premiere_ligne:
        df_dummies_actors[actor] = df_reco['actors'].apply(lambda x: actor in x).astype(int)
    df_reco = pd.concat([df_reco, df_dummies_actors], axis=1)

    #Partie actresses
    actress_premiere_ligne = df_reco.iloc[index_movie]['actresses']
    df_dummies_actors = pd.DataFrame(columns=actress_premiere_ligne)
    for actor in actress_premiere_ligne:
        df_dummies_actors[actor] = df_reco['actresses'].apply(lambda x: actor in x).astype(int)
    df_reco = pd.concat([df_reco, df_dummies_actors], axis=1)

    #Partie directors
    directors_premiere_ligne = df_reco.iloc[index_movie]['directors']
    df_dummies_actors = pd.DataFrame(columns=directors_premiere_ligne)
    for actor in directors_premiere_ligne:
        df_dummies_actors[actor] = df_reco['directors'].apply(lambda x: actor in x).astype(int)
    df_reco = pd.concat([df_reco, df_dummies_actors], axis=1)

    #Partie composers
    composer_premiere_ligne = df_reco.iloc[index_movie]['composers']
    df_dummies_actors = pd.DataFrame(columns=composer_premiere_ligne)
    for actor in composer_premiere_ligne:
        df_dummies_actors[actor] = df_reco['composers'].apply(lambda x: actor in x).astype(int)
    df_reco = pd.concat([df_reco, df_dummies_actors], axis=1)

    #Partie writers
    writers_premiere_ligne = df_reco.iloc[index_movie]['writers']
    df_dummies_actors = pd.DataFrame(columns=writers_premiere_ligne)
    for actor in writers_premiere_ligne:
        df_dummies_actors[actor] = df_reco['writers'].apply(lambda x: actor in x).astype(int)
    df_reco = pd.concat([df_reco, df_dummies_actors], axis=1)

    #Partie producers
    producers_premiere_ligne = df_reco.iloc[index_movie]['producers']
    df_dummies_actors = pd.DataFrame(columns=producers_premiere_ligne)
    for actor in producers_premiere_ligne:
        df_dummies_actors[actor] = df_reco['producers'].apply(lambda x: actor in x).astype(int)
    df_reco = pd.concat([df_reco, df_dummies_actors], axis=1)

    #Partie other_crew
    other_crew_premiere_ligne = df_reco.iloc[index_movie]['other_crew']
    df_dummies_actors = pd.DataFrame(columns=other_crew_premiere_ligne)
    for actor in other_crew_premiere_ligne:
        df_dummies_actors[actor] = df_reco['other_crew'].apply(lambda x: actor in x).astype(int)
    df_reco = pd.concat([df_reco, df_dummies_actors], axis=1)
    #Header
    st.title("Votre film :")
    with st.sidebar.form("my_form"):
        # # Filtrer par film. Le point unique permet de retourner une lsite plutôt que d'avoir à saisir du texte.
        selected_film = st.sidebar.multiselect('Sélectionnez votre film', df_ML['french_title'].unique())
        # # Filtrer par film. Le point unique permet de retourner une lsite plutôt que d'avoir à saisir du texte.
        selected_film = st.sidebar.multiselect('Sélection de genres', tags_genres)       
        # # Filtrer par film. Le point unique permet de retourner une lsite plutôt que d'avoir à saisir du texte.
        selected_film = st.sidebar.multiselect("Sélection d'acteurs", tags_actors)
        # # Filtrer par film. Le point unique permet de retourner une lsite plutôt que d'avoir à saisir du texte.
        selected_film = st.sidebar.multiselect("Sélection d'un réalisateur", tags_directors)
        # # Filtrer par film. Le point unique permet de retourner une lsite plutôt que d'avoir à saisir du texte.
        selected_film = st.sidebar.multiselect("Ajout un membre de l'équipe technique ?", tags_crew)
        # Bouton Submit pour appliquer les changements
        submitted = st.form_submit_button("Fais p'ter les popcorns !")

    # Normaliser les caractéristiques
    scaler = StandardScaler()
    X = df_reco.select_dtypes(include='number')
    X_scaled = scaler.fit_transform(X)
    y = df_reco['french_title']

    # Entraîner le modèle KNeighborsClassifier
    model = KNeighborsClassifier(n_neighbors=100, weights='uniform')
    model.fit(X_scaled, y)

    # Créer un DataFrame pour stocker les recommandations et les distances
    distances, recommandation = model.kneighbors([X_scaled[index_movie, :]])

    # Créer un DataFrame pour stocker les recommandations et les distances
    df_reco_with_distance = df_reco.iloc[recommandation[0]].copy()
    df_reco_with_distance['Distance'] = distances[0]
    df_titre = df_reco_with_distance

    df_titre = df_titre.reset_index(drop=True)
    df_target = df_titre.head(1)

    #On cherche les suites
    df_aglo = get_episodes(index_movie,df_titre)
    df_titre = df_titre.drop(df_aglo.index, axis=0)
    df_titre = df_titre.iloc[1:]
    print("Les suites", df_aglo['french_title'])
    #On cherche les films avec les genres les plus proches
    df_titre = df_titre.sort_values(by=genres_premiere_ligne, ascending=False)
    df_aglo = pd.concat([df_aglo, df_titre.head(3)])
    df_titre = df_titre.iloc[3:]
    print("Les genres proches", df_aglo['french_title'])
    popularite_target = float(df_target["popularite_ponderee"])
    original_popularite_target = float(df_target["popularite_ponderee"])
    if popularite_target > 6:
        popularite_target = float(df_target["popularite_ponderee"]-1.5)
    if popularite_target > 6.5:
        popularite_target = float(df_target["popularite_ponderee"]-2)
    if popularite_target > 7:
        popularite_target = float(df_target["popularite_ponderee"]-2.5)
    if popularite_target > 7.5:
        popularite_target = float(df_target["popularite_ponderee"]-3)
    if popularite_target > 8:
        popularite_target = float(df_target["popularite_ponderee"]-3.5)
    if popularite_target > 8.5:
        popularite_target = float(df_target["popularite_ponderee"]-4)
    if popularite_target > 9:
        popularite_target = float(df_target["popularite_ponderee"]-4.5)

    # Filtrer les lignes de df_titre en utilisant la méthode query
    df_titre = df_titre.query("popularite_ponderee > @popularite_target")
    df_titre = df_titre.reset_index(drop=True)

    #On cherche les meilleurs films dans les plus proches
    df_titre = df_titre.sort_values(by=['popularite_ponderee'], ascending=False)
    df_aglo = pd.concat([df_aglo, df_titre.head(2)])
    df_titre = df_titre.iloc[2:]
    print("Les meilleurs films proches",df_aglo['french_title'])
    #On cherche les films avec les acteurs les plus proches
    df_titre =  df_titre.sort_values(by=actors_premiere_ligne + ['Distance'], ascending=[False]*len(actors_premiere_ligne) + [False])
    df_aglo = pd.concat([df_aglo, df_titre.head(2)])
    df_titre = df_titre.iloc[2:]
    print("Les memes acteurs", df_aglo['french_title'])
    #On cherche les films avec les actrices les plus proches, s'il yen a
    if actress_premiere_ligne != '':
        df_titre =  df_titre.sort_values(by=actress_premiere_ligne + ['Distance'], ascending=[False]*len(actress_premiere_ligne) + [False])
        df_aglo = pd.concat([df_aglo, df_titre.head(2)])
        df_titre = df_titre.iloc[2:]
    print("Les memes actrices", df_aglo['french_title'])
    #On cherche les films avec les réalisateurs les plus proches
    df_titre =  df_titre.sort_values(by=directors_premiere_ligne + ['Distance'], ascending=[False]*len(directors_premiere_ligne) + [False])
    df_aglo = pd.concat([df_aglo, df_titre.head(2)])
    df_titre = df_titre.iloc[2:]
    print("Les memes real",df_aglo['french_title'])
    #On cherche les films direct les plus proches
    df_titre = df_titre.sort_values(by=['Distance'], ascending=True)
    df_aglo = pd.concat([df_aglo, df_titre.head(2)])
    df_titre = df_titre.iloc[2:]
    print("Les derniers films plus proches",df_aglo['french_title'])
    df_aglo = df_aglo.reset_index(drop=True)
    # df_aglo
    loading.empty()

    #image du film chosis
    col0, col1= st.columns(2)
    with col0:
        selected_movie = df_ML.query(f"french_title == '{titre}'").iloc[0]
        full_link_0 = "https://image.tmdb.org/t/p/w500" + selected_movie['poster_path']
        st.image(full_link_0,output_format="auto")
    with col1:
        st.subheader(selected_movie['french_title'])
        st.write("**Synopsis :**", selected_movie['overview'])
        st.write("**Genre(s) :**", selected_movie['genres'])
        st.write("**Casting :**", selected_movie['actors'], selected_movie['actresses'])
        st.write("**Réalisateur :**", selected_movie['directors'])
        st.write("**Date de sortie :**", selected_movie['release_date'])
        st.write("**Société(s) de production :**", selected_movie['production_companies_name'])


        
    
    #Calcul dynamiquement le nombre de colonnes
    st.subheader("Nos recommandations :")
    nombre_total_de_colonnes = len(df_aglo)
    # Nombre maximal de colonnes par ligne
    colonnes_par_ligne = 3

    # Boucle pour afficher les images et les titres dans des colonnes
    for i in range(len(df_aglo)):
        # Créer une nouvelle ligne de colonnes après chaque 'colonnes_par_ligne'
        if i % colonnes_par_ligne == 0:
            colonnes = st.columns(colonnes_par_ligne)

        # Calcul de l'index dans la ligne actuelle
        index_dans_la_ligne = i % colonnes_par_ligne

        # Calcul de l'index global
        index = i * colonnes_par_ligne + index_dans_la_ligne

        # Vérifier si l'index est dans la plage du DataFrame
        if index < nombre_total_de_colonnes:
            full_link = "https://image.tmdb.org/t/p/w500" + df_aglo['poster_path'].iloc[index]
            colonnes[index_dans_la_ligne].image(full_link, output_format="auto")
            colonnes[index_dans_la_ligne].write(df_aglo['french_title'].iloc[index])
    

if selected=="L'équipe du site":
    #Header
    st.title("Présentation de l'équipe :")
    col0, col1, col2= st.columns(3)
    with col0:
        st.subheader('Clara')
        st.write("The Scrum Princess")
    with col1:
        st.subheader('Basile')
        st.write("Magician ML developer")
    with col2:
        st.subheader('Costin')
        st.write("Streamlit conqueror")        

with st.sidebar:
    # Bouton avec une icône à partir de Font Awesome
    if st.button(":twisted_rightwards_arrows:") :
        # Afficher la nouvelle page lorsque le bouton est cliqué
        st.write('Nanar')