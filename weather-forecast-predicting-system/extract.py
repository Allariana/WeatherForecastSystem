import pandas as pd
from constants import *

df = pd.read_csv("weather.csv", encoding='windows-1250', squeeze=True)
df_sort = df.sort_values(by=['Kod stacji', 'Rok', 'Miesiac', 'Dzien'])
df_warsaw = df_sort.loc[df_sort['Nazwa stacji'] == 'WARSZAWA-FILTRY']
df_warsaw_temp = df_warsaw.iloc[:, 7]
df_warsaw_temp.to_csv(DESTINATION_FOLDER + "\warsaw.csv", encoding='windows-1250')

print("Koniec")