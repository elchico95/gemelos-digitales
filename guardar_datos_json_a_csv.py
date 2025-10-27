# ####### cuando  es en un directorio 
import json
import csv

def leer_json(ruta_json):
    """Lee un archivo JSON que contiene una lista de diccionarios."""
    try:
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        print("✅ Archivo JSON leído correctamente.")
        return datos
    except Exception as error:
        print("❌ Error al leer el archivo JSON:", error)
        return []

def guardar_csv(datos, ruta_csv):
    """
    Guarda los datos en un archivo CSV, con cada clave como columna.

    Parámetros:
    - datos: lista de diccionarios
    - ruta_csv: ruta del archivo CSV de salida
    """
    try:
        # Obtener todas las claves únicas como columnas
        columnas = sorted({clave for fila in datos for clave in fila})

        with open(ruta_csv, 'w', newline='', encoding='utf-8-sig') as archivo:
            # Puedes cambiar el delimitador a ';' si tu Excel lo requiere
            escritor = csv.DictWriter(archivo, fieldnames=columnas, delimiter=';')
            escritor.writeheader()

            for fila in datos:
                fila_ordenada = {clave: fila.get(clave, "") for clave in columnas}
                escritor.writerow(fila_ordenada)

        print("📁 CSV guardado correctamente en:", ruta_csv)
    except Exception as error:
        print("❌ Error al guardar el archivo CSV:", error)

# Parte principal del programa
if __name__ == "__main__":
    ruta_entrada = "pon aqui el directorio del archivo.json desde donde se va a leer y descargar los datos"
    ruta_salida = "pon aqui el directorio del archivo.csv donde se guardaran los datos"

    datos = leer_json(ruta_entrada)
    if datos:
        guardar_csv(datos, ruta_salida)







# ####### cuando es en una url
import requests
import csv

def leer_json_desde_url(url):
    """Descarga datos JSON desde una URL pública."""
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        print("✅ Datos descargados desde la URL.")
        return datos
    except Exception as error:
        print("❌ Error al descargar los datos:", error)
        return []

def guardar_csv(datos, claves_deseadas, ruta_csv):
    """Guarda los datos en un archivo CSV, con columnas bien separadas."""
    try:
        with open(ruta_csv, 'w', newline='', encoding='utf-8-sig') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=claves_deseadas, delimiter=';')
            escritor.writeheader()
            for fila in datos:
                fila_filtrada = {clave: fila.get(clave, "") for clave in claves_deseadas}
                escritor.writerow(fila_filtrada)
        print("📁 Datos guardados en CSV:", ruta_csv)
    except Exception as error:
        print("❌ Error al guardar el archivo CSV:", error)

# Ejemplo de uso
if __name__ == "__main__":
    url_json = " pon aqui la url del archivo.json leer y descargar los datos"
    claves = ["ciudad", "temperatura"]
    ruta_salida =  "pon aqui el directorio del archivo.csv donde se guardaran los datos"

    datos = leer_json_desde_url(url_json)
    guardar_csv(datos, claves, ruta_salida)
