import json
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

# 1. Carga de un archivo JSON:
#
# json de github
#
#    - Solicitar al usuario que ingrese la ruta del archivo JSON que desea cargar.
#
#    - Utilizar la biblioteca `json` de Python para cargar el archivo JSON.

def cargar_json(ruta):
    with open(ruta, 'r') as archivo:
        datos = json.load(archivo)
    return datos

#print(cargar_json("Productos.json"))

#
#
# 2. Operaciones CRUD:
#
#    - Permitir al usuario realizar las siguientes operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en los datos cargados desde el archivo JSON:
#
#      - Crear: Agregar nuevos registros al archivo JSON.
#
#      - Leer: Mostrar los registros actuales del archivo JSON.
#
#      - Actualizar: Modificar los registros existentes en el archivo JSON.
#
#      - Eliminar: Eliminar registros del archivo JSON.

# Función para guardar datos en un archivo JSON
def guardar_json(datos, ruta):
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Funciones CRUD
def crear_registro(datos, nuevo_registro):
    datos.append(nuevo_registro)
    return datos

def leer_registros(datos):
    for registro in datos: #bucle con un for...in
        print(registro)
        print("-----------------------------------------------------")

def actualizar_registro(datos, indice, nuevo_registro):
    datos[indice] = nuevo_registro
    return datos

def eliminar_registro(datos, indice):
    print(indice)
    print(datos[indice])
    del datos[indice]
    return datos


#
#
# 3. Limpieza y ordenación de datos:
#
#    - Implementar funciones para limpiar y ordenar los datos cargados desde el archivo JSON:
#
#      - Limpieza: Eliminar datos duplicados o inconsistentes.
#
#      - Ordenación: Ordenar los datos según algún criterio, como por ejemplo, orden alfabético o numérico.
#
#
#
# 4. Visualización de datos:
#
#    - Utilizar tres librerías diferentes para mostrar gráficos basados en los datos cargados y procesados:
#
#      1. Grafico de barras con Matplotlib: Mostrar una visualización de los datos en forma de gráfico de barras.
#
#      2. Diagrama de dispersión con Seaborn: Mostrar una visualización de los datos en forma de diagrama de dispersión.
#
#      3. Gráfico circular con Plotly: Mostrar una visualización de los datos en forma de gráfico circular.





# Funciones de limpieza y ordenación
def limpiar_datos(datos):
    conjunto=list(set(datos))
    #convertir un dict a set y mostrarlo como una list --- duda
    return conjunto  # Eliminar duplicados

def ordenar_datos(datos):
    return sorted(datos)

# Función para mostrar gráfico de barras con Matplotlib
def mostrar_grafico_barras(datos):
    valores = [registro['valor'] for registro in datos]
    etiquetas = [registro['etiqueta'] for registro in datos]
    plt.bar(etiquetas, valores)
    plt.xlabel('Etiquetas')
    plt.ylabel('Valores')
    plt.title('Gráfico de Barras')
    plt.show()

# Función para mostrar diagrama de dispersión con Seaborn
def mostrar_diagrama_dispersion(datos):
    df = pd.DataFrame(datos)
    sns.scatterplot(data=df, x='nombre', y='cantidad')
    plt.xlabel('Nombre de producto')
    plt.ylabel('Unidades')
    plt.title('Diagrama de Dispersión')
    plt.show()

# Función para mostrar gráfico circular con Plotly
def mostrar_grafico_circular(datos):
    df = pd.DataFrame(datos)
    fig = px.pie(df, values='valor', names='etiqueta', title='Gráfico Circular')
    fig.show()

# Ejemplo de uso
if __name__ == "__main__":
#Cargar datos desde un archivo JSON
    ruta_archivo = input("Ingrese la ruta del archivo JSON: ")
    datos = cargar_json(ruta_archivo)
    #print(datos)
#
#     # Operaciones CRUD
#     # Crear un nuevo registro
    nuevo_registro = {
        "id": 100,
        "nombre": "pan de horno",
        "cantidad": "50",
        "descripcion": "pan super bueno",
        "precio": "$12.00",
        "imagen": "img/Pan del horno.png"
    }
    #datos = crear_registro(datos, nuevo_registro)
    #print(datos)
    #guardar_json(datos, ruta_archivo)
#
#     # Leer registros
    print("Registros actuales:")
    leer_registros(datos)
#
#     # Actualizar un registro
    #indice_actualizar = int(input("Ingrese el índice del registro a actualizar: "))
    #nuevo_valor = int(input("Ingrese el nuevo valor de unidades: "))
    #datos = actualizar_registro(datos, indice_actualizar, {'cantidad': nuevo_valor})
    #guardar_json(datos, ruta_archivo)
#
#     # Eliminar un registro
    #indice_eliminar = int(input("Ingrese el índice del registro a eliminar: "))
    #datos = eliminar_registro(datos, indice_eliminar)
    #guardar_json(datos, ruta_archivo)
#
#     # Limpieza y ordenación de datos
    datos_limpios = limpiar_datos(datos)
    print(datos_limpios)
    #datos_ordenados = ordenar_datos(datos)
    #print(datos_ordenados)
#
#     # Visualización de datos
#     # Gráfico de barras con Matplotlib
#     mostrar_grafico_barras(datos_ordenados)
#
#     # Diagrama de dispersión con Seaborn
    #mostrar_diagrama_dispersion(datos)
#
#     # Gráfico circular con Plotly
#     mostrar_grafico_circular(datos_ordenados)
