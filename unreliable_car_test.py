from Prac_08.unreliable_car import UnreliableCar

def main():
    not_so_reliable_car = UnreliableCar("Very Reliable Car", 100, 30)
    not_so_reliable_car.drive(50)
    not_so_reliable_car.drive(50)
    print(not_so_reliable_car)

if __name__ == "__main__":
    main()