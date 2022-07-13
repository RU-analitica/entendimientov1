import pandas as pd
import numpy as np

week = int(input("Digita el número de semana: "))

df1 = pd.read_excel(f'./data/S{week} Boletín Financiero' '.xlsx')
df2 = pd.read_excel(f'./data/S{week} Boletín Comercial' '.xlsx')
# df3 = pd.read_excel(f'./data/S{week} Boletín de Evaluación' '.xlsx')
# df4 = pd.read_excel(f'./data/S{week} Boletín de Evaluación' '.xlsx')
# df5 = pd.read_excel(f'./data/S{week} Boletín de Evaluación' '.xlsx')
# df6 = pd.read_excel(f'./data/S{week} Boletín de Evaluación' '.xlsx')
# df7 = pd.read_excel(f'./data/S{week} Boletín de Evaluación' '.xlsx')


def meanApp():

    df1_mean = df1['calificacion'].mean()
    df2_mean = df2['calificacion'].mean()
    # df3_mean = df3['calificacion'].mean()
    # df4_mean = df4['calificacion'].mean()
    # df5_mean = df5['calificacion'].mean()
    # df6_mean = df6['calificacion'].mean()
    # df7_mean = df7['calificacion'].mean()

    df1_mean = round(df1_mean)
    df2_mean = round(df2_mean)
    # df3_mean = round(df3_mean)
    # df4_mean = round(df4_mean)
    # df5_mean = round(df5_mean)
    # df6_mean = round(df6_mean)
    # df7_mean = round(df7_mean)

    print(df1_mean)
    print(df2_mean)
    # print(df3_mean)
    # print(df4_mean)
    # print(df5_mean)
    # print(df6_mean)
    # print(df7_mean)

    # average = (df1_mean + df2_mean + df3_mean + df4_mean + df5_mean + df6_mean + df7_mean) / 7
    average = (df1_mean + df2_mean) / 2

    print('Promedio total de calificaciones: ')
    print(average)

if __name__ == '__main__':
    meanApp()