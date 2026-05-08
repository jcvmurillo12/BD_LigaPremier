import requests
import sqlite3
import os


def fetch_fixtures(api_key, season=2024):
    """
    Obtiene los partidos finalizados de la Premier League desde la API.
    
    Args:
        api_key: Clave de API para football-api-sports
        season: Temporada a consultar (por defecto 2024)
    
    Returns:
        Lista de partidos con estado "FT" (Finished)
    """
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {"x-apisports-key": api_key}
    params = {"league": 39, "season": season}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error HTTP: {response.status_code}")
            return []
        
        data = response.json()
        
        if "response" not in data:
            print("Error: Respuesta inválida de la API")
            return []
        
        fixtures_finalizados = [
            fixture for fixture in data["response"]
            if fixture["fixture"]["status"]["short"] == "FT"
        ]
        
        return fixtures_finalizados
    
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []


def save_to_sqlite(fixtures, db_path="data/premier_league.db"):
    """
    Guarda los partidos en una base de datos SQLite.
    
    Args:
        fixtures: Lista de partidos obtenidos de la API
        db_path: Ruta de la base de datos SQLite
    """
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Crear tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS partidos (
                id INTEGER PRIMARY KEY,
                fecha TEXT,
                equipo_local TEXT,
                equipo_visitante TEXT,
                goles_local INTEGER,
                goles_visitante INTEGER
            )
        """)
        
        registros_insertados = 0
        
        # Insertar cada partido
        for fixture in fixtures:
            try:
                fixture_id = fixture["fixture"]["id"]
                fecha = fixture["fixture"]["date"]
                equipo_local = fixture["teams"]["home"]["name"]
                equipo_visitante = fixture["teams"]["away"]["name"]
                goles_local = fixture["goals"]["home"]
                goles_visitante = fixture["goals"]["away"]
                
                cursor.execute("""
                    INSERT OR IGNORE INTO partidos 
                    (id, fecha, equipo_local, equipo_visitante, goles_local, goles_visitante)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (fixture_id, fecha, equipo_local, equipo_visitante, goles_local, goles_visitante))
                
                registros_insertados += 1
            
            except (KeyError, TypeError) as e:
                print(f"Error al procesar fixture: {e}")
                continue
        
        conn.commit()
        print(f"Se insertaron {registros_insertados} registros exitosamente.")
        
    except sqlite3.Error as e:
        print(f"Error de base de datos: {e}")
    
    finally:
        if conn:
            conn.close()
