import requests
from bs4 import BeautifulSoup
import re

url = "https://www.formula1.com/en/results/2024/drivers"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    drivers_table = soup.find('tbody')  # Obtenemos el primer 'tbody' que contiene la lista de pilotos

    if drivers_table:
        # Crear una lista para almacenar la información de los pilotos
        drivers_data = []

        # Recorremos cada fila dentro del 'tbody'
        for row in drivers_table.find_all('tr'):
            # Extraemos las celdas (columnas) dentro de la fila
            columns = row.find_all('td')
            
            # Asignamos los valores de cada columna a las variables correspondientes
            driver_position = columns[0].text.strip()  # Posición
            
            driver_name = columns[1].text.strip().replace('\xa0', ' ')
            driver_nationality = columns[2].text.strip()  # Nacionalidad
            driver_team = columns[3].text.strip()  # Equipo
            driver_pts = columns[4].text.strip()  # Puntos

            # Eliminar las últimas 3 letras del nombre si parecen ser una abreviatura
            if len(driver_name) > 3:
                driver_name = driver_name[:-3].strip()
            
            # Almacenar la información en un diccionario
            driver_info = {
                'Position': driver_position,
                'Name': driver_name,
                'Nationality': driver_nationality,
                'Team': driver_team,
                'Points': driver_pts
            }
            
            # Agregamos el diccionario a la lista de datos de los pilotos
            drivers_data.append(driver_info)
    
    # Imprimir la información extraída
    for driver in drivers_data:
        print(driver)
else:
    print("Error al cargar la web, código:", response.status_code)