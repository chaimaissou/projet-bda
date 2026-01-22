import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'exam_scheduler',
    'port': 3306,
    'autocommit': False,
    'use_pure': True
}

def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print(f"✅ Connexion BD réussie")
            return connection
        else:
            print("❌ Connexion échouée")
            return None
    except Error as e:
        print(f"❌ Erreur de connexion BD: {e}")
        return None

def test_connection():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT COUNT(*) as count FROM modules")
            result = cursor.fetchone()
            count = result['count'] if result else 0
            print(f"✅ Test OK - {count} modules en base")
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"❌ Erreur test: {e}")
            return False
    return False