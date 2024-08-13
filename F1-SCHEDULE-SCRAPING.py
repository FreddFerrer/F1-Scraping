import datetime
import requests
from bs4 import BeautifulSoup

# URL de la página web
url = 'https://www.autosport.com/f1/schedule/2024/'

def parse_datetime(date_str, time_str):
    # Definir el formato de la fecha y hora
    date_format = "%d %b"  # Día y mes
    time_format = "%H:%M"  # Hora y minuto
    
    # Crear un objeto datetime a partir de la fecha y hora
    event_datetime_str = f"{date_str} {time_str}"
    try:
        event_datetime = datetime.datetime.strptime(event_datetime_str, f"{date_format} {time_format}")
    except ValueError:
        return None
    
    # Ajustar el año a 2024
    event_datetime = event_datetime.replace(year=2024)
    
    return event_datetime

def get_next_race(races):
    # Obtener la fecha y hora actual
    now = datetime.datetime.now()
    
    # Encontrar el próximo evento
    next_race = None
    for race in races:
        if race['race_date_time'] > now:
            if not next_race or race['race_date_time'] < next_race['race_date_time']:
                next_race = race
    
    return next_race

# Realizar la solicitud GET a la URL
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar todos los elementos de la tabla de horario
    schedule = soup.find_all('tbody', class_="ms-schedule-table__item")
    
    if schedule:
        races = []
        
        for race in schedule:
            # Obtener el nombre del evento
            race_name = race.select_one('.ms-schedule-table-item-main__event a span').text.strip()

            # Obtener la fecha en formato 'local'
            race_date = race.select_one('.ms-schedule-table-date--local span').text.strip()
            
            # Obtener la hora en formato 'local'
            race_time = race.select_one('.ms-schedule-table__time .ms-schedule-table-date--local').text.strip()

            # Parsear fecha y hora
            race_datetime = parse_datetime(race_date, race_time)
                
            if race_datetime:
                races.append({
                    'race': race_name,
                    'race_date_time': race_datetime
                })
        
        # Mostrar los resultados extraídos
        print("Lista completa de carreras:")
        for race in races:
            print(f"Carrera: {race['race']} - Fecha y Hora: {race['race_date_time']}")
        
        # Encontrar y mostrar el próximo evento
        next_race = get_next_race(races)
        if next_race:
            print(f"\nLa próxima carrera es: {next_race['race']} - Fecha y Hora: {next_race['race_date_time']}")
        else:
            print("\nNo hay eventos futuros.")
    else:
        print("No se encontraron carreras en la página.")
else:
    print(f"Error al acceder a la URL: {response.status_code}")
