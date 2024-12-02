import requests
from bs4 import BeautifulSoup

# URL de la página web a scrapear
url = 'https://ejemplo.com'

# Realizar una solicitud GET a la página
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Lista de IDs que queremos extraer
    ids_a_extraer = ['id1', 'id2', 'id3']

    # Crear o abrir el archivo .txt para guardar los datos
    with open('output.txt', 'w', encoding='utf-8') as file:
        for element_id in ids_a_extraer:
            # Buscar el elemento por su ID
            element = soup.find(id=element_id)
            
            if element:
                # Escribir el texto del elemento en el archivo
                file.write(f"ID: {element_id}\n")
                file.write(f"Contenido: {element.get_text(strip=True)}\n")
                file.write("-" * 40 + "\n")
            else:
                file.write(f"ID: {element_id} no encontrado.\n")
                file.write("-" * 40 + "\n")

    print("Extracción completada y guardada en 'output.txt'")
else:
    print(f"Error al acceder a la página: {response.status_code}")