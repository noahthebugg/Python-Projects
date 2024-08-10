class Point:
    # Klassenattribut zur Speicherung der Anzahl der Punkte
    point_count = 0

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        # Erhöhung der Anzahl der Punkte
        Point.point_count += 1

    def __del__(self):
        # Verringerung der Anzahl der Punkte
        Point.point_count -= 1

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    def coincide(self, point: 'Point') -> bool:
        return self.x == point.x and self.y == point.y

    def __str__(self):
        return f"Punkt bei ({self.x},{self.y})"


class Circle(Point):
    def __init__(self, x: float, y: float, radius: float):
        # Initialisierung des Mittelpunktes des Kreises
        super().__init__(x, y)
        self.radius = radius

    def coincide(self, point: Point) -> bool:
        # Berechnung der Distanz zwischen dem Mittelpunkt des Kreises und einem gegebenen Punkt
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        # Überprüfung, ob der Punkt innerhalb oder auf dem Kreis liegt
        return distance <= self.radius

    def __str__(self):
        return f"Kreis mit Mittelpunkt bei ({self.x},{self.y}) und Radius {self.radius}"


class LineSeg:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def p_on_line(self, point: Point) -> bool:
        # Berechnung der Steigung der Strecke
        slope = (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
        # Berechnung des y-Achsenabschnitts
        intercept = self.point1.y - slope * self.point1.x
        # Überprüfung, ob der Punkt auf der Strecke liegt
        return point.y == slope * point.x + intercept and min(self.point1.x, self.point2.x) <= point.x <= max(self.point1.x, self.point2.x)

    def __str__(self):
        return f"Strecke von ({self.point1.x},{self.point1.y}) zu ({self.point2.x},{self.point2.y})"
