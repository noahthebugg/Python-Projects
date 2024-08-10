from time import sleep
from numpy import sin, cos, arccos, pi

# Datenstruktur
airports = {
    'berlin' : {
        'lat' : 52.365,
        'lon' : 13.51,
        'dest' : ['marrakesh', 'montreal']
    },
    'marrakesh' : {
        'lat' : 31.6,
        'lon' : -8.025,
        'dest' : ['berlin', 'lima', 'montreal']
    },
    'montreal' : {
        'lat' : 45.67,
        'lon' : -74.04,
        'dest' : ['berlin', 'marrakesh', 'lima', 'montreal']
    },
    'lima' : {
        'lat' : -12.02,
        'lon' : -77.11,
        'dest' : ['marrakesh', 'montreal']
    },
    'ulaanbaatar' : {
        'lat' : 47.85,
        'lon' : 106.76,
        'dest' : ['montreal']
    }
}

# Funktion zur Umrechnung von Gradmaß auf Bogenmaß
def deg_to_rad(deg):
    return deg * pi / 180

# Funktion zur Berechnung der Distanz zwischen zwei Flughäfen
def calc_distance(airport1, airport2):
    lat1, lon1 = airports[airport1]['lat'], airports[airport1]['lon']
    lat2, lon2 = airports[airport2]['lat'], airports[airport2]['lon']
    orthod = arccos(sin(deg_to_rad(lat1)) * sin(deg_to_rad(lat2)) +
                    cos(deg_to_rad(lat1)) * cos(deg_to_rad(lat2)) *
                    cos(abs(deg_to_rad(lon2) - deg_to_rad(lon1))))
    return 6371 * orthod

# Funktion zur Überprüfung der Eingabe
def get_valid_input(options, key):
    error_messages = {
        'start': 'Fehler: Unbekannter Flughafen!',
        'dest': 'Fehler: Unbekannter Flughafen oder kein möglicher Zielflughafen!',
        '_': 'Fehler: Unbekannter Fehler!'
    }
    while True:
        user_input = input('<> ').strip().lower()
        if user_input in options:
            return user_input.title()
        else:
            print('\n' + error_messages.get(key, error_messages['_']) + '\n')
            quit()

# Funktion zur Aufzählung von Listenelementen
def print_list(list):
    for i, list_item in enumerate(list):
        if (i > 0):
            print(',', end=' ')
        print(list_item.title(), end='')
        if (i == len(list) - 1):
            print('.')

# Programmstart
print('\n----- Programm zur Berechnung von Flugdistanzen -----\n',
      '\nBei welchem Flughafen möchten Sie starten?',
      'Folgende Flughäfen stehen zur Auswahl:', end=' ')
print_list(airports)

# Eingabe des Startflughafens
start_input = get_valid_input(airports, 'start')

# Mögliche Zielflughäfen
print('Ihre Auswahl:', start_input.title(), '>>>', 'Mögliche Zielflughäfen:', end=' ')
print_list(airports[start_input.lower()]['dest'])

# Eingabe des Zielflughafens
dest_input = get_valid_input(airports[start_input.lower()]['dest'], 'dest')

# Berechnung und ausgabe der Distanz
distance = round(calc_distance(start_input.lower(), dest_input.lower()))
print(f'Die Distanz zwischen {start_input} und {dest_input} beträgt rund: {distance} km.')

# Beenden des Programmes mit Delay
sleep(2)
print('\nProgramm wird beendet...')
sleep(1)
