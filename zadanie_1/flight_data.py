import pandas as pd
import matplotlib.pyplot as plt
import requests
from zadanie_1.database import *

# Funkcja do pozyskania danych z OpenSky Network API
def fetch_flight_data(databasefile="flights.db"):
    # wspolrzedne ATL (Atlanta) w stopniach 
    lon_min, lat_min = -85.4277, 32.6407
    lon_max, lat_max = -83.4277, 34.6407

    # print("jestem1")
    # napisz kod do pozyskania danych z OpenSky Network API, pamietaj o zalozeniu konta
    user_name = 'tomD'   # Your OpenSky Network username
    password = 'tomek2004'   # Your OpenSky Network password
    
    # URL do API
    url_data = (
        'https://' + user_name + ':' + password +
        '@opensky-network.org/api/states/all?' +
        'lamin=' + str(lat_min) + '&lomin=' + str(lon_min) +
        '&lamax=' + str(lat_max) + '&lomax=' + str(lon_max)
    )
    # print("jestem2")
    try:
        response = requests.get(url_data)
        response.raise_for_status()
        data = response.json()
        # print(data)
        # Kolumny dla DataFrame
        col_name = [
            'icao24', 'callsign', 'origin_country', 'time_position', 'last_contact',
            'long', 'lat', 'baro_altitude', 'on_ground', 'velocity',
            'true_track', 'vertical_rate', 'sensors', 'geo_altitude',
            'squawk', 'spi', 'position_source'
        ]

        # Tworzenie DataFrame
        flight_df = pd.DataFrame(data['states'], columns=col_name)

        # Zapisz dane do bazy SQLite
        save_to_db(flight_df, databasefile)
        print("Data saved to database successfully!")

    except Exception as e:
        print(f"Error fetching flight data: {e}")


# Odczyt danych i wygenerowanie wykresu z danych lotniczych
def plot_flight_data(databasefile="flights.db", show_plot=True):
    # Wczytaj dane lotnicze z bazy danych
    flight_df = load_flight_data(databasefile) # to bedzie obiekt typu DataFrame

    # caly kod tutaj (filtracja, konwersja jednostek, sortowanie i wybieranie jednego, rysowanie wykresu)

    flight_df = flight_df.dropna(subset=['velocity', 'geo_altitude'])
    flight_df['velocity'] = pd.to_numeric(flight_df['velocity'])
    flight_df['geo_altitude'] = pd.to_numeric(flight_df['geo_altitude'])

    flight_df = flight_df.sort_values(by='velocity', ascending=False).drop_duplicates(subset='icao24', keep='first')

    # Konwersja jednostek
    flight_df['velocity'] = flight_df['velocity'] * 3.6  # m/s na km/h
    flight_df['geo_altitude'] = flight_df['geo_altitude'] / 1000  # metry na kilometry

    # Wykres
    plt.figure(figsize=(10, 6))
    plt.scatter(flight_df['velocity'], flight_df['geo_altitude'], alpha=0.6, color='blue', marker='o')
    plt.xlabel("Prędkość (km/h)")
    plt.ylabel("Wysokość (km)")
    plt.title("Zależność wysokości od prędkości")
    plt.xlim(0, 1200)
    plt.ylim(0, 14)

    plt.grid(True)
    plt.tight_layout()
    # Wyświetlanie wykresu tylko, jeśli show_plot=True
    if show_plot:
        plt.show()
