import pandas as pd
import numpy as np
import warnings

warnings.simplefilter("ignore")

print('----------------------------------------------------- \n')
print('Análisis de entendimiento semanal. \n \n')
print('Instrucciones: \n \n')
print('1. Asegúrate de que el archivo que deseas analizar esté en la carpeta data. \n')
print('2. El archivo deberá tener el nombre de la semana y el tipo de comunicado con el fin de dar un orden a los datos. \n')
print('3. El archivo deberá tener la extensión .xlsx \n')
print('4. Copia solo el nombre del archivo sin extensión y pegalo en la terminal cuando te sea requerido')
print('----------------------------------------------------- \n')

doc = str(input('Escribe el nombre del documento: '))
file = f'./data/{doc}.xlsx'

pd.options.display.float_format = '{:,.1f}'.format

if (file):
    df = pd.read_excel(file)

    # Dropna from 'calificacion'
    df.dropna(subset=['calificacion'], inplace=True)

    # Dropna from last question
    df.dropna(subset=df.iloc[:0, 40], inplace=True)

    df = df[df['estatus_asignacion'] == 'REALIZADA']

    df_grouped = df.groupby(['calificacion'])

    df.fillna(1, inplace=True)

    # Questions
    Q1 = df.iloc[:0, 38]
    Q2 = df.iloc[:0, 39]
    Q3 = df.iloc[:0, 40]
    Q4 = df.iloc[:0, 41]

    # Correct answers
    correct_answer_1 = df_grouped.get_group(10).iloc[:, 38].unique()
    correct_answer_2 = df_grouped.get_group(10).iloc[:, 39].unique()
    correct_answer_3 = df_grouped.get_group(10).iloc[:, 40].unique()
    correct_answer_4 = df_grouped.get_group(10).iloc[:, 41].unique()

    df_len = len(df)

    # Count the number of correct answers
    correct_answer_1_count = []
    correct_answer_2_count = []
    correct_answer_3_count = []
    correct_answer_4_count = []

    for answer in correct_answer_1:
        correct_answer_1_count.append(df.iloc[:, 38].value_counts()[answer])

    for answer in correct_answer_2:
        correct_answer_2_count.append(df.iloc[:, 39].value_counts()[answer])

    for answer in correct_answer_3:
        correct_answer_3_count.append(df.iloc[:, 40].value_counts()[answer])

    for answer in correct_answer_4:
        correct_answer_4_count.append(df.iloc[:, 41].value_counts()[answer])


    # Average of correct answers
    correct_answer1_avg = ((correct_answer_1_count[0] / df_len) * 100).round(1)
    correct_answer2_avg = ((correct_answer_2_count[0] / df_len) * 100).round(1)
    correct_answer3_avg = ((correct_answer_3_count[0] / df_len) * 100).round(1)
    correct_answer4_avg = ((correct_answer_4_count[0] / df_len) * 100).round(1)

    # Average of califications
    calification_avg = df['calificacion'].mean().round(1)
    understanding_avg = (calification_avg * 10).round(2)


    print('----------------------------------------------------- \n')
    print('Entendimiento \n')
    print(f' Calificación promedio: {calification_avg}')
    print(f' % Entendimiento: {understanding_avg}%')
    print('----------------------------------------------------- \n \n')
    print('Análisis de preguntas \n')
    print(f'Pregunta 1: {Q1}')
    print(f'Respuesta correcta: {correct_answer_1}')
    print(f'Porcentaje de personas que respondieron correctamente esta pregunta: {correct_answer1_avg}%\n')
    print(f'Pregunta 2: {Q2}')
    print(f'Respuesta correcta: {correct_answer_2}')
    print(f'Porcentaje de personas que respondieron correctamente esta pregunta: {correct_answer2_avg}% \n')
    print(f'Pregunta 3: {Q3}')
    print(f'Respuesta correcta: {correct_answer_3}')
    print(f'Porcentaje de personas que respondieron correctamente esta pregunta: {correct_answer3_avg}%')
    print('----------------------------------------------------- \n ')
    print('En caso de existir una pregunta 4, a continuación los resultados, si no, ignora las próximas líneas. \n')
    print(f'Pregunta 4: {Q4}')
    print(f'Respuesta correcta: {correct_answer_4}')
    print(f'Porcentaje de personas que respondieron correctamente esta pregunta: {correct_answer4_avg}%')
    print('----------------------------------------------------- \n \n')

else:
    print('\n Ingrese un nombre de archivo válido')
