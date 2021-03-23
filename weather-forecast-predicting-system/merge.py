import os
import glob
import pandas as pd

from constants import *

all_files = glob.glob(os.path.join(SOURCE_DATA, "*.csv"))

i = 0
for f in all_files:
        df = pd.read_csv(f, header=None, encoding='windows-1250')
        df.to_csv(DATA_WITH_HEADERS + "\k_" + str(i) + ".csv", header=["Kod stacji", "Nazwa stacji", "Rok", "Miesiac", "Dzien", "Srednia dobowa temperatura",
"Status pomiaru TEMP", "Srednia dobowa wilgotnosc wzgledna[%]", "Status pomiaru WLGS",
"Srednia dobowa predkosc waitru [m/s]", "Status pomiaru FWS", "Srednie dobowe zachmurzenie ogolne [oktanty]",
        "Status pomiaru NOS"], encoding='windows-1250')
        i += 1

files = glob.glob(os.path.join(DATA_WITH_HEADERS, "*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',', header=None, encoding='windows-1250') for f in files)
df_merged = pd.concat(df_from_each_file)
df_merged.to_csv(DESTINATION_FOLDER + "\k_d_t_m.csv", encoding='windows-1250')

