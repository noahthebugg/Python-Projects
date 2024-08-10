import numpy as np

# Preise in Cent
preise = np.array([5599, 12043, 26718])

# Gleichungssystem
A = np.array([
    [1, 1, 1],
    [1, 0, -4],
    [0, 1, -2]
])
b = np.array([500, 0, 50])

# Lösung des Gleichungssystems
loesung = np.linalg.solve(A, b)
loesung_abgerundet = np.floor(loesung).astype(int)
s, h, m = loesung_abgerundet
print("Stückzahlen:")
print(f"Schuhe: {s}, Handtaschen: {h}, Mäntel: {m}")

# Gesamtwert der täglichen Produktion in Cent
gesamter_wert_cent = np.dot(preise, loesung_abgerundet)
gesamter_wert_euro = gesamter_wert_cent / 100
print("Gesamtwert der täglichen Produktion in Euro:", gesamter_wert_euro)
