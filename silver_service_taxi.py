from Prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = 0
        self.price_per_km = Taxi.price_per_km * fanciness
        self.flagfall = 4.50

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        return self.flagfall + super().get_fare()