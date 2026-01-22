import streamlit as st
from utils.helpers import check_authentication, logout, init_session_state
from utils.styles import get_custom_css
from models.db_manager import DatabaseManager
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Décideurs - Exam Scheduler",
    page_icon="📊",
    layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

init_session_state()
check_authentication()

if st.session_state.user['role'] not in ['Administrateur']:
    st.error("❌ Accès réservé aux décideurs (Administrateurs)")
    st.stop()

st.markdown("""
<div class="main-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="color: white; margin: 0; font-size: 1.75rem;">📊 Tableau de Bord</h1>
            <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;">
                Vue Stratégique Globale - Direction
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

stats = DatabaseManager.get_statistics()
examens_df = DatabaseManager.get_all_examens()

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">Indicateurs Clés de Performance</p>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    nb_examens = len(examens_df) if not examens_df.empty else 0
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="color: #3b82f6; margin: 0; font-size: 0.9rem;">Examens Programmés</h3>
        <h2 style="margin: 0.5rem 0; font-size: 2rem;">{nb_examens}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    occupation = 0
    if not examens_df.empty and stats.get('capacite_totale'):
        total_capacity = int(stats['capacite_totale'])
        occupation = (nb_examens / total_capacity * 100) if total_capacity > 0 else 0
    
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="color: #10b981; margin: 0; font-size: 0.9rem;">Taux d'Occupation</h3>
        <h2 style="margin: 0.5rem 0; font-size: 2rem;">{occupation:.1f}%</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    conflits_count = len(st.session_state.conflits) if st.session_state.conflits else 0
    
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="color: #f59e0b; margin: 0; font-size: 0.9rem;">Conflits Restants</h3>
        <h2 style="margin: 0.5rem 0; font-size: 2rem;">{conflits_count}</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    total_depts = stats.get('total_departements', 7)
    
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="color: #8b5cf6; margin: 0; font-size: 0.9rem;">Départements</h3>
        <h2 style="margin: 0.5rem 0; font-size: 2rem;">0/{total_depts}</h2>
        <p style="color: #64748b; margin: 0; font-size: 0.85rem;">Validations</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

if not examens_df.empty:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="section-title">Répartition par Département</p>', unsafe_allow_html=True)
        
        dept_counts = examens_df.groupby('departement').size().reset_index(name='count')
        
        fig = px.pie(
            dept_counts,
            values='count',
            names='departement',
            color_discrete_sequence=['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#06b6d4', '#ec4899']
        )
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            height=350,
            showlegend=True,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="section-title">Charge par Formation</p>', unsafe_allow_html=True)
        
        formation_counts = examens_df.groupby('formation').size().reset_index(name='count')
        formation_counts = formation_counts.sort_values('count', ascending=True)
        
        fig2 = px.bar(
            formation_counts,
            x='count',
            y='formation',
            orientation='h',
            color='count',
            color_continuous_scale='Blues'
        )
        
        fig2.update_layout(
            height=350,
            showlegend=False,
            xaxis_title="Nombre d'examens",
            yaxis_title="",
            margin=dict(l=20, r=20, t=20, b=20)
        )
        
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Répartition Temporelle</p>', unsafe_allow_html=True)
    
    examens_df['date'] = pd.to_datetime(examens_df['date_heure']).dt.date
    daily_counts = examens_df.groupby('date').size().reset_index(name='count')
    
    fig3 = px.line(
        daily_counts,
        x='date',
        y='count',
        markers=True,
        color_discrete_sequence=['#3b82f6']
    )
    
    fig3.update_layout(
        height=300,
        xaxis_title="Date",
        yaxis_title="Nombre d'examens",
        margin=dict(l=20, r=20, t=20, b=20),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">📋 Planning Complet des Examens</p>', unsafe_allow_html=True)
    
    examens_display = examens_df.copy()
    examens_display['date_heure'] = pd.to_datetime(examens_display['date_heure']).dt.strftime('%d/%m/%Y %H:%M')
    
    st.dataframe(
        examens_display[['date_heure', 'module', 'formation', 'salle', 'capacite', 'professeur']],
        use_container_width=True,
        hide_index=True,
        column_config={
            "date_heure": "Date et Heure",
            "module": "Module",
            "formation": "Formation",
            "salle": "Salle",
            "capacite": "Capacité",
            "professeur": "Surveillant"
        }
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">✅ Validation Finale</p>', unsafe_allow_html=True)

if nb_examens == 0:
    st.warning("⚠️ Aucun examen à valider. Contactez le service de planification.")
elif conflits_count > 0:
    st.error(f"❌ Impossible de valider: {conflits_count} conflit(s) détecté(s)")
else:
    st.info("✔️ Tous les indicateurs sont au vert. Vous pouvez valider l'emploi du temps.")
    
    if st.button("✅ Valider l'Emploi du Temps Final", use_container_width=True, type="primary"):
        st.markdown("""
        <div class="success-banner">
            ✅ Emploi du temps validé avec succès par la direction !
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.markdown('</div>', unsafe_allow_html=True)

if examens_df.empty:
    st.info("📝 Aucun examen planifié. Contactez le service planification pour générer un planning.")