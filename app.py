import streamlit as st
import time

# Configuration de la page
st.set_page_config(page_title="Suivi Entraînement Cardio", layout="centered")

# Interface utilisateur
st.title("🕒 Suivi Entraînement Cardio")
st.write("Suivez les exercices avec un compteur de temps. Le programme dure environ 30 minutes.")
st.write("Veuillez choisir le temps d'exercice et de repos")

col1, col2 = st.columns(2)
tps_exercice = col1.number_input("Temps d'exercice (s)", value=30, key="exercice")
tps_repos = col2.number_input("Temps de repos (s)", value=30, key="repos")

# Définition des blocs d'entraînement
bloc_1 = [
    ("⌛ Preparation", 10),
    ("🏋🏻‍♂️ Jumping Jacks lents", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Talons-fesses dynamiques", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Montées de genoux (sans sauter)", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Squat + bras levés", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Cercle de bras + torsions du buste", tps_exercice),
    ("⌛ Repos", tps_repos),
]
bloc_2 = [
    ("⌛ Preparation", 10),
    ("🏋🏻‍♂️ Jumping Jack classique", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Talons fesses rapides", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Montées de genoux dynamiques modifiés", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Pas chassés rapides", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Repos actif (marche)", tps_exercice)
]

bloc_3 = [
    ("⌛ Preparation", 10),
    ("🏋🏻‍♂️ Burpees modifiés", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Fentes dynamiques (alternes rapidement sans sauter)", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Squats rapides", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Montées de genoux + bras tendus", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Repos actif (marche)", tps_exercice)
]

bloc_4 = [
    ("⌛ Preparation", 10),
    ("🏋🏻‍♂️ Burpees sans pompes", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Mountain climber modérés", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Squats sautées légers (ou squats rapides)", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Planche avec genoux alternés à la poitrine", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Repos actif (marche)", tps_exercice)
]

bloc_5 = [
    ("⌛ Preparation", 10),
    ("🏋🏻‍♂️ Jumping jack + squat (3 JJ & 1 squat)", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Fentes arrières dynamiques", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Moutain climbers rapides", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Burpess modifiés", tps_exercice),
    ("⌛ Repos", tps_repos),
    ("🏋🏻‍♂️ Repos actif (marche)", tps_exercice)
]

bloc_6 = [
    ("🏋🏻‍♂️ Marche lente + respiration profonde", 60),
    ("🏋🏻‍♂️ Etirement quadriceps (cuisse)", 60),
    ("🏋🏻‍♂️ Etirement ischio-jambiers (derriere cuisse)", 60),
    ("🏋🏻‍♂️ Etirement dos + epaules", 60),
    ("🏋🏻‍♂️ Etirement hanches + aducteurs", 60)
]

# Variables de session pour gérer l'état de progression
if "bloc_1_done" not in st.session_state:
    st.session_state.bloc_1_done = False
if "bloc_2_done" not in st.session_state:
    st.session_state.bloc_2_done = False
if "bloc_3_done" not in st.session_state:
    st.session_state.bloc_3_done = False
if "bloc_4_done" not in st.session_state:
    st.session_state.bloc_4_done = False
if "bloc_5_done" not in st.session_state:
    st.session_state.bloc_5_done = False
if "bloc_6_done" not in st.session_state:
    st.session_state.bloc_6_done = False

# Fonction pour exécuter un bloc d'entraînement
def run_workout(block):
    for i, (exercise, duration) in enumerate(block):
        st.subheader(f"{exercise}")

        # Zone dynamique pour le compteur et la barre de progression
        countdown_text = st.empty()
        progress_bar = st.progress(0)

        # Début du compte à rebours
        for sec in range(duration, 0, -1):
            countdown_text.markdown(f"⏳ **Temps restant : {sec} sec**")
            progress_bar.progress((duration - sec + 1) / duration)
            time.sleep(1)

        countdown_text.markdown("✅ **Terminé !**")
        if i < len(block) - 1:
            st.write("**➡️ Prochain exercice...**")
            time.sleep(2)

# Bouton pour démarrer le Bloc 1
if not st.session_state.bloc_1_done:
    if st.button("🚀 Démarrer Bloc 1 - Echauffement"):
        run_workout(bloc_1)
        st.session_state.bloc_1_done = True
        st.rerun()

# Bouton pour démarrer le Bloc 2
if st.session_state.bloc_1_done and not st.session_state.bloc_2_done:
    if st.button("🚀 Démarrer Bloc 2 - Activation cardio"):
        run_workout(bloc_2)
        st.session_state.bloc_2_done = True
        st.rerun()

# Bouton pour démarrer le Bloc 3
if st.session_state.bloc_1_done and st.session_state.bloc_2_done and not st.session_state.bloc_3_done:
    if st.button("🚀 Démarrer Bloc 3 - Cardio & Endurance"):
        run_workout(bloc_3)
        st.session_state.bloc_3_done = True
        st.rerun()

# Bouton pour démarrer le Bloc 4
if st.session_state.bloc_1_done and st.session_state.bloc_2_done and st.session_state.bloc_3_done and not st.session_state.bloc_4_done:
    if st.button("🚀 Démarrer Bloc 4 - Cardio & Renforcement"):
        run_workout(bloc_4)
        st.session_state.bloc_4_done = True
        st.rerun()

# Bouton pour démarrer le Bloc 5
if st.session_state.bloc_1_done and st.session_state.bloc_2_done and st.session_state.bloc_3_done and st.session_state.bloc_4_done and not st.session_state.bloc_5_done:
    if st.button("🚀 Démarrer Bloc 5 - Résistance & Explosivité"):
        run_workout(bloc_5)
        st.session_state.bloc_5_done = True
        st.rerun()

# Bouton pour passer au Bloc 6
if st.session_state.bloc_1_done and st.session_state.bloc_2_done and st.session_state.bloc_3_done and st.session_state.bloc_4_done and st.session_state.bloc_5_done and not st.session_state.bloc_6_done:
    if st.button("➡️ Passer au Bloc 6 - Retour au calme & Etirement"):
        run_workout(bloc_6)
        st.session_state.bloc_6_done = True
        st.success("🎉 Entraînement terminé ! Bravo 💪")
