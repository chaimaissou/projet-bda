from config.database import get_connection
import pandas as pd
from datetime import datetime

class DatabaseManager:
    
    @staticmethod
    def get_user_by_credentials(matricule, nom, prenom):
        conn = get_connection()
        if not conn:
            return None
        
        cursor = conn.cursor(dictionary=True)
        
        tables = [
            ('administrateurs', 'Administrateur'),
            ('professeurs', 'Professeur'),
            ('etudiants', 'Etudiant')
        ]
        
        for table, role in tables:
            query = f"""
                SELECT * FROM {table} 
                WHERE matricule = %s AND nom = %s AND prenom = %s
            """
            cursor.execute(query, (matricule, nom, prenom))
            user = cursor.fetchone()
            
            if user:
                user['role'] = role
                user['table'] = table
                conn.close()
                return user
        
        conn.close()
        return None
    
    @staticmethod
    def get_all_examens():
        conn = get_connection()
        if not conn:
            print("❌ Erreur: Pas de connexion BD")
            return pd.DataFrame()
        
        try:
            query = """
                SELECT 
                    e.id,
                    e.date_heure,
                    e.duree_minutes,
                    e.type_examen,
                    COALESCE(m.nom, 'Module inconnu') as module,
                    COALESCE(m.code, 'N/A') as module_code,
                    COALESCE(l.nom, 'Salle inconnue') as salle,
                    COALESCE(l.code, 'N/A') as salle_code,
                    COALESCE(l.capacite, 0) as capacite,
                    COALESCE(f.nom, 'Formation inconnue') as formation,
                    COALESCE(d.nom, 'Dept inconnu') as departement,
                    COALESCE(CONCAT(p.nom, ' ', p.prenom), 'Professeur inconnu') as professeur
                FROM examens e
                LEFT JOIN modules m ON e.module_id = m.id
                LEFT JOIN lieu_examen l ON e.salle_id = l.id
                LEFT JOIN formations f ON m.formation_id = f.id
                LEFT JOIN departements d ON f.dept_id = d.id
                LEFT JOIN professeurs p ON e.surveillant_principal_id = p.id
                ORDER BY e.date_heure DESC
            """
            
            df = pd.read_sql(query, conn)
            
            print(f"✅ DEBUG get_all_examens:")
            print(f"   - Nombre d'examens: {len(df)}")
            print(f"   - Colonnes: {df.columns.tolist()}")
            if len(df) > 0:
                print(f"   - Premier examen: {df.iloc[0].to_dict()}")
            
            conn.close()
            return df
            
        except Exception as e:
            print(f"❌ Erreur get_all_examens: {e}")
            import traceback
            traceback.print_exc()
            conn.close()
            return pd.DataFrame()
    
    @staticmethod
    def get_statistics():
        conn = get_connection()
        if not conn:
            return {}
        
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM vue_statistiques_globales")
        stats = cursor.fetchone()
        
        conn.close()
        return stats if stats else {}
    
    @staticmethod
    def get_available_rooms():
        conn = get_connection()
        if not conn:
            return pd.DataFrame()
        
        query = "SELECT * FROM lieu_examen WHERE disponibilite = 1 ORDER BY capacite DESC"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    
    @staticmethod
    def check_room_availability(room_id, date_heure, duree_minutes):
        conn = get_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        
        query = """
            SELECT COUNT(*) as count
            FROM examens e
            WHERE e.salle_id = %s
            AND e.date_heure < DATE_ADD(%s, INTERVAL %s MINUTE)
            AND DATE_ADD(e.date_heure, INTERVAL e.duree_minutes MINUTE) > %s
        """
        
        try:
            cursor.execute(query, (room_id, date_heure, duree_minutes, date_heure))
            result = cursor.fetchone()
            conn.close()
            return result[0] == 0
        except Exception as e:
            print(f"Erreur check availability: {e}")
            conn.close()
            return False
    
    @staticmethod
    def get_room_occupation(room_id, date_heure, duree_minutes):
        conn = get_connection()
        if not conn:
            return None
        
        query = """
            SELECT m.code, m.nom, e.date_heure
            FROM examens e
            JOIN modules m ON e.module_id = m.id
            WHERE e.salle_id = %s
            AND e.date_heure < DATE_ADD(%s, INTERVAL %s MINUTE)
            AND DATE_ADD(e.date_heure, INTERVAL e.duree_minutes MINUTE) > %s
            LIMIT 1
        """
        
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (room_id, date_heure, duree_minutes, date_heure))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return f"{result['code']} - {result['nom']} à {result['date_heure']}"
            return None
        except Exception as e:
            print(f"Erreur get occupation: {e}")
            conn.close()
            return None
    
    @staticmethod
    def get_modules_by_formation(formation_id):
        conn = get_connection()
        if not conn:
            return pd.DataFrame()
        
        query = """
            SELECT m.*, CONCAT(p.nom, ' ', p.prenom) as professeur
            FROM modules m
            LEFT JOIN professeurs p ON m.professeur_id = p.id
            WHERE m.formation_id = %s
        """
        df = pd.read_sql(query, conn, params=(formation_id,))
        conn.close()
        return df
    
    @staticmethod
    def get_all_modules():
        conn = get_connection()
        if not conn:
            return pd.DataFrame()
        
        query = """
            SELECT m.*, 
                   CONCAT(p.nom, ' ', p.prenom) as professeur,
                   f.nom as formation,
                   d.nom as departement
            FROM modules m
            LEFT JOIN professeurs p ON m.professeur_id = p.id
            LEFT JOIN formations f ON m.formation_id = f.id
            LEFT JOIN departements d ON f.dept_id = d.id
            ORDER BY m.formation_id, m.code
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    
    @staticmethod
    def get_all_professeurs():
        conn = get_connection()
        if not conn:
            return pd.DataFrame()
        
        query = """
            SELECT p.*, d.nom as departement
            FROM professeurs p
            LEFT JOIN departements d ON p.dept_id = d.id
            ORDER BY p.nom, p.prenom
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    
    @staticmethod
    def insert_examen(module_id, date_heure, duree, salle_id, surveillant_id):
        """
        Insérer un examen dans la base de données
        """
        conn = None
        try:
            conn = get_connection()
            if not conn:
                print("❌ Erreur: Pas de connexion à la base de données")
                return False
            
            cursor = conn.cursor(dictionary=True)
            
            print(f"📋 Paramètres: module={module_id}, date={date_heure}, duree={duree}, salle={salle_id}, surv={surveillant_id}")
            
            # Vérifier module
            cursor.execute("SELECT id FROM modules WHERE id = %s", (module_id,))
            if not cursor.fetchone():
                print(f"❌ Module {module_id} introuvable")
                return False
            
            # Vérifier salle
            cursor.execute("SELECT id FROM lieu_examen WHERE id = %s", (salle_id,))
            if not cursor.fetchone():
                print(f"❌ Salle {salle_id} introuvable")
                return False
            
            # Vérifier professeur
            cursor.execute("SELECT id FROM professeurs WHERE id = %s", (surveillant_id,))
            if not cursor.fetchone():
                print(f"❌ Professeur {surveillant_id} introuvable")
                return False
            
            # Vérifier qu'il n'y a pas de conflit
            check_query = """
                SELECT COUNT(*) as count
                FROM examens e
                WHERE e.salle_id = %s
                AND e.date_heure < DATE_ADD(%s, INTERVAL %s MINUTE)
                AND DATE_ADD(e.date_heure, INTERVAL e.duree_minutes MINUTE) > %s
            """
            
            cursor.execute(check_query, (salle_id, date_heure, duree, date_heure))
            result = cursor.fetchone()
            conflict_count = result['count'] if result else 0
            
            if conflict_count > 0:
                print(f"❌ Conflit détecté: La salle {salle_id} est déjà occupée à cet horaire")
                return False
            
            print(f"✅ Aucun conflit détecté")
            
            # Formater la date correctement
            if isinstance(date_heure, str):
                parts = date_heure.split()
                if len(parts) == 2:
                    date_part, time_part = parts
                    if ':' in time_part and len(time_part) == 5:
                        date_heure = f"{date_part} {time_part}:00"
                    elif ':' not in time_part:
                        date_heure = f"{date_part} {time_part}:00:00"
            
            print(f"📅 Date formatée: {date_heure}")
            
            # Insérer l'examen
            insert_query = """
                INSERT INTO examens 
                (module_id, date_heure, duree_minutes, salle_id, surveillant_principal_id, statut, type_examen)
                VALUES (%s, %s, %s, %s, %s, 'Planifié', 'Écrit')
            """
            
            print(f"🔄 Tentative d'insertion...")
            cursor.execute(insert_query, (module_id, date_heure, duree, salle_id, surveillant_id))
            conn.commit()
            
            exam_id = cursor.lastrowid
            print(f"✅ Examen inséré avec succès! ID: {exam_id}")
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur insertion examen: {str(e)}")
            import traceback
            traceback.print_exc()
            if conn:
                try:
                    conn.rollback()
                except:
                    pass
            return False
        
        finally:
            try:
                if conn:
                    conn.close()
            except:
                pass
    
    @staticmethod
    def delete_all_examens():
        conn = get_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        
        try:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            cursor.execute("DELETE FROM examens")
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
            conn.commit()
            print("Tous les examens supprimés")
            success = True
        except Exception as e:
            print(f"Erreur suppression: {e}")
            conn.rollback()
            success = False
        finally:
            cursor.close()
            conn.close()
        
        return success