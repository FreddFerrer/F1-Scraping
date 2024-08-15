import datetime
import requests
import mysql.connector
from bs4 import BeautifulSoup

# Conectar a la base de datos
connection = mysql.connector.connect(
    host='localhost',  # Si estás ejecutando desde tu máquina local
    port=3310,         # El puerto mapeado en tu contenedor Docker
    user='freddy',
    password='Test123',
    database='db_motorsport_predictor_f1'
)

# Datos obtenidos del scraping
races_data = [
    {'race_name': 'Bahrain GP', 'date': '2024-03-02', 'time': '18:00:00'},
    {'race_name': 'Saudi Arabian GP', 'date': '2024-03-09', 'time': '20:00:00'},
    {'race_name': 'Australian GP', 'date': '2024-03-24', 'time': '15:00:00'},
    {'race_name': 'Japanese GP', 'date': '2024-04-07', 'time': '14:00:00'},
    {'race_name': 'Chinese GP', 'date': '2024-04-21', 'time': '15:00:00'},
    {'race_name': 'Miami GP', 'date': '2024-05-05', 'time': '16:00:00'},
    {'race_name': 'Emilia Romagna GP', 'date': '2024-05-19', 'time': '15:00:00'},
    {'race_name': 'Monaco GP', 'date': '2024-05-26', 'time': '15:00:00'},
    {'race_name': 'Canadian GP', 'date': '2024-06-09', 'time': '14:00:00'},
    {'race_name': 'Spanish GP', 'date': '2024-06-23', 'time': '15:00:00'},
    {'race_name': 'Austrian GP', 'date': '2024-06-30', 'time': '15:00:00'},
    {'race_name': 'British GP', 'date': '2024-07-07', 'time': '15:00:00'},
    {'race_name': 'Hungarian GP', 'date': '2024-07-21', 'time': '15:00:00'},
    {'race_name': 'Belgian GP', 'date': '2024-07-28', 'time': '15:00:00'},
    {'race_name': 'Dutch GP', 'date': '2024-08-25', 'time': '15:00:00'},
    {'race_name': 'Italian GP', 'date': '2024-09-01', 'time': '15:00:00'},
    {'race_name': 'Azerbaijan GP', 'date': '2024-09-15', 'time': '15:00:00'},
    {'race_name': 'Singapore GP', 'date': '2024-09-22', 'time': '20:00:00'},
    {'race_name': 'United States GP', 'date': '2024-10-20', 'time': '14:00:00'},
    {'race_name': 'Mexican GP', 'date': '2024-10-27', 'time': '14:00:00'},
    {'race_name': 'Brazilian GP', 'date': '2024-11-03', 'time': '14:00:00'},
    {'race_name': 'Las Vegas GP', 'date': '2024-11-23', 'time': '22:00:00'},
    {'race_name': 'Qatar GP', 'date': '2024-12-01', 'time': '19:00:00'},
    {'race_name': 'Abu Dhabi GP', 'date': '2024-12-08', 'time': '17:00:00'}
]


cursor = connection.cursor()

# Insertar los datos en la tabla `race`
for i, race in enumerate(races_data):
    query = """
    INSERT INTO race (season, round, race_name, circuit_id, date, time)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        '2024',
        i + 1,  # `round`
        race['race_name'],
        i + 1,  # `circuit_id`
        race['date'],
        race['time']
    )
    cursor.execute(query, values)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar la conexión
cursor.close()
connection.close()

print("Datos insertados correctamente en la tabla `race`.")