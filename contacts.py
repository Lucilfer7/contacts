import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Configuración de la API de Google Contacts
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']
API_SERVICE_NAME = 'people'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = 'client_secret.json'  # Necesitas descargar este archivo desde la Consola de Desarrolladores de Google

# Directorio donde se guardará el archivo de texto con los números de teléfono
OUTPUT_DIR = 'output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Función para autenticarse y obtener el servicio de Google Contacts
def authenticate_and_get_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    return service

# Función para obtener y guardar los números de teléfono en un archivo de texto
def save_phone_numbers(service):
    results = service.people().connections().list(resourceName='people/me', personFields='names,phoneNumbers').execute()
    connections = results.get('connections', [])

    phone_numbers = []
    for person in connections:
        names = person.get('names', [])
        phone_numbers.extend([(name['displayName'], phone['value']) for name in names for phone in person.get('phoneNumbers', [])])

    # Guardar los números de teléfono en un archivo de texto
    output_file_path = os.path.join(OUTPUT_DIR, 'phone_numbers.txt')
    with open(output_file_path, 'w') as f:
        for name, phone_number in phone_numbers:
            f.write(f"{name}: {phone_number}\n")

    print(f"Números de teléfono guardados en {output_file_path}")

# Autenticarse y obtener el servicio
service = authenticate_and_get_service()

# Obtener y guardar los números de teléfono
save_phone_numbers(service)
