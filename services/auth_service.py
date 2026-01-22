from models.db_manager import DatabaseManager

class AuthService:
    
    @staticmethod
    def login(matricule, nom_prenom):
        try:
            parts = nom_prenom.strip().split(' ', 1)
            if len(parts) != 2:
                return None
            
            nom, prenom = parts
            
            user = DatabaseManager.get_user_by_credentials(matricule, nom, prenom)
            
            if user:
                return {
                    'id': user['id'],
                    'matricule': user['matricule'],
                    'nom': user['nom'],
                    'prenom': user['prenom'],
                    'role': user['role'],
                    'email': user.get('email', ''),
                    'departement_id': user.get('dept_id') or user.get('departement_id'),
                    'formation_id': user.get('formation_id')
                }
            
            return None
            
        except Exception as e:
            print(f"Erreur auth: {e}")
            return None
    
    @staticmethod
    def get_role_display(role):
        roles = {
            'Administrateur': 'Administrateur Examens',
            'Professeur': 'Chef de Département',
            'Etudiant': 'Étudiant'
        }
        return roles.get(role, role)