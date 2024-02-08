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
import time
import streamlit as st
from streamlit_option_menu import option_menu

# Import dataset
df_ML = pd.read_csv('movie_beforeML.csv')
    
#Configuration de la page
st.set_page_config(
    page_title="Projet2xCBC",
    layout="wide",
    initial_sidebar_state="collapsed")

citations_films = [
    "Que la Force soit avec toi. - Star Wars (1977)",
    "On se reverra toujours à Casablanca. - Casablanca (1942)",
    "J'ai besoin de la vitesse. - Top Gun (1986)",
    "La vie, c'est comme une boîte de chocolats ; on ne sait jamais sur quoi on va tomber. - Forrest Gump (1994)",
    "Je reviendrai. - Terminator (1984)",
    "Vers l'infini et au-delà ! - Toy Story (1995)",
    "Voici Johnny ! - Shining (1980)",
    "Je suis le roi du monde ! - Titanic (1997)",
    "Pourquoi cet air si sérieux ? - The Dark Knight (2008)",
    "La peur est le chemin vers le côté obscur. - Star Wars: Épisode I - La Menace Fantôme (1999)",
    "Un peu d'arc-en-ciel suffit à éclairer tout un ciel. - Les Choristes (2004)",
    "Ils ont les armes, on les emmerde. - Le Cinquième Élément (1997)",
    "Moi, j'ai pas d'amis. - Amélie Poulain (2001)",
    "On n'est pas chez Mémé ici. - La Grande Vadrouille (1966)",
    "Je suis Spartacus ! - Spartacus (1960)",
    "T'as de beaux yeux, tu sais. - Le Quai des Brumes (1938)",
    "Je veux être seul. - L'As de Pique (1932)",
    "Écoutez-moi bien, Monsieur. - Le Dictateur (1940)",
    "Je suis ce que je suis. - Les Enfants du Paradis (1945)",
    "C'est un truc de fou. - Les Tontons Flingueurs (1963)",
    "La classe américaine, c'est nous. - La Classe Américaine (1993)",
    "Elle est où la poulette ? - Le Père Noël est une ordure (1982)",
    "Ils ont les armes, on les emmerde. - Le Cinquième Élément (1997)",
    "La morale, c'est comme la confiture, moins on en a, plus on l'étale. - Les Valseuses (1974)",
    "Vous n'avez rien compris à rien. - Hiroshima mon amour (1959)",
    "Un peu d'arc-en-ciel suffit à éclairer tout un ciel. - Les Choristes (2004)",
    "Je suis un homme, je ne peux pas me passer de femmes. - La Cité de la Peur (1994)",
    "Quand on mettra les cons sur orbite, t'as pas fini de tourner. - Michel Audiard",
    "C'est l'histoire d'un homme qui tombe d'un immeuble de 50 étages. Le mec, au fur et à mesure de sa chute, il se répète sans cesse pour se rassurer : jusqu'ici tout va bien, jusqu'ici tout va bien, jusqu'ici tout va bien. - La Haine (1995)",
    "Si tu es gêné par le bruit des autres, apprends à ne pas être gêné par ta propre respiration. - Amélie Poulain (2001)",
    "Il vaut mieux mobiliser son intelligence sur des conneries que mobiliser sa connerie sur des choses intelligentes. - Les Tontons Flingueurs (1963)",
    "Les cons, ça ose tout. C'est même à ça qu'on les reconnaît. - Les Tontons Flingueurs (1963)",
    "C'est un roc ! C'est un pic ! C'est un cap ! Que dis-je, c'est un cap ? C'est une péninsule ! - Cyrano de Bergerac (1990)",
    "On ne devrait jamais quitter Montauban. - L'Armée des Ombres (1969)",
    "Les cons, ça ose tout. C'est même à ça qu'on les reconnaît. - Les Tontons Flingueurs (1963)",
    "Je suis fatigué patron, fatigué de devoir courir les routes et d'être seul comme un moineau sous la pluie. - Les Temps Modernes (1936)",
    "L'Égypte, c'est un pays de contrastes. D'un côté, vous avez la ville, et de l'autre, le désert. Un peu comme Paris et Marne-la-Vallée. - OSS 117 : Le Caire, nid d'espions (2006)"
    "La première règle du Fight Club est : il est interdit de parler du Fight Club. La seconde règle du Fight Club est : il est interdit de parler du Fight Club. - Fight Club (1999)"
    "Maintenant, si ça ne vous dérange pas, je vais me coucher, avant que l'un de vous ait encore une brillante idée pour nous faire tuer…ou pire, nous faire expulser ! - Harry Potter à l'école des sorciers (2001)"
    "C’est à moi que tu parles ? C’est à moi que tu parles ??... - Taxi Driver (1976)"
    "La différence entre toi et moi, c’est que moi j’ai la classe - Men in Black (1997)"
    "J’adore l’odeur du napalm au petit matin. - Apocalypse Now (1979)"
    "Le coup le plus rusé que le diable ait jamais réussi, c’est de faire croire à tout le monde qu’il n’existait pas. - Usual Suspect (1995)"
    "- C’est bon on peut les avoir. - Ils sont très loin. - Lancez-moi. - Pardon ? - Je ne peux pas sauter aussi loin alors lancez-moi ! - Entendu. - Eh, heu le dites pas à l’Elfe, hein? - Pas un mot. - Le Seigneur des anneaux : Les Deux Tours (2002)"
    "Pas de bras, pas de chocolat - Intouchable (2011)"
    "Balance man... Cadence man... Trace la glace c'est le Coooool Rasta ! - Rasta Rockett (1993)"
    "Vous savez, moi je ne crois pas qu’il y ait de bonne ou de mauvaise situation. Moi, si je devais résumer ma vie aujourd’hui avec vous, je dirais que c’est d’abord des rencontres. Des gens qui m’ont tendu la main, peut-être à un moment où je ne pouvais pas, où j’étais seul chez moi. Et c’est assez curieux de se dire que les hasards, les rencontres forgent une destinée... Parce que quand on a le goût de la chose, quand on a le goût de la chose bien faite, le beau geste, parfois on ne trouve pas l’interlocuteur en face je dirais, le miroir qui vous aide à avancer. Alors ça n’est pas mon cas, comme je disais là, puisque moi au contraire, j’ai pu ; et je dis merci à la vie, je lui dis merci, je chante la vie, je danse la vie... je ne suis qu’amour ! Et finalement, quand des gens me disent « Mais comment fais-tu pour avoir cette humanité ? », je leur réponds très simplement que c’est ce goût de l’amour, ce goût donc qui m’a poussé aujourd’hui à entreprendre une construction mécanique... mais demain qui sait ? Peut-être simplement à me mettre au service de la communauté, à faire le don, le don de soi. - Astérix et Obélix : Mission Cléopâtre (2002)"
]

