import csv
import matplotlib.pyplot as plt

def read_csv_file():
    while True:
        filename = input("CSV Dateiname: ")
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file, delimiter=';')
                data = {'x': [], 'y': []}
                for row in reader:
                    data['x'].append(float(row[0]))
                    data['y'].append(float(row[1]))
                return data
        except FileNotFoundError:
            print("Datei wurde nicht gefunden. Bitte erneut einen Dateinamen eingeben.")
        except ValueError:
            print("Die CSV-Datei enthält ungültige Werte.")


def get_float(prompt, error_message):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(error_message)


def get_percentage(prompt, error_message):
    while True:
        value = get_float(prompt, error_message)
        if 0 <= value <= 100:
            return value
        else:
            print("Prozentwerte müssen im Bereich [0, 100] liegen.")


def create_subplot(x, y, start_percent, end_percent):
    n = len(x)
    start_idx = int((start_percent / 100) * n)
    end_idx = int((end_percent / 100) * n)
    plt.figure()
    plt.plot(x[start_idx:end_idx], y[start_idx:end_idx])
    plt.title(f'Graph von {start_percent}% bis {end_percent}%')
    plt.xlabel('x-Werte')
    plt.ylabel('y-Werte')
    plt.savefig('plot.pdf')
    plt.show()


def main():
    # Lesen der CSV-Datei
    data = read_csv_file()

    # Abfage nach Skalierungsfaktor
    scaling_factor = get_float("Skalierungsfaktor: ", "Der Skalierungsfaktor muss vom Typ Float sein.")

    # Abfrage des Start- und Endwertes in Prozent
    start_percent = get_percentage("Start Prozent: ", "Es werden Floats als Eingabe erwartet.")
    end_percent = get_percentage("End Prozent: ", "Es werden Floats als Eingabe erwartet.")

    # Skalierungsfaktor
    data['y'] = [y * scaling_factor for y in data['y']]

    # Plotten des Graphes abhängig von Nutzereingaben
    create_subplot(data['x'], data['y'], start_percent, end_percent)


if __name__ == "__main__":
    main()
