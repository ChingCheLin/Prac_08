"""
CP1404/CP5632 Practical
Test Silver Service Taxi
"""
from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 1.5)

    fancy_taxi.drive(40)

    print(fancy_taxi)
    print("Current fare: $ {:.2f}".format(fancy_taxi.get_fare()))

if __name__ == '__main__':
    main()