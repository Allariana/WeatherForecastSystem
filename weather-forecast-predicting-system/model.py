import pandas as pd

df = pd.read_csv("weather.csv", encoding='windows-1250')
print(df.dtypes)
print("Koniec")