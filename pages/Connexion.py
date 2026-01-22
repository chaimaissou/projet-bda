import streamlit as st
from services.auth_service import AuthService
from utils.helpers import init_session_state
from utils.styles import get_custom_css

st.set_page_config(
    page_title="Connexion - Exam Scheduler",
    page_icon="👤",
    layout="centered"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

init_session_state()

if st.session_state.user is not None:
    st.success(f"✅ Vous êtes déjà connecté en tant que **{st.session_state.user['prenom']} {st.session_state.user['nom']}** ({st.session_state.user['role']})")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚪 Se déconnecter", use_container_width=True, type="primary"):
        st.session_state.user = None
        st.rerun()
    
    st.stop()

st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h1 style="color: #667eea; font-size: 3rem; margin: 0;">🎓 Num_Exam</h1>
    <p style="color: #6b7280; font-size: 1.2rem; margin-top: 0.5rem;">Connexion à la plateforme</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card" style="max-width: 500px; margin: 2rem auto;">', unsafe_allow_html=True)

with st.form("login_form"):
    st.markdown("### 🔐 Identifiants")
    
    matricule = st.text_input(
        "Matricule",
        placeholder="Ex: ADM001, PROF001, ETU001",
        help="Votre matricule universitaire"
    )
    
    nom_prenom = st.text_input(
        "Nom et Prénom",
        placeholder="Ex: Durand Robert",
        help="Format: Nom Prénom (séparés par un espace)"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    submitted = st.form_submit_button("🔑 Se connecter", use_container_width=True, type="primary")
    
    if submitted:
        if not matricule or not nom_prenom:
            st.error("⚠️ Veuillez remplir tous les champs")
        else:
            with st.spinner("Authentification en cours..."):
                user = AuthService.login(matricule, nom_prenom)
                
                if user:
                    st.session_state.user = user
                    st.success(f"✅ Connexion réussie ! Bienvenue **{user['prenom']} {user['nom']}**")
                    st.balloons()
                    st.rerun()
                else:
                    st.error("❌ Identifiants incorrects. Vérifiez votre matricule, nom et prénom.")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="card" style="max-width: 600px; margin: 0 auto;">', unsafe_allow_html=True)
st.markdown("### 💡 Comptes de Test")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **👨‍💼 Administrateur**
    - Matricule: `ADM001`
    - Nom Prénom: `Durand Robert`
    
    **📊 Décideur**
    - Matricule: `ADM002`
    - Nom Prénom: `Lefevre Catherine`
    """)

with col2:
    st.markdown("""
    **🏛️ Chef de Département**
    - Matricule: `PROF001`
    - Nom Prénom: `Martin Jean`
    
    **🎓 Étudiant**
    - Matricule: `ETU001`
    - Nom Prénom: `Dupont Jean`
    """)

st.markdown('</div>', unsafe_allow_html=True)