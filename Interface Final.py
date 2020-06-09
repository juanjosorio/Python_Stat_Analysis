def welcome_message():

    '''Es una función que crea un letrero de bienvenida acogedor
    Parametros:
    ninguno
    Salida:
    Una impresión'''

    print('''

    ░█──░█ █▀▀ █── █▀▀ █▀▀█ █▀▄▀█ █▀▀ 
    ░█░█░█ █▀▀ █── █── █──█ █─▀─█ █▀▀ 
    ░█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀───▀ ▀▀▀
    ''')

# Este es un programa que ayuda a la realización de analisis estadísticos de manera rápida

# Se importan todas las librerías que van a ser usadas durante la ejecución del programa

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics
from statistics import median
from tkinter import filedialog
import seaborn as sns
import os.path
import sys
from scipy.stats import sem, t
from xlrd import XLRDError
# from Proyecto import Extras
from textwrap import wrap



# Función que crea un letrero de bienvenida bonito

# Creates a line separator that can be used to give order to the code

def line_separator():
    print("-" * 60)

def conseguir_archivo():

    ''' Función que usa tkinter para extraer el path hacia un archivo
    Parametros:
    ninguno
    Salida:
    path hacia el archivo donde se encuentran los datos '''


    #En una ventana le permite al usuario escoger el archivo que quiere

    #Con "filetypes" se filtran todos los archivos que no sean de excel o CSV

    import_file_path = filedialog.askopenfilename(
        filetypes=[('Excel and CSV Files', '*.csv',), ('Excel and CSV Files', '*.xlsx'),
                   ('Excel and CSV Files', '*.xls')])



    #Se verifica que exista el archivo
    if len(import_file_path) == 0:
        sys.exit()
    print (import_file_path)

    #Regresa el "camino" del archivo"
    return import_file_path


def lista_para_identificar_tipo_de_archivo(x):

    '''Función que recibe el path hacia un archivo, separa la función desde el punto y así el último elemento de la lista es un tipo de archivo
    Parametros:
    x:FilePath
    Salida:
    archivo:Tipo de archivo'''

    lista_con_tipo_de_archivo = x.split(".")

    archivo = lista_con_tipo_de_archivo[-1]

    return archivo




def leer_csv(import_file_path):

    '''En caso de que lista_para_identificar_tipo_de_archivo arroje csv, esta función lee el data frame
    Parametros:
    import_file_path:ruta hacia el archivo
    Retorno:
    data: el data frame con el que se realiza el analisis'''



    data = pd.read_csv(import_file_path)

    print(data.head())

    return data

def la_hoja_existe(import_file_path,nombre_sheet):
    try:
        pd.read_excel(import_file_path, sheet_name=nombre_sheet)
        return True
    except XLRDError:
        return False

def leer_Excel(import_file_path):
    '''En caso de que lista_para_identificar_tipo_de_archivo arroje .xlsx, est función lee el data frame
        Parametros:
        import_file_path:ruta hacia el arhcivo
        Retorno:
        data: el data frame con el que se realiza el analisis'''
    xls = pd.ExcelFile(import_file_path)
    sheets = xls.sheet_names
    lenght = len(sheets)
    if lenght== 1:
        data = pd.read_excel(import_file_path)
        print(data.head())
        return data
    else:
        for i in range(lenght):

            print("-"+sheets[i])
        nombre_sheet = input('Arriba aparecen las hojas de cálculo registradas, ingrese el nombre de la hoja de cálculo donde se encuentren los datos que desee graficar: ' + '\n')
        while not la_hoja_existe(import_file_path,nombre_sheet):
            nombre_sheet = input(
                'Arriba aparecen las hojas de cálculo registradas, ingrese el nombre de la hoja de cálculo donde se encuentren los datos que desee graficar: ' + '\n')
        data = pd.read_excel(import_file_path, sheet_name=nombre_sheet)

        print(data.head())

        return data


# La función que consigue el input del usuario
def input_usuario():


    ''' La función le presnta al usuario los posibles gráficos que puede hacer y un número que corresponde a dicho gráfico
    Parámetros:
    ninguno
    Retorno:
    el nombre, o el número del gráfico que el usuario desea realizar'''


    print('''
    -Histograma (puede escribir 1)
    -Box-Plot (2) 
    -Regresión Lineal (3)
    -Medidas de dispersión (4)
    -Intervalos de confianza (5)
    -Pie Chart Contados (6)
    -Pie Chart Porcentaje (7)
    -Violin Plots (8)
    ''')

    user_input = input(
        "Escriba el nombre del grafico que quiere realizar. Presione enter o escriba 'Terminar' si así lo desea: " + "\n")

    return user_input


