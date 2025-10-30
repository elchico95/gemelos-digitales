import json
import csv

def calcular_media(alumnos):
    """Calcula la nota media de cada alumno y la devuelve como nueva lista"""
    alumnos_con_media = []
    
    for alumno in alumnos:
        notas = alumno["notas"]
        media = sum(notas) / len(notas)

        # Imprimimos la media en consola
        print(f"{alumno['nombre']} {alumno['apellidos']} nota media de {media:.2f}")

        # Creamos un nuevo diccionario solo con los datos que queremos guardar
        alumno_con_media = {
            "id": alumno["id"],
            "nombre": alumno["nombre"],
            "apellidos": alumno["apellidos"],
            "edad": alumno["edad"],
            "nota_media": round(media, 2),
            "faltas": alumno["faltas"],
            "supera": alumno["supera"]
        }

        # Añadimos este diccionario al final de la lista 'alumnos_con_media'.
        # 'append' agrega un solo elemento al final de la lista.
        alumnos_con_media.append(alumno_con_media)
    
    return alumnos_con_media


if __name__ == "__main__":
    # 1️⃣ Leemos el archivo JSON original
    with open("alumnos_json.json", "r", encoding="utf-8") as f:
        alumnos = json.load(f)

    # 2️⃣ Calculamos las medias
    alumnos_con_media = calcular_media(alumnos)

    # 3️⃣ Guardamos los resultados en un CSV
    with open("alumnos_media.csv", "w", newline="", encoding="utf-8") as csvfile:
        columnas = ["id", "nombre", "apellidos", "edad", "nota_media", "faltas", "supera"]
        writer = csv.DictWriter(csvfile, fieldnames=columnas, delimiter=';')
        writer.writeheader()
        writer.writerows(alumnos_con_media)

    print("✅ Resultados guardados correctamente en alumnos_media.csv")
