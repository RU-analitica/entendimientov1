import pandas as pd
import numpy as np

file1 = pd.read_excel('./Semana 1 - 7/S01 Boletín Comercial.xlsx')
file2 = pd.read_excel('./Semana 1 - 7/S01 Boletín Financiero.xlsx')
file3 = pd.read_excel('./Semana 1 - 7/S02 Boletín Comercial.xlsx')
file4 = pd.read_excel('./Semana 1 - 7/S02 Boletín Financiero.xlsx')
file5 = pd.read_excel('./Semana 1 - 7/S03 Boletín Comercial.xlsx')
file6 = pd.read_excel('./Semana 1 - 7/S03 Boletín Financiero.xlsx')
file7 = pd.read_excel('./Semana 1 - 7/S04 Boletín Comercial.xlsx')
file8 = pd.read_excel('./Semana 1 - 7/S04 Boletín Financiero.xlsx')
file9 = pd.read_excel('./Semana 1 - 7/S05 Boletín Comercial.xlsx')
file10 = pd.read_excel('./Semana 1 - 7/S05 Boletín Financiero.xlsx')
file11 = pd.read_excel('./Semana 1 - 7/S06 Boletín Comercial.xlsx')
file12 = pd.read_excel('./Semana 1 - 7/S06 Boletín Financiero.xlsx')
file13 = pd.read_excel('./Semana 1 - 7/S07 Boletín Comercial.xlsx')
file14 = pd.read_excel('./Semana 1 - 7/S07 Boletín Financiero.xlsx')

df1 = pd.DataFrame(file1)
df2 = pd.DataFrame(file2)
df3 = pd.DataFrame(file3)
df4 = pd.DataFrame(file4)
df5 = pd.DataFrame(file5)
df6 = pd.DataFrame(file6)
df7 = pd.DataFrame(file7)
df8 = pd.DataFrame(file8)
df9 = pd.DataFrame(file9)
df10 = pd.DataFrame(file10)
df11 = pd.DataFrame(file11)
df12 = pd.DataFrame(file12)
df13 = pd.DataFrame(file13)
df14 = pd.DataFrame(file14)

df = pd.DataFrame()

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14])

def run():
    df.to_excel('./S1-7.xlsx')
    print('Done!')

if __name__ == '__main__':
    run()