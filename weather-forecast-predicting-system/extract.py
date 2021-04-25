import pandas as pd
from constants import *

df = pd.read_csv("weather.csv", encoding='windows-1250', squeeze=True)
df_sort = df.sort_values(by=['Kod stacji', 'Rok', 'Miesiac', 'Dzien'])
df_city = df_sort.loc[df_sort['Nazwa stacji'] == CITY]
df_city_chosen = df_city.iloc[:, [5, 6, 7, 8, 9, 10, 11, 12, 13]]
df_city_chosen.to_csv(DESTINATION_FOLDER + FILENAME, encoding='windows-1250')

print("Koniec")

# df_city_chosen = df_city.iloc[:, [5, 6, 7, 11, 12]]