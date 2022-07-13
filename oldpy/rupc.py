import pandas as pd
import numpy as np

df = pd.read_excel('./Semana 12 - X/S15 Boletín Financiero.xlsx')
df = pd.DataFrame(df)
df = df[df['TERRITORIO'] == 'TERRITORIO RU PACIFICO CENTRO']


pd.options.display.float_format = '{:,.1f}'.format

def analysis():


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
    print('Respuesta correcta Q1: ')
    print((df_grouped.get_group(10).iloc[:, 39]).unique())

    print('\n')
    print('Respuesta correcta Q2')
    print((df_grouped.get_group(10).iloc[:, 40]).unique())

    print('\n')
    print('Respuesta correcta Q3')
    print((df_grouped.get_group(10).iloc[:, 41]).unique())

if __name__ == '__main__':
    analysis()