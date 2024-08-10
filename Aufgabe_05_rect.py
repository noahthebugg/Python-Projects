def draw_rectangle(height, width):
    # Obere Rahmenlinie
    print('C' * (width + 2))

    # Mittlere Zeilen mit 'A' und Rahmen 'C'
    for _ in range(height):
        print('C' + 'A' * width + 'C')

    # Untere Rahmenlinie
    print('C' * (width + 2))

# Benutzer nach Höhe und Breite des Rechtecks fragen
height = int(input("Bitte Höhe eingeben: "))
width = int(input("Bitte Breite eingeben: "))

# Leerzeile
print()

# Rechteck zeichnen
draw_rectangle(height, width)
