import streamlit as st
from utils.helpers import check_authentication, logout, init_session_state
from utils.styles import get_custom_css
from models.db_manager import DatabaseManager
import pandas as pd

st.set_page_config(
    page_title="Consultation - Exam Scheduler",
    page_icon="📅",
    layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

init_session_state()
check_authentication()

st.markdown("""
<div class="main-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="color: white; margin: 0; font-size: 1.75rem;">📅 Consultation des Examens</h1>
            <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;">
                Votre Planning Personnalisé
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

# Récupérer les examens
examens_df = DatabaseManager.get_all_examens()

print(f"\n📊 DEBUG Consultation.py:")
print(f"   Type: {type(examens_df)}")
print(f"   Shape: {examens_df.shape if isinstance(examens_df, pd.DataFrame) else 'N/A'}")
print(f"   Empty: {examens_df.empty if isinstance(examens_df, pd.DataFrame) else 'N/A'}")
print(f"   Len: {len(examens_df) if isinstance(examens_df, pd.DataFrame) else 'N/A'}")

# Afficher un petit aperçu
if isinstance(examens_df, pd.DataFrame) and len(examens_df) > 0:
    print(f"   Colonnes: {examens_df.columns.tolist()}")
    print(f"   Premiers examens:")
    print(examens_df.head().to_string())

# Vérifier que c'est un DataFrame valide
if isinstance(examens_df, pd.DataFrame) and len(examens_df) > 0:
    print(f"\n✅ {len(examens_df)} examens trouvés - Affichage des filtres")
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">🔍 Filtres de Recherche</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        departements = ['Tous'] + sorted([str(d) for d in examens_df['departement'].dropna().unique().tolist() if d and str(d) != 'nan'])
        dept_filter = st.selectbox("Département", departements)
    
    with col2:
        formations = ['Toutes'] + sorted([str(f) for f in examens_df['formation'].dropna().unique().tolist() if f and str(f) != 'nan'])
        formation_filter = st.selectbox("Formation", formations)
    
    with col3:
        search_term = st.text_input("Recherche", placeholder="Module, salle, professeur...")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    filtered_df = examens_df.copy()
    
    if dept_filter != 'Tous' and dept_filter:
        filtered_df = filtered_df[filtered_df['departement'].astype(str) == str(dept_filter)]
    
    if formation_filter != 'Toutes' and formation_filter:
        filtered_df = filtered_df[filtered_df['formation'].astype(str) == str(formation_filter)]
    
    if search_term:
        mask = (
            filtered_df['module'].astype(str).str.contains(search_term, case=False, na=False) |
            filtered_df['salle'].astype(str).str.contains(search_term, case=False, na=False) |
            filtered_df['professeur'].astype(str).str.contains(search_term, case=False, na=False)
        )
        filtered_df = filtered_df[mask]
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<p class="section-title">📋 Planning des Examens ({len(filtered_df)} résultats)</p>', unsafe_allow_html=True)
    
    if len(filtered_df) > 0:
        print(f"   Affichage de {len(filtered_df)} examens filtrés")
        
        filtered_df_display = filtered_df.copy()
        filtered_df_display['date'] = pd.to_datetime(filtered_df_display['date_heure']).dt.strftime('%d/%m/%Y')
        filtered_df_display['heure'] = pd.to_datetime(filtered_df_display['date_heure']).dt.strftime('%H:%M')
        
        for idx, row in filtered_df_display.iterrows():
            st.markdown(f"""
            <div class="exam-card">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div style="flex: 1;">
                        <h3 style="margin: 0 0 0.5rem 0; color: #1e293b; font-size: 1.1rem;">{row['module']}</h3>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.75rem;">
                            <span class="badge badge-blue">{row['module_code']}</span>
                            <span class="badge badge-green">{row['formation']}</span>
                        </div>
                        <p style="color: #64748b; margin: 0; font-size: 0.9rem;">
                            <strong>Département:</strong> {row['departement']}<br>
                            <strong>Surveillant:</strong> {row['professeur']}
                        </p>
                    </div>
                    <div style="text-align: right; min-width: 180px;">
                        <div style="background: #f1f5f9; padding: 0.75rem; border-radius: 8px; margin-bottom: 0.5rem;">
                            <div style="font-size: 0.85rem; color: #64748b;">Date</div>
                            <div style="font-weight: 600; color: #1e293b;">{row['date']}</div>
                        </div>
                        <div style="background: #dbeafe; padding: 0.75rem; border-radius: 8px; margin-bottom: 0.5rem;">
                            <div style="font-size: 0.85rem; color: #1e40af;">Heure</div>
                            <div style="font-weight: 600; color: #1e40af;">{row['heure']}</div>
                        </div>
                        <div style="background: #f0fdf4; padding: 0.75rem; border-radius: 8px;">
                            <div style="font-size: 0.85rem; color: #166534;">Salle</div>
                            <div style="font-weight: 600; color: #166534;">{row['salle']}</div>
                            <div style="font-size: 0.85rem; color: #166534;">Capacité: {row['capacite']}</div>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📥 Télécharger Mon Planning",
            data=csv,
            file_name="mon_planning_examens.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    else:
        st.info("🔍 Aucun examen trouvé avec ces critères")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    print(f"❌ Pas d'examens trouvés ou DataFrame invalide")
    st.info("📝 Aucun planning d'examen disponible pour le moment. Les examens apparaîtront ici dès qu'ils seront planifiés par l'administration.")