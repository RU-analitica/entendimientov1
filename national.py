import pandas as pd
import numpy as np

def analysis():

    inputWeek = input("Digita el número de semana: ")
    kind = input('Elige una opción: \n \n 1 - Comercial \n \n 2 - Financiero \n \n Opción: ')

    if(int(inputWeek) < 10):
        inputWeek = f'0{inputWeek}'

    if(kind == '1'):
        file = f'./data/S{inputWeek} Boletín Comercial' '.xlsx'

    elif(kind == '2'):
        file = f'./data/S{inputWeek} Boletín Financiero' '.xlsx'

    else:
        print('\n Opción no válida')
        return

    pd.options.display.float_format = '{:,.1f}'.format

    df = pd.read_excel(file)

    Q1 = df.iloc[:0, 39]
    Q2 = df.iloc[:0, 40]
    Q3 = df.iloc[:0, 41]

    tmpAns1 = df.iloc[:, 39].unique()
    tmpAns2 = df.iloc[:, 40].unique()
    tmpAns3 = df.iloc[:, 41].unique()

    Q1_ans = []
    Q2_ans = []
    Q3_ans = []

    for answer in tmpAns1:
        Q1_ans.append(answer)

    for answer in tmpAns2:
        Q2_ans.append(answer)

    for answer in tmpAns3:
        Q3_ans.append(answer)

    Q1_ans_count = []
    Q2_ans_count = []
    Q3_ans_count = []

    Q1_ans_ans = []
    Q2_ans_ans = []
    Q3_ans_ans = []


    for answer in Q1_ans:
        Q1_ans_ans.append(answer)
        Q1_ans_count.append(df.iloc[:, 39].value_counts()[answer])

    for answer in Q2_ans:
        Q2_ans_ans.append(answer)
        Q2_ans_count.append(df.iloc[:, 40].value_counts()[answer])

    for answer in Q3_ans:
        Q3_ans_ans.append(answer)
        Q3_ans_count.append(df.iloc[:, 41].value_counts()[answer])

    dict1 = dict(zip(Q1_ans_ans, Q1_ans_count))
    dict2 = dict(zip(Q2_ans_ans, Q2_ans_count))
    dict3 = dict(zip(Q3_ans_ans, Q3_ans_count))

    print(dict1)
    print(dict2)
    print(dict3)

    print('\n')

    total_count_answers = sum(Q1_ans_count)

    print('Total count of answers: ', total_count_answers)
    print('\n')

    q1_percents = []
    q2_percents = []
    q3_percents = []

    for number in Q1_ans_count:
        q1_percents.append((number / total_count_answers) * 100)

    for number in Q2_ans_count:
        q2_percents.append((number / total_count_answers) * 100)

    for number in Q3_ans_count:
        q3_percents.append((number / total_count_answers) * 100)

    print(q1_percents)
    print(q2_percents)
    print(q3_percents)

    print('\n')

    df_grouped = df.groupby(['calificacion'])
    print('Pregunta 1: ')
    print(df.iloc[:0, 39])
    print('Respuesta correcta Q1: ')
    print((df_grouped.get_group(10).iloc[:, 39]).unique())

    print('\n')
    print('Pregunta 2: ')
    print(df.iloc[:0, 40])
    print('Respuesta correcta Q2')
    print((df_grouped.get_group(10).iloc[:, 40]).unique())

    print('\n')
    print('Pregunta 3: ')
    print(df.iloc[:0, 41])
    print('Respuesta correcta Q3')
    print((df_grouped.get_group(10).iloc[:, 41]).unique())

    print('\n')
    print('Total aprobados: ', len(df[df['calificacion'] >= 8]))
    print('Porcentaje de aprobados: ', len(df[df['calificacion'] >= 8]) / len(df) * 100)


if __name__ == '__main__':
    analysis()