# Esta función comprueba que la columna que eligió el usuario existe
def the_column_exists(data, y):
    ''' Función que verifica si el nombre de la columna elegida por el usuario existe.
    Parámetros:
    Data: el data frame sobre el que se hará la verificación
    y: el nombre de la columna que se verificará si existe
    Retorno:
    Booleana acerca de si la colmna existe o no'''

    try:
        print(data[y])
        return True
    except KeyError:
        return False


# La función que crea el histograma
def create_histogram(data):
    '''
    Función que, usando librerías, crea un histograma de la columna dentro de un set de datos que el usuario desee.
    Parámetros:
    data: el set de datos donde está contenida la columna que el usuario desee graficar
    Retorno:
    Gráfica de tipo histograma
    '''

    data = data.apply(pd.to_numeric, errors="coerce")

    print("Los nombres de las columnas disponibles son los siguientes: ")

    for i in data.columns:
        print('-' + str(i))

    print('\n' + '¿De qué columna deseas realizar el histograma?')

    b = input("(Escribe el nombre del encabezado de la columna): " + "\n")

    while not the_column_exists(data, b):
        b = input("Esa columna no aparece registrada, escribe una válida: " + "\n")

    row_to_do_hisogram_of = data[b].apply(pd.to_numeric, errors="coerce")

    data_ignoringNa = row_to_do_hisogram_of.dropna()

    plt.hist(data_ignoringNa)

    title = input("Ponle un título a tu histograma: ")

    x_histo = input('Escriba el título del eje X: ')

    y_histo = input("Escriba el título para el eje Y: ")

    plt.title(title)

    plt.xlabel(x_histo)

    plt.ylabel(y_histo)

    plt.show()


# La función que crea el box-plot
def create_boxplot(data):
    data = data.apply(pd.to_numeric, errors="coerce")

    print('Los nombres de las columnas disponibles son los siguientes: ')

    for i in data.columns:
        print('-' + str(i))

    print('\n' + '¿De qué columna deseas realizar el box-plot?')

    cb = input("(Escribe el nombre del encabezado de la columna): " + "\n")

    while not the_column_exists(data, cb):
        cb = input("Esa columna no aparece registrada, escribe una válida: " + "\n")

    data.boxplot(column=str(cb))

    title = input("Ponle un título a tu box-plot: ")

    x_boxplot = input("Escribe el título para el eje X: ")

    y_boxplot = input("Escribe el título para el eje Y: ")

    plt.title(title)

    plt.xlabel(x_boxplot)

    plt.ylabel(y_boxplot)

    plt.show()


# Función de medidas de dispersión
def medidas_de_dispersion(data):
    data = data.apply(pd.to_numeric, errors="coerce")
    #datas = data.dropna
    datas = data

    # Permite que el usuario escoja la columna que desea utilizar
    print('Los nombres de las columnas disponibles son los siguientes: ')

    for i in data.columns:
        print('-' + str(i))

    print('\n' + '¿De qué columna deseas realizar las medidas de dispersíon? ')

    columna_nombre = input("(Escribe el nombre del encabezado de la columna): " + "\n")

    while not the_column_exists(data, columna_nombre):
        columna_nombre = input("(Escribe el nombre del encabezado de la columna): " + "\n")
    if len(data[columna_nombre]) == 0:
        return print ("La columna seleccionada no registra números")

    # Cálculo de la Stdev
    stdev = statistics.pstdev(datas[columna_nombre])

    print("StDev: " + str(stdev))

    # Cálculo de la Varianza
    variance = stdev * stdev

    print("Variance: " + str(variance))

    # Cálculo de la media
    length_list = len(datas[columna_nombre])
    sum_list = sum(datas[columna_nombre])
    mean = sum_list / length_list
    print("Mean: " + str(mean))

    # Cálculo de la mediana
    med = median(datas[columna_nombre])

    print("Median: " + str(med))

    #Cálculo de la Moda
    print("Mode: " + str(statistics.mode(datas[columna_nombre])))


    #Cálculo del Min
    print("Min: " + str(min(datas[columna_nombre])))

    #Cálculo del Max
    print("Max: " + str(max(datas[columna_nombre])))












