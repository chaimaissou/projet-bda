import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from utils.styles import get_custom_css
from utils.helpers import init_session_state

st.set_page_config(
    page_title="Exam Scheduler",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

init_session_state()

st.markdown("""
<div class="main-header" style="text-align: center;">
    <h1 style="color: white; font-size: 2.8rem; margin: 0; font-weight: 800;">
    Université M'hamed Bougara - Faculté des Sciences
         Exam Scheduler
    </h1>
    <p style="color: rgba(255,255,255,0.95); font-size: 1.1rem; margin: 1rem 0 0 0; font-weight: 500;">
        Plateforme Intelligente de Gestion des Examens Universitaires
    </p>
</div>
""", unsafe_allow_html=True)

if st.session_state.user:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #e8f2ff 0%, #f0f5ff 100%); 
    border-left: 5px solid #7fa8e8; padding: 1.2rem; border-radius: 8px;">
        <p style="margin: 0; color: #5b7dd6; font-weight: 600;">
            ✅ Connecté en tant que <strong>{st.session_state.user['prenom']} {st.session_state.user['nom']}</strong>
        </p>
        <p style="margin: 0.5rem 0 0 0; color: #7c8fa3; font-size: 0.9rem;">
            Rôle: <strong>{st.session_state.user['role']}</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">🚀 Navigation Rapide</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="metric-card" style="text-align: center; padding: 2.5rem 1.5rem; cursor: pointer;">
            <div style="font-size: 3.5rem; margin-bottom: 1rem; animation: bounce 2s infinite;">⚙️</div>
            <h3 style="margin: 0 0 0.5rem 0; color: #2c3e50; font-size: 1.1rem;">Administration</h3>
            <p style="color: #7c8fa3; margin: 0; font-size: 0.9rem;">Génération et planification</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card" style="text-align: center; padding: 2.5rem 1.5rem; cursor: pointer;">
            <div style="font-size: 3.5rem; margin-bottom: 1rem; animation: bounce 2s infinite 0.2s;">📊</div>
            <h3 style="margin: 0 0 0.5rem 0; color: #2c3e50; font-size: 1.1rem;">Tableau de Bord</h3>
            <p style="color: #7c8fa3; margin: 0; font-size: 0.9rem;">Statistiques et KPIs</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card" style="text-align: center; padding: 2.5rem 1.5rem; cursor: pointer;">
            <div style="font-size: 3.5rem; margin-bottom: 1rem; animation: bounce 2s infinite 0.4s;">📅</div>
            <h3 style="margin: 0 0 0.5rem 0; color: #2c3e50; font-size: 1.1rem;">Consultation</h3>
            <p style="color: #7c8fa3; margin: 0; font-size: 0.9rem;">Plannings personnalisés</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e8f0ff 0%, #f0f5ff 100%); 
    border-left: 5px solid #7fa8e8; padding: 1.5rem; border-radius: 8px; text-align: center;">
        <p style="margin: 0; color: #5b7dd6; font-weight: 600; font-size: 1.05rem;">
            👋 Bienvenue sur Exam Scheduler
        </p>
        <p style="margin: 0.8rem 0 0 0; color: #7c8fa3; font-size: 0.95rem;">
            Connectez-vous via la page <strong>Connexion</strong> dans le menu latéral pour accéder aux fonctionnalités.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">✨ Fonctionnalités Principales</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div style="background: #f9fbfd; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #7fa8e8;">
            <h4 style="margin: 0 0 1rem 0; color: #5b7dd6; font-size: 1rem;">🎯 Planification</h4>
            <ul style="margin: 0; padding-left: 1.5rem; color: #2c3e50; line-height: 1.8;">
                <li><strong>Génération automatique</strong> en moins de 45 secondes</li>
                <li><strong>Détection de conflits</strong> intelligente</li>
                <li><strong>Optimisation</strong> en temps réel</li>
                <li><strong>Gestion multi-départements</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #f9fbfd; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #7fa8e8;">
            <h4 style="margin: 0 0 1rem 0; color: #5b7dd6; font-size: 1rem;">📊 Gestion</h4>
            <ul style="margin: 0; padding-left: 1.5rem; color: #2c3e50; line-height: 1.8;">
                <li><strong>Espaces personnalisés</strong> par rôle</li>
                <li><strong>Exports</strong> PDF et CSV</li>
                <li><strong>Validation</strong> hiérarchique</li>
                <li><strong>Stockage persistant</strong> des données</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: #a0adb6; padding: 3rem 2rem 2rem 2rem; margin-top: 3rem; 
background: linear-gradient(180deg, rgba(245, 248, 252, 0) 0%, #f5f8fc 100%); border-top: 1px solid #e8eef5;">
    <p style="margin: 0; font-size: 0.9rem; font-weight: 500;">© 2026 Exam Scheduler - Plateforme Universitaire</p>
    <p style="margin: 0.8rem 0 0 0; font-size: 0.85rem;">
        Développé avec  par <strong>AISSOU Chaima</strong> & <strong>FLICI Kenza</strong>
    </p>
    <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #e8eef5;">
        <span style="color: #7c8fa3; font-size: 0.8rem;">  Exam Scheduler 2026</span>
    </div>
</div>
""", unsafe_allow_html=True)