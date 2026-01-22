import streamlit as st
from utils.helpers import check_authentication, logout, init_session_state
from utils.styles import get_custom_css
from models.db_manager import DatabaseManager
import pandas as pd

st.set_page_config(
    page_title="Chef de Département - Exam Scheduler",
    page_icon="🏛️",
    layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

init_session_state()
check_authentication()

if st.session_state.user['role'] != 'Professeur':
    st.error("❌ Accès réservé aux chefs de département (Professeurs)")
    st.stop()

st.markdown("""
<div class="main-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="color: white; margin: 0; font-size: 1.75rem;">🏛️ Département d'Informatique</h1>
            <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;">
                Validation et Suivi des Examens
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([5, 1])
with col2:
    st.markdown('<div class="logout-btn">', unsafe_allow_html=True)
    if st.button("Déconnexion", use_container_width=True):
        logout()
    st.markdown('</div>', unsafe_allow_html=True)

examens_df = DatabaseManager.get_all_examens()

if not examens_df.empty:
    dept_examens = examens_df[examens_df['departement'] == 'Informatique']
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Vue d\'Ensemble du Département</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #3b82f6; margin: 0; font-size: 0.9rem;">Examens Planifiés</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">{len(dept_examens)}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        modules_count = dept_examens['module'].nunique() if not dept_examens.empty else 0
        
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #10b981; margin: 0; font-size: 0.9rem;">Modules Concernés</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">{modules_count}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        dept_conflits = [c for c in st.session_state.conflits 
                        if 'Informatique' in c.get('details', '')] if st.session_state.conflits else []
        
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #f59e0b; margin: 0; font-size: 0.9rem;">Alertes</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">{len(dept_conflits)}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if dept_conflits:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="section-title">⚠️ Alertes Spécifiques au Département</p>', unsafe_allow_html=True)
        
        for conflit in dept_conflits:
            box_class = "error-box" if conflit['gravite'] == 'error' else "alert-box"
            st.markdown(f"""
            <div class="{box_class}">
                <strong>{conflit['type']}</strong><br>
                {conflit['details']}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">📅 Planning du Département</p>', unsafe_allow_html=True)
    
    if not dept_examens.empty:
        dept_examens_display = dept_examens.copy()
        dept_examens_display['date_heure'] = pd.to_datetime(dept_examens_display['date_heure']).dt.strftime('%d/%m/%Y %H:%M')
        
        st.dataframe(
            dept_examens_display[['date_heure', 'module', 'salle', 'capacite', 'professeur']],
            use_container_width=True,
            hide_index=True,
            column_config={
                "date_heure": "Date et Heure",
                "module": "Module",
                "salle": "Salle",
                "capacite": "Capacité",
                "professeur": "Surveillant"
            }
        )
        
        csv = dept_examens.to_csv(index=False)
        st.download_button(
            label="📥 Télécharger le Planning du Département",
            data=csv,
            file_name="planning_informatique.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.info("📝 Aucun examen planifié pour ce département")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">✅ Validation Départementale</p>', unsafe_allow_html=True)
    
    remarques = st.text_area(
        "Remarques ou Observations",
        placeholder="Ajoutez vos commentaires concernant le planning...",
        height=100
    )
    
    if len(dept_examens) == 0:
        st.warning("⚠️ Aucun examen à valider pour ce département")
    else:
        if st.button("✅ Valider pour le Département Informatique", use_container_width=True, type="primary"):
            st.markdown("""
            <div class="success-banner">
                ✅ Planning validé pour le département d'Informatique !
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("📝 Aucun planning disponible. Contactez le service planification.")