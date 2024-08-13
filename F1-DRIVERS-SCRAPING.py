import requests
from bs4 import BeautifulSoup

url = "https://www.formula1.com/en/drivers"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    drivers = soup.find_all('div', class_="f1-inner-wrapper flex flex-col gap-micro text-brand-black")
    
    # Encuentra todos los divs que contienen los nombres de los pilotos
    driver_name_divs = soup.find_all('div', class_="flex gap-xxs flex-col f1-driver-name")
    
    for div in driver_name_divs:
        first_name = div.find_all('p')[0].text.strip()
        last_name = div.find_all('p')[1].text.strip()
        full_name = f"{first_name} {last_name}"
        print(full_name)
else:
    print("Error al cargar la web, codigo:", response.status_code)