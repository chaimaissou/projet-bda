import streamlit as st
from utils.helpers import check_authentication, logout, init_session_state
from utils.styles import get_custom_css
from services.scheduler_service import SchedulerService
from services.conflict_detector import ConflictDetector
from models.db_manager import DatabaseManager
import time
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Administration - Exam Scheduler",
    page_icon="⚙️",
    layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

init_session_state()
check_authentication()

if st.session_state.user['role'] != 'Administrateur':
    st.error("Accès non autorisé")
    st.stop()

st.markdown("""
<div class="main-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="color: white; margin: 0; font-size: 1.75rem;">Administration</h1>
            <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;">
                Service de Planification des Examens
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

tab1, tab2, tab3 = st.tabs(["📋 Planification Manuelle", "🤖 Génération Automatique", "🏢 Disponibilité Salles"])


with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">📅 Configuration Manuelle des Examens</p>', unsafe_allow_html=True)
    
    # Section 1: Configuration de base
    st.markdown("**1️⃣ Paramètres de l'Examen**", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        date_exam = st.date_input(
            "📆 Date de l'examen",
            value=pd.to_datetime("2026-02-01")
        )
    
    with col2:
        heure_exam = st.time_input(
            "🕐 Heure de début",
            value=pd.to_datetime("08:00").time()
        )
    
    col1, col2 = st.columns(2)
    
    with col1:
        duree = st.selectbox(
            "⏱️ Durée de l'examen",
            options=[90, 120, 150, 180],
            index=1,
            format_func=lambda x: f"{x} minutes"
        )
    
    with col2:
        modules_df = DatabaseManager.get_all_modules()
        if not modules_df.empty:
            module_selected = st.selectbox(
                "📚 Module",
                options=modules_df['id'].tolist(),
                format_func=lambda x: f"{modules_df[modules_df['id']==x]['code'].values[0]} - {modules_df[modules_df['id']==x]['nom'].values[0]}"
            )
    
    st.divider()
    
    # Section 2: Vérification disponibilité
    st.markdown("**2️⃣ Vérification Disponibilité des Salles**", unsafe_allow_html=True)
    
    date_heure_str = f"{date_exam} {heure_exam.strftime('%H:%M')}"
    date_heure_exam = datetime.strptime(date_heure_str, '%Y-%m-%d %H:%M')
    
    salles_df = DatabaseManager.get_available_rooms()
    salles_dispo = []
    
    for idx, salle in salles_df.iterrows():
        is_available = DatabaseManager.check_room_availability(
            salle['id'],
            date_heure_str,
            duree
        )
        
        salles_dispo.append({
            'id': salle['id'],
            'code': salle['code'],
            'nom': salle['nom'],
            'capacite': salle['capacite'],
            'type': salle['type'],
            'batiment': salle['batiment'],
            'disponible': is_available
        })
    
    salles_dispo_df = pd.DataFrame(salles_dispo)
    
    # Affichage en grille amélioré
    cols = st.columns(2)
    col_idx = 0
    
    for idx, salle in salles_dispo_df.iterrows():
        with cols[col_idx % 2]:
            if salle['disponible']:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%); 
                border-left: 5px solid #10b981; padding: 1.2rem; border-radius: 10px; 
                margin-bottom: 1rem; box-shadow: 0 2px 8px rgba(16, 185, 129, 0.1);">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <strong style="color: #065f46; font-size: 1.1rem;">{salle['code']} - {salle['nom']}</strong><br>
                            <span style="color: #047857; font-size: 0.9rem;">📍 {salle['batiment']} | 👥 {salle['capacite']} places</span><br>
                            <span style="color: #047857; font-size: 0.85rem;">🏷️ {salle['type']}</span>
                        </div>
                        <span style="color: #10b981; font-weight: 700, font-size: 1.2rem;">✓</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); 
                border-left: 5px solid #ef4444; padding: 1.2rem; border-radius: 10px; 
                margin-bottom: 1rem; box-shadow: 0 2px 8px rgba(239, 68, 68, 0.1);">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <strong style="color: #991b1b; font-size: 1.1rem;">{salle['code']} - {salle['nom']}</strong><br>
                            <span style="color: #b91c1c; font-size: 0.9rem;">📍 {salle['batiment']} | 👥 {salle['capacite']} places</span><br>
                            <span style="color: #b91c1c; font-size: 0.85rem;">🏷️ {salle['type']}</span>
                        </div>
                        <span style="color: #ef4444; font-weight: 700, font-size: 1.2rem;">✕</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        col_idx += 1
    
    st.divider()
    
    # Section 3: Sélection
    st.markdown("**3️⃣ Sélection de la Salle et du Surveillant**", unsafe_allow_html=True)
    
    salles_dispo_only = salles_dispo_df[salles_dispo_df['disponible'] == True]
    
    if not salles_dispo_only.empty:
        salle_selected = st.selectbox(
            "🏢 Sélectionner la salle",
            options=salles_dispo_only['id'].tolist(),
            format_func=lambda x: f"{salles_dispo_only[salles_dispo_only['id']==x]['code'].values[0]} - {salles_dispo_only[salles_dispo_only['id']==x]['nom'].values[0]} (Capacité: {salles_dispo_only[salles_dispo_only['id']==x]['capacite'].values[0]})"
        )
    else:
        st.error("❌ Aucune salle disponible à ce créneau horaire")
        salle_selected = None
    
    professeurs_df = DatabaseManager.get_all_professeurs()
    
    if not professeurs_df.empty:
        surveillant_selected = st.selectbox(
            "👨‍🏫 Surveillant principal",
            options=professeurs_df['id'].tolist(),
            format_func=lambda x: f"{professeurs_df[professeurs_df['id']==x]['nom'].values[0]} {professeurs_df[professeurs_df['id']==x]['prenom'].values[0]} ({professeurs_df[professeurs_df['id']==x]['departement'].values[0]})"
        )
    
    st.divider()
    
    # Section 4: Résumé et bouton
    if st.button("➕ Ajouter cet Examen au Planning", use_container_width=True, type="primary"):
        if salle_selected is None:
            st.error("Impossible d'ajouter l'examen : aucune salle disponible")
        else:
            # Afficher le résumé
            st.info("📋 Résumé de l'Examen")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**📚 Module:** {modules_df[modules_df['id']==module_selected]['code'].values[0]}")
                st.write(f"**📅 Date:** {date_exam.strftime('%d/%m/%Y')}")
                st.write(f"**🕐 Heure:** {heure_exam.strftime('%H:%M')}")
                
            with col2:
                st.write(f"**⏱️ Durée:** {duree} minutes")
                st.write(f"**🏢 Salle:** {salles_dispo_only[salles_dispo_only['id']==salle_selected]['code'].values[0]}")
                st.write(f"**👨‍🏫 Surveillant:** {professeurs_df[professeurs_df['id']==surveillant_selected]['nom'].values[0]}")
            
            date_heure_str = f"{date_exam.strftime('%Y-%m-%d')} {heure_exam.strftime('%H:%M')}"
            
            print(f"DEBUG: Tentative insertion avec les paramètres:")
            print(f"  module_id: {module_selected}")
            print(f"  date_heure: {date_heure_str}")
            print(f"  duree: {duree}")
            print(f"  salle_id: {salle_selected}")
            print(f"  surveillant_id: {surveillant_selected}")
            
            # Insérer dans la base
            success = DatabaseManager.insert_examen(
                module_selected,
                date_heure_str,
                duree,
                salle_selected,
                surveillant_selected
            )
            
            if success:
                st.success("✅ Examen ajouté avec succès au planning !")
                st.balloons()
                time.sleep(2)
                st.rerun()
            else:
                st.error("❌ Erreur lors de l'ajout de l'examen")
                st.warning("💡 Vérifications à faire:")
                st.write("- Vérifiez la console pour les logs détaillés")
                st.write("- Vérifiez que la salle n'est pas déjà occupée")
                st.write("- Vérifiez que tous les IDs existent en base")
    
    st.markdown('</div>', unsafe_allow_html=True)


with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Configuration de la Génération Automatique</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        date_debut = st.date_input(
            "Date de début",
            value=pd.to_datetime("2026-02-01"),
            key="auto_date_debut"
        )
    
    with col2:
        date_fin = st.date_input(
            "Date de fin",
            value=pd.to_datetime("2026-02-15"),
            key="auto_date_fin"
        )
    
    with col3:
        duree_creneau = st.selectbox(
            "Durée des créneaux",
            options=[90, 120, 150, 180],
            index=1,
            format_func=lambda x: f"{x} minutes",
            key="auto_duree"
        )
    
    st.markdown("---")
    
    modules_df = DatabaseManager.get_all_modules()
    professeurs_df = DatabaseManager.get_all_professeurs()
    
    st.markdown("**Sélection des Modules et Surveillants**")
    
    selected_modules = []
    
    if not modules_df.empty:
        for idx, module in modules_df.iterrows():
            col1, col2, col3 = st.columns([3, 3, 1])
            
            with col1:
                include = st.checkbox(
                    f"{module['code']} - {module['nom']}",
                    value=True,
                    key=f"module_auto_{module['id']}"
                )
            
            with col2:
                surveillant = st.selectbox(
                    "Surveillant principal",
                    options=professeurs_df['id'].tolist(),
                    format_func=lambda x: f"{professeurs_df[professeurs_df['id']==x]['nom'].values[0]} {professeurs_df[professeurs_df['id']==x]['prenom'].values[0]}",
                    key=f"surveillant_auto_{module['id']}",
                    label_visibility="collapsed"
                )
            
            with col3:
                st.write(f"{module['credits']} crédits")
            
            if include:
                surveillant_nom = f"{professeurs_df[professeurs_df['id']==surveillant]['nom'].values[0]} {professeurs_df[professeurs_df['id']==surveillant]['prenom'].values[0]}"
                selected_modules.append({
                    'module_id': module['id'],
                    'module_nom': module['nom'],
                    'module_code': module['code'],
                    'surveillant_id': surveillant,
                    'surveillant_nom': surveillant_nom
                })
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🤖 Générer le Planning Automatique", use_container_width=True, type="primary", key="btn_auto"):
        if len(selected_modules) == 0:
            st.error("Veuillez sélectionner au moins un module")
        else:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("Initialisation de l'algorithme...")
            progress_bar.progress(10)
            time.sleep(0.3)
            
            status_text.text("Récupération des données...")
            progress_bar.progress(30)
            time.sleep(0.3)
            
            start_time = time.time()
            
            status_text.text("Génération du planning optimal...")
            progress_bar.progress(50)
            
            examens, conflits_initiaux = SchedulerService.generate_schedule_with_modules(
                date_debut.strftime('%Y-%m-%d'),
                date_fin.strftime('%Y-%m-%d'),
                selected_modules,
                duree_creneau
            )
            
            progress_bar.progress(70)
            
            status_text.text("Détection des conflits...")
            conflits_finaux = ConflictDetector.detect_conflicts(examens)
            all_conflits = conflits_initiaux + conflits_finaux
            
            progress_bar.progress(85)
            
            status_text.text("Sauvegarde dans la base de données...")
            success = SchedulerService.save_schedule_to_db(examens)
            
            progress_bar.progress(100)
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            st.session_state.examens = examens
            st.session_state.conflits = all_conflits
            st.session_state.generation_time = execution_time
            
            status_text.empty()
            progress_bar.empty()
            
            st.markdown(f"""
            <div class="success-banner">
                Génération terminée en {execution_time:.2f} secondes - 
                {len(examens)} examens planifiés - 
                {len(all_conflits)} conflits détectés
            </div>
            """, unsafe_allow_html=True)


with tab3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Vérifier Disponibilité des Salles</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        check_date = st.date_input(
            "Date",
            value=pd.to_datetime("2026-02-01"),
            key="check_date"
        )
    
    with col2:
        check_heure = st.time_input(
            "Heure",
            value=pd.to_datetime("08:00").time(),
            key="check_heure"
        )
    
    with col3:
        check_duree = st.selectbox(
            "Durée",
            options=[90, 120, 150, 180],
            index=1,
            format_func=lambda x: f"{x} minutes",
            key="check_duree"
        )
    
    if st.button("🔍 Vérifier Disponibilité", use_container_width=True):
        check_datetime_str = f"{check_date} {check_heure.strftime('%H:%M')}"
        
        salles_df = DatabaseManager.get_available_rooms()
        
        disponibilites = []
        
        for idx, salle in salles_df.iterrows():
            is_available = DatabaseManager.check_room_availability(
                salle['id'],
                check_datetime_str,
                check_duree
            )
         
            occupied_by = None
            if not is_available:
                occupied_by = DatabaseManager.get_room_occupation(
                    salle['id'],
                    check_datetime_str,
                    check_duree
                )
            
            disponibilites.append({
                'Salle': f"{salle['code']} - {salle['nom']}",
                'Type': salle['type'],
                'Capacité': salle['capacite'],
                'Bâtiment': salle['batiment'],
                'Statut': '✅ DISPONIBLE' if is_available else '❌ OCCUPÉE',
                'Occupée par': occupied_by if occupied_by else '-'
            })
        
        dispo_df = pd.DataFrame(disponibilites)
        
        st.dataframe(
            dispo_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Statut": st.column_config.TextColumn(
                    "Statut",
                    width="medium"
                )
            }
        )
    
    st.markdown('</div>', unsafe_allow_html=True)


if st.session_state.examens or DatabaseManager.get_all_examens().shape[0] > 0:
    st.markdown("<br>", unsafe_allow_html=True)
    
    examens_df = DatabaseManager.get_all_examens()
    
    if not examens_df.empty:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3 style="color: #3b82f6; margin: 0; font-size: 0.9rem;">Examens Planifiés</h3>
                <h2 style="margin: 0.5rem 0; font-size: 2rem;">{len(examens_df)}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            conflits_count = len(st.session_state.conflits) if st.session_state.conflits else 0
            st.markdown(f"""
            <div class="metric-card">
                <h3 style="color: #f59e0b; margin: 0; font-size: 0.9rem;">Conflits Détectés</h3>
                <h2 style="margin: 0.5rem 0; font-size: 2rem;">{conflits_count}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            exec_time = st.session_state.generation_time or 0
            st.markdown(f"""
            <div class="metric-card">
                <h3 style="color: #10b981; margin: 0; font-size: 0.9rem;">Temps d'Exécution</h3>
                <h2 style="margin: 0.5rem 0; font-size: 2rem;">{exec_time:.2f}s</h2>
            </div>
            """, unsafe_allow_html=True)
        
        if st.session_state.conflits:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<p class="section-title">Panneau de Contrôle des Conflits</p>', unsafe_allow_html=True)
            
            for conflit in st.session_state.conflits:
                box_class = "error-box" if conflit['gravite'] == 'error' else "alert-box"
                st.markdown(f"""
                <div class="{box_class}">
                    <strong>{conflit['type']}</strong><br>
                    {conflit['details']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="section-title">Planning Complet des Examens</p>', unsafe_allow_html=True)
        
        st.dataframe(
            examens_df[['date_heure', 'module', 'salle', 'capacite', 'professeur']],
            use_container_width=True,
            hide_index=True
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            csv = examens_df.to_csv(index=False)
            st.download_button(
                label="📥 Télécharger le Planning (CSV)",
                data=csv,
                file_name="planning_examens.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col2:
            if st.button("🗑️ Supprimer Tout le Planning", use_container_width=True, type="secondary"):
                if DatabaseManager.delete_all_examens():
                    st.session_state.examens = []
                    st.session_state.conflits = []
                    st.success("Planning supprimé")
                    time.sleep(1)
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)