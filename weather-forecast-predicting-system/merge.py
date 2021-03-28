import os
import glob
import pandas as pd

from constants import *

all_files = glob.glob(os.path.join(SOURCE_DATA, "*.csv"))
all_files2 = glob.glob(os.path.join(SOURCE_DATA2, "*.csv"))

i = 0
for f in all_files:
        df = pd.read_csv(f, header=None, encoding='windows-1250')
        df.to_csv(DATA_WITH_HEADERS + "\k_" + str(i) + ".csv", header=["Kod stacji", "Nazwa stacji", "Rok", "Miesiac", "Dzien", "Srednia dobowa temperatura",
"Status pomiaru TEMP", "Srednia dobowa wilgotnosc wzgledna[%]", "Status pomiaru WLGS", "Srednia dobowa predkosc wiatru [m/s]", "Status pomiaru FWS",
        "Srednie dobowe zachmurzenie ogolne [oktanty]", "Status pomiaru NOS"], encoding='windows-1250')
        i += 1

i = 0
for f in all_files2:
        df = pd.read_csv(f, header=None, encoding='windows-1250')
        df.to_csv(DATA_WITH_HEADERS2 + "\k_" + str(i) + ".csv", header=["Kod stacji", "Nazwa stacji", "Rok", "Miesiac", "Dzien", "Maksymalna temperatura dobowa [°C]",
"Status pomiaru TMAX", "Minimalna temperatura dobowa [°C]", "Status pomiaru TMIN", "Średnia temperatura dobowa [°C]", "Status pomiaru STD", "Temperatura minimalna przy gruncie [°C]",
        "Status pomiaru TMNG", "Suma dobowa opadów [mm]", "Status pomiaru SMDB", "Rodzaj opadu  [S/W/ ]", "Wysokość pokrywy śnieżnej [cm]", "Status pomiaru PKSN"],
                  encoding='windows-1250')
        i += 1

files = glob.glob(os.path.join(DATA_WITH_HEADERS, "*.csv"))
files2 = glob.glob(os.path.join(DATA_WITH_HEADERS2, "*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',', header=None, encoding='windows-1250') for f in files)
df_from_each_file2 = (pd.read_csv(f2, sep=',', header=None, encoding='windows-1250') for f2 in files2)
df_merged = pd.concat(df_from_each_file)
df_merged2 = pd.concat(df_from_each_file2)
df_merged.to_csv(DESTINATION_FOLDER + "\k_d_t_m.csv", encoding='windows-1250')
df_merged2.to_csv(DESTINATION_FOLDER + "\k_d_m.csv", encoding='windows-1250')

