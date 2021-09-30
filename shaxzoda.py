from aylana import *


class Shaxzoda():
    """xususiyatilari start va end
        medodlari kesibUtadimi"""

    def __init__(self, start: Nuqta, end: Nuqta):
        self.start = start
        self.end = end

    def kesibUtadimi(self, circle: Aylana):
        if circle.niIchidami(self.start) and circle.niIchidami(self.end):
            return False
        if circle.niIchidami(self.start) or circle.niIchidami(self.end):
            return True
        else:
            return False