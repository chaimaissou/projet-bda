from config.database import get_connection, test_connection
from models.db_manager import DatabaseManager

print("=== TEST CONNEXION ===")
test_connection()

print("\n=== TEST MODULES ===")
modules = DatabaseManager.get_all_modules()
print(f"Modules trouvés: {len(modules)}")
if not modules.empty:
    print(modules[['id', 'code', 'nom']].head())

print("\n=== TEST SALLES ===")
salles = DatabaseManager.get_available_rooms()
print(f"Salles trouvées: {len(salles)}")
if not salles.empty:
    print(salles[['id', 'code', 'nom', 'capacite']].head())

print("\n=== TEST PROFESSEURS ===")
profs = DatabaseManager.get_all_professeurs()
print(f"Professeurs trouvés: {len(profs)}")
if not profs.empty:
    print(profs[['id', 'nom', 'prenom']].head())

print("\n=== TEST INSERTION ===")
result = DatabaseManager.insert_examen(
    module_id=1,
    date_heure="2026-02-01 08:00:00",
    duree=120,
    salle_id=1,
    surveillant_id=1
)
print(f"Insertion test: {'✅ Réussi' if result else '❌ Échec'}")

print("\n=== TEST EXAMENS ===")
examens = DatabaseManager.get_all_examens()
print(f"Examens dans la BD: {len(examens)}")