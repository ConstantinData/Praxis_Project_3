import pandas as pd
import matplotlib.pyplot as plt

# Lade den Datensatz mit Zeitreihendaten für die Jahre 2018 und 2019
time_series_data = pd.read_csv('20230828_3.3_Datensatz_Glueck_2018-2019.csv')

# Konvertiere das Datum in einen datetime-Datentyp
time_series_data['Year'] = pd.to_datetime(time_series_data['Year'])

# Setze das Datum als Index
time_series_data.set_index('Date', inplace=True)

# Visualisiere die Zeitreihendaten
plt.figure(figsize=(10, 6))
time_series_data['Score'].plot(label='Happiness Score')
time_series_data['GDP_per_capita'].plot(label='GDP per Capita')
# Füge weitere Variablen hinzu...

plt.title('Time Series Analysis')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()
plt.show()