class Nuqta():
    """xususiyatilari x va y
        medodlari gachaMasofa
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def gachaMasofa(self, n):
        distance = sqrt(abs(n.x - self.x) ** 2 + abs(n.y - self.y) ** 2)
        return distance