# Función de intervalos de confianza
def intervalos_de_confianza(data):
    datas = data.apply(pd.to_numeric, errors="coerce")
    data=datas
    #data=datas.dropna()

    # Permite que el usuario escoja la columna que desea utilizar
    print('Los nombres de las columnas disponibles son los siguientes: ')

    for i in data.columns:
        print('-' + str(i))

    print('\n' + '¿De qué columna deseas realizar los intervalos de confianza?')

    columna_nombre = input("(Escribe el nombre del encabezado de la columna): " + "\n")

    while not the_column_exists(data, columna_nombre):
        columna_nombre = input("(Escribe el nombre del encabezado de la columna): " + "\n")

    # cálculo de la media
    length_list = len(data[columna_nombre])
    if length_list == 0:
        return print("La columna no registra datos")
    sum_list = sum(data[columna_nombre])
    list_mean = sum_list / length_list

    # Usuario escoge el porcentaje que necesita trabajar
    percentile = float(input("Inserte el porcentaje que desea para el intervalo(En forma decimal): "+'\n'))
    while percentile > 1:
        percentile = float(input("Inserte el porcentaje que desea para el intervalo(En forma decimal): "+'\n'))
    while percentile < 0:
        percentile = float(input("Inserte el porcentaje que desea para el intervalo(En forma decimal): "+'\n'))
    # Cálculo de el intervalo
    std_err = sem(data[columna_nombre])
    variable1 = std_err * t.ppf((1 + percentile) / 2, length_list - 1)
    first_value = list_mean - variable1
    second_value = list_mean + variable1
    percentage =percentile*100
    print(" ")
    print("Confidence Interval of" + " " + str(percentage) + "%: (" + str(first_value) + ",", str(second_value) + ")")


# Función que crea regresión lineal
def regresion(data):

    """
    La función le permite al usuario elegir las columnas para el eje X y Y, de tal forma que se traza un gráfico de
    Regresión Lineal usando la librería "Seaborn"


    Dentro de la función se puede ver qué ocurre en cada paso con comentarios en azul

    :param data:
    :return:
    """

    #coge la base de datos
    data = data.apply(pd.to_numeric, errors="coerce")

    print("Los nombres de las columnas disponibles son los siguientes: ")

    #imprime el nombre de las columnas disponibles
    for i in data.columns:
        print('-' + str(i))

    #El usuario ingresa el nombre de la columna que va en el eje X

    columna_x = input('Ingrese el nombre de la columna para el eje X: ' + '\n')


    #Se revisa que exista la columna, si no existe le pide al usuario que vuelva a ingresar el nombre

    while not the_column_exists(data, columna_x):
        columna_x = input("No se encuentra esta columna, escriba una nueva: " + "\n")


    #Se repite el proceso con el eje Y

    columna_y = input('Ingrese el nombre de la columna para el eje Y: ' + '\n')

    while not the_column_exists(data, columna_y):
        columna_y = input("No se encuentra esta columna, escriba una nueva: " + "\n")


    #se traza el gráfico

    sns.lmplot(x=columna_x, y=columna_y, data=data, line_kws={'color': 'darkorange'},
               scatter_kws={'color': 'dodgerblue'})

    #Ingresos del usuario para los títulos
    regresion_title = input('Ingrese el título para la gráfica: ' + '\n')

    regresion_x_title = input('Ingrese el título para el eje X: ' + '\n')

    regresion_y_title = input('Ingrese el título para el eje Y: ' + '\n')


    #título  central
    plt.title(regresion_title)

    #título para el eje x
    plt.xlabel(regresion_x_title)


    #título para el eje y
    plt.ylabel(regresion_y_title)

    #se muestra el gráfico
    plt.show()


def pie_chart_raw_data(data):

    """
    La función le permite al usuario crear un Pie Chart de la columna que ingrese. La función cuenta las veces que se
    repite un valor dentro de la columna, y se crea el gráfico usando la librería de "Matplotlib"

    Dentro de la función se puede ver qué ocurre en cada paso con comentarios en azul


    :param data:
    :return:
    """


    #Imprime las columnas disponibles

    print("Los nombres de las columnas disponibles son los siguientes: ")


    for i in data.columns:
        print('-' + str(i))

    #El usuario ingresa el nombre de la columna

    nombre_columna = input("Escribe el nombre del encabezado de la columna: " + '\n')

    #El programa revisa si el la columna existe

    while not the_column_exists(data, nombre_columna):
        nombre_columna = input("Escribe el nombre del encabezado de la columna: " + '\n')


    #Se filtra la base de datos dentro de una nueva variable conteniendo únicamente la columna

    data_con_columna = data[nombre_columna]

    #Crea un índice que equivale a la cantidad de valores en la columna

    index_columna = data_con_columna.value_counts()

    #Se trazan los subtramas de el gráfico
    fig1, ax1 = plt.subplots()

    #El programa ingresa el contenido del gráfico
    ax1.pie(index_columna, labels=index_columna, shadow=True, startangle=90)

    #Se determina el eje del gráfico, siendo un círculo
    ax1.axis('equal')

    #Se traza la leyenda del gráfico
    plt.legend(list(index_columna.index.values), loc='best')


    #El usuario ingresa el título del gráfico

    title_pie = input('Ingrese el título del Pie Chart: ' + '\n')
    plt.title(title_pie, y=1.08)

    #El programa muestra el gráfico
    plt.show()

