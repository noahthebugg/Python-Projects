# Berechnung der Note aus der Punktzahl
def calculate_grade_value(key, points):
    if points >= key[9]:
        return 1.0
    elif points >= key[8]:
        return 1.3
    elif points >= key[7]:
        return 1.7
    elif points >= key[6]:
        return 2.0
    elif points >= key[5]:
        return 2.3
    elif points >= key[4]:
        return 2.7
    elif points >= key[3]:
        return 3.0
    elif points >= key[2]:
        return 3.3
    elif points >= key[1]:
        return 3.7
    elif points >= key[0]:
        return 4.0
    elif points < key[0]:
        return 5.0
    else:
        return None

# Berechnung der Note mit Notenschlüssel
def calculate_grade(user_input, points):
    KEY1 = [50, 54, 58, 62, 66, 70, 74, 78, 82, 86]
    KEY2 = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    KEY3 = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

    match user_input:
        case 1:
            return calculate_grade_value(KEY1, points)
        case 2:
            return calculate_grade_value(KEY2, points)
        case 3:
            return calculate_grade_value(KEY3, points)
        case _:
            return None

# Prüfen auf Korrektheit der Angabe
def check_input(prompt, cond):
    user_input = input(prompt).replace(',', '.')

    if '-' in user_input:
        if(cond(user_input[1:])):
            return float(user_input)
        else:
            print('\nFehler: Unbekannter Notenschlüssel oder fehlerhafte Punkteingabe. Versuchen Sie es erneut.')
            quit()
    elif cond(user_input):
        return float(user_input)
    else:
        print('\nFehler: Unbekannter Notenschlüssel oder fehlerhafte Punkteingabe. Versuchen Sie es erneut.')
        quit()

# Eingabe des Notenschlüssels
key_input = check_input('Bitte wählen Sie Ihren Notenschlüssel (1, 2, 3): ', lambda x: x.isdigit() and 1 <= int(x) <= 3)
# Eingabe der Punktzahl
point_input = check_input('Bitte geben Sie die erreichte Punktzahl ein (Dezimalzahl möglich): ', lambda x: x[1:].replace('.', '').isdigit())

# Ausgabe der Note
grade = calculate_grade(key_input, point_input)
if grade is not None:
    print(f'\nNote: {grade}')
else:
    print('\nFehler: Note konnte nicht berechnet werden. Versuchen Sie es erneut.')
