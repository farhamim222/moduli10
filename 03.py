# Define the Elevator class
class Elevator:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor

    def move_to_floor(self, floor):
        self.current_floor = floor
        print(f"Elevator is now on floor {self.current_floor}")


# Define the Talothe class with the fire alarm method
class Talothe:
    def __init__(self, num_elevators):
        self.elevators = [Elevator() for _ in range(num_elevators)]

    def palohälytys(self):
        print("Fire alarm! All elevators are moving to the ground floor.")
        for elevator in self.elevators:
            elevator.move_to_floor(0)


# Main program
if __name__ == "__main__":
    # Initialize the Talothe with a number of elevators
    house = Talothe(num_elevators=3)

    # Simulate normal elevator usage
    house.elevators[0].move_to_floor(5)
    house.elevators[1].move_to_floor(3)
    house.elevators[2].move_to_floor(7)

    # Trigger the fire alarm
    house.palohälytys()
