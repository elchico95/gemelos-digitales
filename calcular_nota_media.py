# calcular_media.py
import json

def calcular_media(alumnos):
    """Calcula e imprime la nota media de cada alumno"""
    for alumno in alumnos:
        notas = alumno["notas"]
        media = sum(notas) / len(notas)
        print(f"{alumno['nombre']} {alumno['apellidos']} nota media de {media:.2f}")

#.2f → indica que queremos mostrar el número con 2 decimales en formato float (número con decimales). EJEPMLO:
""" media = 9.75678
print(f"La nota media es {media:.2f}") """

if __name__ == "__main__":
    # Abrimos el archivo JSON con los datos de los alumnos
    with open("alumnos_json.json", "r", encoding="utf-8") as f:
        alumnos = json.load(f)

    # Llamamos a la función
    calcular_media(alumnos)



#  ####       EXPLICACION DE LA FUNCIÓN     ##################


# alumnos → es toda la clase, todos los registros de alumnos.
# alumno → cada diccionario individual dentro de esa lista, mientras el bucle recorre todos los alumnos uno por uno.
# import json → permite leer y manejar archivos .json.
# with open(..., "r", encoding="utf-8") → abre el archivo JSON en modo lectura.
# json.load(f) → convierte el contenido JSON en una lista/diccionario de Python.
# calcular_media(alumnos) → llama a la función para mostrar la media de cada alumno.

