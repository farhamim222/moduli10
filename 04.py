import random


# Define the Car class
class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0  # Initial speed of the car
        self.distance_covered = 0  # Distance covered by the car in km

    def kulje(self, time_hours):
        self.distance_covered += self.speed * time_hours

    def change_speed(self):
        # Randomly adjust the speed of the car for each hour
        self.speed += random.randint(-10, 15)
        if self.speed < 0:
            self.speed = 0  # Prevents the speed from going negative


# Define the Kilpailu class
class Kilpailu:
    def __init__(self, name, length_km, cars):
        self.name = name
        self.length_km = length_km
        self.cars = cars

    def tunti_kuluu(self):
        for car in self.cars:
            car.change_speed()
            car.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Car Name':<15}{'Speed (km/h)':<15}{'Distance (km)':<15}")
        print("=" * 45)
        for car in self.cars:
            print(f"{car.name:<15}{car.speed:<15}{car.distance_covered:<15}")
        print("\n")

    def kilpailu_ohi(self):
        for car in self.cars:
            if car.distance_covered >= self.length_km:
                return True
        return False


# Main program
if __name__ == "__main__":
    # Creating a list of 10 cars for the race
    cars = [Car(f"Car {i + 1}") for i in range(10)]

    # Initialize the race with 8000 km length
    race = Kilpailu("The Great Scrap Rally", 8000, cars)

    hours_passed = 0
    while not race.kilpailu_ohi():
        race.tunti_kuluu()
        hours_passed += 1

        # Print the status every 10 hours
        if hours_passed % 10 == 0:
            print(f"--- Hour {hours_passed} ---")
            race.tulosta_tilanne()

    # Print the final results
    print("--- Race Over ---")
    race.tulosta_tilanne()
