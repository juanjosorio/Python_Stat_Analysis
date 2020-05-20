#Este es un programa que ayuda a la realización de analisis estadísticos de manera muy rápida
#Se importan todas las librerías quue van a ser usadas durante la ejecución del programa
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics
from math import sqrt
from statistics import median
from tkinter import filedialog
import seaborn as sns
#from Proyecto import Extras
from textwrap import wrap

#Función que crea un letrero de bienvenida bonito

#Creates a line separator thaat can be used to give order to the code
def line_separator():
    print("-"*60)
def conseguir_archivo():
    ''' Función que usa tkinter para extraer el path hacia un archivo
    Parametros:
    ninguno
    Salida:
    path hacia el archivo donde se encuentran los datos '''

    import_file_path = filedialog.askopenfilename()

    return import_file_path
def lista_para_identificar_tipo_de_archivo(x):
    '''Función que recibe el path hacia un archivo, separa la función desde el punto y así el último elemento de la lista es un tipo de archivo
    Parametros:
    x:FilePath
    Salida:
    Tipo de archivo'''

    lista_con_tipo_de_archivo =x.split(".")

    archivo=lista_con_tipo_de_archivo[-1]

    return archivo

def leer_csv(import_file_path):
    '''En caso de que lista_para_identificar_tipo_de_archivo arroje csv, esta función lee el data frame
    Parametros:
    import_file_path:ruta hacia el archivo
    Retorno:
    data: el data frame con el que se realiza el analisis'''

    data = pd.read_csv(import_file_path)

    print (data.head())



    return data
def leer_Excel(import_file_path):

    data = pd.read_excel(import_file_path)

    print (data.head())



    return data

#La función que consigue el input del usuario
def input_usuraio():

    print('''
    -Histograma(puede escribir 1)
    -Box-Plot(2) 
    -Linear Regression(3)
    -Medidas de dispersión(4)
    -Intervalos de confianza(5)
    -Pie Chart(6)
    ''')

    user_input=input("Escriba el nombre del grafico que quiera realizar. Presione enter o escriba 'Terminar' si así lo desea: "+"\n")

    return user_input

#Esta función comprueba que la columna que eligió el usuario existe
def the_column_exists(data,y):

    try:
        print(data[y])
        return True
    except KeyError:
        return False

#La función que crea el histograma
def create_histogram(data):
    data = data.apply(pd.to_numeric, errors="coerce")

    print("Los nombres de las columnas disponibles son los siguientes: ")

    for i in data.columns:
        print('-' + str(i))

    print('\n' + '¿De qué columna deseas realizar el histograma?')

    b = input("(Escribe el nombre del encabezado de la columna): " + "\n")

    while not the_column_exists(data,b):
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
#La función que crea el box-plot
def create_boxplot(data):
    data = data.apply(pd.to_numeric, errors="coerce")

    print('Los nombres de las columnas disponibles son los siguientes: ')

    for i in data.columns:
        print('-' + str(i))

    print('\n' + '¿De qué columna deseas realizar el box-plot?')

    cb = input("(Escribe el nombre del encabezado de la columna): " + "\n")

    while not the_column_exists(data,cb):
        cb = input("Esa columna no aparece registrada, escribe una válida: " + "\n")

    data.boxplot(column=str(cb))

    title = input("Ponle un título a tu box-plot: ")

    x_boxplot = input("Escribe el título para el eje X: ")

    y_boxplot = input("Escribe el título para el eje Y: ")

    plt.title(title)

    plt.xlabel(x_boxplot)

    plt.ylabel(y_boxplot)

    plt.show()



#Función de medidas de dispersión
def medidas_de_dispersion(data):

    data = data.apply(pd.to_numeric, errors="coerce")

    print('Los nombres de las columnas disponibles son los siguientes: ')

    for i in data.columns:
        print('-' + str(i))

    print('\n' + '¿De qué columna deseas realizar las medidas de dispersíon? ')

    columna_nombre = input("(Escribe el nombre del encabezado de la columna): " + "\n")

    while not the_column_exists(data,columna_nombre):
        columna_nombre = input("(Escribe el nombre del encabezado de la columna): " + "\n")
        # Median

    med = median(data[columna_nombre])

    print("Median: " + str(med))

        # Stdev

    stdev = statistics.pstdev(data[columna_nombre])

    print("StDev: " + str(stdev))

        # Variance

    variance = stdev * stdev

    print("Variance: " + str(variance))