phrase_chargement = [
    "Plongée dans la matrice en cours",
    "En attente de l'arrivée des dinosaures",
    "Chargement dans l'espace-temps, façon Retour vers le Futur.",
    "Élaboration de votre Truman Show personnel",
    "Tentative d'éviter l'iceberg droit devant !",
    "Saut dans l'hyperespace cinéphile",
    "Auto-destruction de l'écran de chargement en cours...",
    "Préparation de votre rêve partagé",
    "Ouverture d'une brèche dans votre chargement à coup de hache",
    "Je suis un écran, un écran de chargement ",
    "Déchiffrement du Da Vinci Code en cours...",
    "Recrutement de nouveau Avengers en cours ",
    "Concoction de votre potion cinématographique en cours.",
    "Création de la communauté des cinéphiles",
    "Envolé de l'écran de chargement à vélo",
    "Voyage vers l'inconnu  et l'au delà cinématographique !",
    "Exposition à la kryptonite en cours"
]

# Sélectionner une citation aléatoire
citation_aleatoire = random.choice(phrase_chargement)

with st.spinner(citation_aleatoire):
    time.sleep(5)

#Options Menu
with st.sidebar:
    selected = option_menu('Projet2xCBC', ["Présentation", 'Recommendation','Le petit +'],
    icons=['play-btn','search','info-circle'], menu_icon='intersect', default_index=0)

if selected=="Présentation":
    #Header
    st.title("**Le mode d'emploi :**")
    st.subheader("Bienvenue dans notre Système de Recommandation Cinématographique Exclusif !")
    st.write("Afin de vous proposer la meilleure expérience possible notre équipe de Data Analyst, a travaillé d'arrache-pied pour vous, et nous sommes fiers de nous proposer notre outil.")
    st.subheader("**__Guide de bonne pratique :__**")
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
    st.write("Vous avez eu le courage de lire ce mode d'emploi, vous pouvez donc profitez de notre *easter egg* essentiel à votre passion de cinéphile !")


if selected=="Recommendation":
    #Header
    st.title("Voici pour vous, nos suggestions d'après vos critères")
    st.subheader('Find your perfect film !')

    st.divider()
    # Création de la sidebar et features
    st.sidebar.title('Votre système de recommandation')

    # # Filtrer par film. Le point unique permet de retourner une lsite plutôt que d'avoir à saisir du texte.
    selected_film = st.sidebar.multiselect('Sélectionnez votre film', df_ML['french_title'].unique())

    # # Filtrer par d'autres conditions
    selected_conditions = st.sidebar.multiselect("Sélectionnez d'autres paramètres (genre(s),acteur(s)/actrice(s),réalisateur) :", citations_films)

if selected=="Le petit +":
    #Header
    st.title("Le modele d'defdsvdv :")
    st.subheader("Si vo !")
    st.write("Salut la compagnie !")
    st.write("qsdsqc à la marche")