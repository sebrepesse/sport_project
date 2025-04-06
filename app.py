import streamlit as st
import time

# Configuration de la page
st.set_page_config(page_title="Suivi Entraînement Cardio", layout="centered")

# Interface utilisateur
st.title("🦙 Cardio Objectif Pérou ")
with st.expander("Information sur l'entrainement"):
    st.write("Suivez les exercices avec un compteur de temps. Le programme dure environ 30 minutes.")
    st.write("Veuillez choisir le temps d'exercice et de repos")

    col1, col2 = st.columns(2)
    tps_exercice = col1.number_input("Temps d'exercice (s)", value=30, key="exercice")
    tps_repos = col2.number_input("Temps de repos (s)", value=30, key="repos")

# Définition des blocs d'entraînement
blocs = [
    [
        ("⌛ 1/6 Preparation - Echauffement", 10),
        ("🏋🏻‍♂️ Jumping Jacks lents", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Fentes à la marche", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Fentes latérales", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Montées de genoux (sans sauter)", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Squat + bras levés", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Crunch lent", tps_exercice),
        ("💨 Repos", tps_repos),
    ],
    [
        ("⌛ 2/6 Preparation - Activation cardio", 10),
        ("🏋🏻‍♂️ Jumping Jack", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Pas chassés lent", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Montain climber lent", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Squat", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Planche", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Repos actif (marche)", tps_exercice)
    ],
    [
        ("⌛ 3/6 Preparation - Cardio & Endurance", 10),
        ("🏋🏻‍♂️ Jumping Jack + squat (3 JJ & 1 squat)", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Fentes avant & arrière", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Squats rapides", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Pas chassés moyen", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Crunch moyen", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Repos actif (marche)", tps_exercice)
    ],
    [
        ("⌛ 4/6 Preparation - Cardio & Renforcement", 10),
        ("🏋🏻‍♂️ Jumping Jack", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Fentes latérales", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Mountain climber modérés", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Squats sautées légers (ou squats rapides)", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Planche avec genoux alternés à la poitrine", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Repos actif (marche)", tps_exercice)
    ],
    [
        ("⌛ 5/6 Preparation - Résistance & Explosivité", 10),
        ("🏋🏻‍♂️ Jumping jack + squat (3 JJ & 1 squat)", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Fentes avant & arrières", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Moutain climbers rapides", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Crunch", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Planche", tps_exercice),
        ("💨 Repos", tps_repos),
        ("🏋🏻‍♂️ Repos actif (marche)", tps_exercice)
    ],
    [
        ("⌛ 6/6 Preparation - Retour au calme & Etirement", 10),
        ("🏋🏻‍♂️ Marche lente + respiration profonde", 60),
        ("🏋🏻‍♂️ Etirement quadriceps (cuisse)", 60),
        ("🏋🏻‍♂️ Etirement ischio-jambiers (derriere cuisse)", 60),
        ("🏋🏻‍♂️ Etirement dos + epaules", 60),
        ("🏋🏻‍♂️ Etirement hanches + adducteurs", 60)
    ]
]

# Initialisation des variables de session
if "is_running" not in st.session_state:
    st.session_state.is_running = False
if "current_bloc_index" not in st.session_state:
    st.session_state.current_bloc_index = 0
if "current_exercise_index" not in st.session_state:
    st.session_state.current_exercise_index = 0

# Fonction pour exécuter un exercice avec affichage progressif
def run_exercise(exercise, duration, next_exercise):
    st.header(f"{exercise}")
    

    countdown_text = st.empty()
    progress_bar = st.progress(0)

    # Affichage du prochain exercice
    st.write("###")
    st.subheader(f"➡️ **Prochain exercice** : {next_exercise}")
    for sec in range(duration, 0, -1):
        countdown_text.markdown(f"<h3>⏳ Temps restant : {sec} sec</h3>", unsafe_allow_html=True)
        progress_bar.progress((duration - sec + 1) / duration)
        time.sleep(1)

    
    countdown_text.markdown("✅ **Terminé !**")
    time.sleep(1)

# Démarrer l'entraînement
if not st.session_state.is_running:
    if st.button("🚀 Démarrer l'entraînement"):
        st.session_state.is_running = True
        st.rerun()

# Boucle principale d'entraînement
if st.session_state.is_running:
    bloc_idx = st.session_state.current_bloc_index
    ex_idx = st.session_state.current_exercise_index

    if bloc_idx < len(blocs):  # Vérifier s'il reste des blocs
        bloc = blocs[bloc_idx]
        if ex_idx < len(bloc):  # Vérifier s'il reste des exercices dans le bloc
            exercice, duree = bloc[ex_idx]
            
            # Définir le prochain exercice (s'il existe)
            next_exercise = bloc[ex_idx + 1][0] if ex_idx + 1 < len(bloc) else "Fin du bloc"

            run_exercise(exercice, duree, next_exercise)

            # Passer à l'exercice suivant
            st.session_state.current_exercise_index += 1
            st.rerun()
        else:
            # Passer au bloc suivant
            st.session_state.current_bloc_index += 1
            st.session_state.current_exercise_index = 0
            st.rerun()
    else:
        st.success("🏆 Entraînement terminé ! Félicitations 🎉")
        st.session_state.is_running = False
