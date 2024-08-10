"""
TU Berlin
Einführung in die Informationstechnik für Ingenieure

Vorgaben zu Aufgabe 05 - Kontrollstrukturen II
"""

mix = [51, 0, "Q", "LISTE", 4.3, {"null" : 0, "eins" : 1, "zwei" : 2}, -1, "Tupel", 1, "False", 3 > 5, "hell", 666, "dictionaries", True, 42.42]

# START TODO ###################

ints = []
doubles = []
strings = []
dicts = []
summe = 0

for _ in mix:
    if type(_) == bool:
        break
    elif type(_) == int:
        ints.append(_)
        summe += _
    elif type(_) == float:
        doubles.append(_)
        summe += _
    elif type(_) == str:
        strings.append(_)
    elif type(_) == dict:
        dicts.append(_)

# END TODO #####################


# Ausgaben der Listen
print("Sortierte Listen: ")
print(ints)
print(doubles)
print(strings)
print(dicts)

# Ausgabe der Summe von allen eingelesenen Zahlen
print(summe)