def pie_chart_con_datos_contados(data):
    '''Pie chart que se utiliza sobre un set de datos en los que los datos con una misma característica ya fueron integrados
    Parámetros:
    data: el set de datos sobre el que se hará el pie chart( en este caso tiene que cumplir con lo descrito anteriormente si se
    quieren resultados óptimos
    Retorno:
    grafica: una gráfica de estilo pie'''

    #link
    #https://matplotlib.org/3.2.1/gallery/pie_and_polar_charts/pie_features.html

    print("Los nombres de las columnas disponibles son los siguientes: ")
    for i in data.columns:
        print('-' + str(i))
    a = input("Escribe el nombre del encabezado de la columna: "+'\n')
    while not the_column_exists(data,a):
        a = input("Escribe el nombre del encabezado de la columna: "+'\n')
    b = input("Escriba el nombre de la columna donde se encuentre el índice de los datos: "+'\n')
    while not the_column_exists(data, b):
        b = input("Escriba el nombre de la columna donde se encuentre el índice de los datos: "+'\n')
    columns = data.dropna()
    data_withoutNa = data[a].dropna()
    labels = data[b].tolist()
    title=input("Escriba el titulo de la gráfica: "+'\n')
    if len(labels) != len(columns):
        fig1, ax1 = plt.subplots()
        ax1.pie(data_withoutNa,
                shadow=True, startangle=90, autopct='%1.1f%%')
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.legend(labels)
        plt.title(title, wrap=True)
        plt.show()
    elif len(labels) == len(columns):
        fig1, ax1 = plt.subplots()
        ax1.pie(data[a],
            shadow=True, startangle=90, autopct='%1.1f%%')
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.legend(labels)
        plt.title(title, wrap=True)
        plt.show()


def violin_plot(data):

    #Coge la base de datos
    data = data.apply(pd.to_numeric, errors='coerce')


    #Imprime las columnas disponibles

    print('El nombre de las columnas disponibles es el siguiente: ' + '\n')

    for i in data.columns:
        print('-' + str(i))

    #El usuario ingresa el nombre de la columna para el eje x del gráfico
    x_axis_column = input('Escriba el nombre de la columna para el realizar el Violin Plot ' + '\n')

    #El programa revisa que la columna exista

    while not the_column_exists(data, x_axis_column):
        x_axis_column = input("No se encuentra esta columna, escriba una nueva: " + "\n")



    #Se traza el gráfico
    sns.violinplot(x=data[x_axis_column], data=data, inner='quartile', color='lightblue')

    #El usuario ingresa el título central
    plt.title(input('Ingrese e título para la gráfica: ' + '\n'))

    #EL usuario ingresa el título para el eje Y
    plt.xlabel(input('Ingrese el título para el eje X: ' + '\n'))

    #El programa muestra el gráfico
    plt.show()


# Lista de las opciones válidas
options = {"Histograma": create_histogram,
           "1": create_histogram,
           "Box-plot": create_boxplot,
           "2": create_boxplot,
           "3": regresion,

           "4": medidas_de_dispersion,
           "5": intervalos_de_confianza,
           "Medidas de dispersión": medidas_de_dispersion,
           "Intervalos de confianza": intervalos_de_confianza,
           "6": pie_chart_raw_data,
           "Pie Chart Raw Data": pie_chart_raw_data,
           "7":pie_chart_con_datos_contados,
           "Pie Chart Data Contada":pie_chart_con_datos_contados,
           '8': violin_plot,
           'Violin Plot': violin_plot
           }

#Los archivos que el programa puede leer

possible_files = {"csv": leer_csv, "xls": leer_Excel, "xlsx": leer_Excel}


def main():
    (welcome_message())
    (line_separator())
    a = conseguir_archivo()
    archivo_a_leer = lista_para_identificar_tipo_de_archivo(a)
    print(archivo_a_leer)
    funcion = possible_files.get(archivo_a_leer)
    data = (funcion(a))

    while True:
        user_input = input_usuario()
        option = options.get(user_input, False)
        if not option:
            break
        else:
            option(data)


if __name__ == "__main__":
    main()
