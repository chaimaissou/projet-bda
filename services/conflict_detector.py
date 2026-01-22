from datetime import datetime, timedelta

class ConflictDetector:
    
    @staticmethod
    def detect_conflicts(examens):
        conflits = []
        
        for i, exam1 in enumerate(examens):
            dt1 = datetime.strptime(exam1['date_heure'], '%Y-%m-%d %H:%M')
            end1 = dt1 + timedelta(minutes=exam1['duree'])
            
            for exam2 in examens[i+1:]:
                dt2 = datetime.strptime(exam2['date_heure'], '%Y-%m-%d %H:%M')
                end2 = dt2 + timedelta(minutes=exam2['duree'])
                
                if exam1['salle_id'] == exam2['salle_id']:
                    if not (end1 <= dt2 or end2 <= dt1):
                        conflits.append({
                            'type': 'Conflit de salle',
                            'details': f"{exam1['salle']} occupée simultanément pour {exam1['module']} et {exam2['module']}",
                            'gravite': 'error'
                        })
                
                if exam1.get('surveillant_id') == exam2.get('surveillant_id'):
                    if not (end1 <= dt2 or end2 <= dt1):
                        surveillant = exam1.get('surveillant', 'Surveillant inconnu')
                        conflits.append({
                            'type': 'Conflit de surveillant',
                            'details': f"{surveillant} affecté simultanément à {exam1['module']} et {exam2['module']}",
                            'gravite': 'warning'
                        })
        
        return conflits
    
    @staticmethod
    def validate_capacity(examens, inscriptions_data):
        conflits = []
        
        for exam in examens:
            nb_inscrits = len(inscriptions_data.get(exam['module_id'], []))
            
            if nb_inscrits > exam['capacite']:
                conflits.append({
                    'type': 'Capacité insuffisante',
                    'details': f"{exam['salle']}: {nb_inscrits} étudiants pour {exam['capacite']} places",
                    'gravite': 'warning'
                })
        
        return conflits