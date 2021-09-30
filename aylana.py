from nuqta import *

class Aylana():
    """
    xususiyatilari markaz va radius
        medodlari niIchidami
    """

    def __init__(self, markaz: Nuqta, radius: int):
        self.markaz = markaz
        self.radius = radius

    def niIchidami(self, dot: Nuqta):
        if dot.gachaMasofa(self.markaz) < self.radius:
            return True
        else:
            return False