#Función de intervalos de confianza
def intervalos_de_confianza(data):

    data = data.apply(pd.to_numeric, errors="coerce")

    print('Los nombres de las columnas disponibles son los siguientes: ')

    for i in data.columns:
        print('-' + str(i))

    print('\n' + '¿De qué columna deseas realizar los intervalos de confianza?')

    columna_nombre = input("(Escribe el nombre del encabezado de la columna): " + "\n")

    while not the_column_exists(data,columna_nombre):
        columna_nombre = input("(Escribe el nombre del encabezado de la columna): " + "\n")

    length_list = len(data[columna_nombre])

    sum_list = sum(data[columna_nombre])

    stdev = statistics.pstdev(data[columna_nombre])

    list_mean = sum_list / length_list
    # confidence90% 1.29

    fr1 = (stdev / sqrt(length_list)) * 1.29

    n1 = list_mean + fr1

    n2 = list_mean - fr1

    print('Confidence interval 90%: ' + "(" + str(n2) + ",", str(n1) + ")")

    # Confidence95% 1.65

    fr2 = (stdev / sqrt(length_list)) * 1.65

    n11 = list_mean + fr2

    n21 = list_mean - fr2

    print('Confidence interval 95%: ' + "(" + str(n21) + ",", str(n11) + ")")

    # Confidence99% 2.33

    fr3 = (stdev / sqrt(length_list)) * 2.33

    n12 = list_mean + fr3

    n22 = list_mean - fr3

    print('Confidence interval 99%: ' + "(" + str(n22) + ",", str(n12) + ")")

#Función que crea regresión lineal
def regresion(data):

    data = data.apply(pd.to_numeric, errors="coerce")

    print("Los nombres de las columnas disponibles son los siguientes: ")

    for i in data.columns:
        print('-' + str(i))

    columna_x = input('Ingrese el nombre de la columna para el eje X: '+'\n')

    while not the_column_exists(data,columna_x):
        columna_x = input("No se encuentra esta columna, escriba una nueva: " + "\n")

    columna_y = input('Ingrese el nombre de la columna para el eje Y: '+'\n')

    while not the_column_exists(data,columna_y):
        columna_y = input("No se encuentra esta columna, escriba una nueva: " + "\n")

    sns.lmplot(x = columna_x, y = columna_y, data = data, line_kws = {'color': 'darkorange'}, scatter_kws = {'color':'dodgerblue'})

    regresion_title = input('Ingrese el título para la gráfica: '+'\n')

    regresion_x_title = input('Ingrese el título para el eje X: '+'\n')

    regresion_y_title = input('Ingrese el título para el eje Y: '+'\n')

    plt.title(regresion_title)
    plt.xlabel(regresion_x_title)
    plt.ylabel(regresion_y_title)

    plt.show()



def pie_chart(data):

    data = data

    print("Los nombres de las columnas disponibles son los siguientes: ")

    for i in data.columns:
        print('-' + str(i))

    nombre_columna = input("Escribe el nombre del encabezado de la columna: "+'\n')

    while not the_column_exists(data,nombre_columna):
        nombre_columna = input("Escribe el nombre del encabezado de la columna: "+'\n')

    data_con_columna = data[nombre_columna]

    index_columna = data_con_columna.value_counts()

    fig1, ax1 = plt.subplots()



    ax1.pie(index_columna, labels= index_columna, shadow = True, startangle= 90)

    ax1.axis('equal')

    plt.legend(list(index_columna.index.values), loc ='best')

    title_pie = input('Ingrese el título del Pie Chart: '+'\n')
    plt.title(title_pie, y=1.08)

    plt.show()




#Lista de las opciones válidas
options = {"Histograma" : create_histogram,
           "1": create_histogram,
           "Box-plot" : create_boxplot,
           "2":create_boxplot,
           "3":regresion,

           "4": medidas_de_dispersion,
           "5": intervalos_de_confianza,
           "Medidas de dispersión": medidas_de_dispersion,
           "Intervalos de confianza": intervalos_de_confianza,
            "6" : pie_chart,
           "Pie Chart" : pie_chart
    }
possible_files = {"csv": leer_csv, "xls": leer_Excel, "xlsx":leer_Excel}



def main():

    #(Extras.welcome_message())
    (line_separator())
    a=conseguir_archivo()
    archivo_a_leer=lista_para_identificar_tipo_de_archivo(a)
    print(archivo_a_leer)
    funcion =  possible_files.get(archivo_a_leer)
    data = (funcion(a))

    while True:
        user_input = input_usuraio()
        option = options.get(user_input, False)
        if not option:
            break
        else:
            option(data)

if __name__ == "__main__":
        main()
