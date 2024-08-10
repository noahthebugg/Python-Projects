import numpy as np

# 1. Speichern der Matrix
matrix_given = np.array([
    [-np.pi, 1, np.pi],
    [0, 2*np.pi, -1],
    [0, 0, -2]
])

# 2. Minimum jeder Spalte
min_per_column = np.min(matrix_given, axis=0)
print("Minimum jeder Spalte:", min_per_column)

# 3. Ersetzen von Werten kleiner als Null durch Null
matrix_given[matrix_given < 0] = 0
print("\nMatrix nach Ersetzen von Werten kleiner als Null durch Null:")
print(matrix_given)
print("\nNicht-Null Einträge der Matrix:", matrix_given[matrix_given != 0])

# 4. Erstellen eines leeren Vektors
vektor_empty = np.empty(5)
print("\nEmpty Vektor:", vektor_empty)

# 5. Erstellen einer Diagonalmatrix
matrix_diag = np.diag(vektor_empty)
print("\nDiagonalmatrix mit dem empty Vektor:")
print(matrix_diag)

# 6. Erstellen eines Vektors mit arange
vektor_arange = np.arange(3, 15, 3)
print("\nArange Vektor:", vektor_arange)

# 7. Erstellen einer 5x5 Matrix mit der ersten Nebendiagonalen
matrix_5x5 = np.zeros((5, 5))
np.fill_diagonal(matrix_5x5[1:], vektor_arange)
print("\n5x5 Matrix mit arange Vektor auf der ersten Nebendiagonalen:")
print(matrix_5x5)

# 8. Ausgabe der unteren rechten 2x2 Matrix
lower_right_2x2 = matrix_5x5[-2:, -2:]
print("\nUntere rechte 2x2 Matrix:")
print(lower_right_2x2)
