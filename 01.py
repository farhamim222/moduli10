class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor  # Starts on the lowest floor

    def move_to_floor(self, target_floor):
        if target_floor < self.lowest_floor or target_floor > self.highest_floor:
            print(f"Error: Floor {target_floor} is out of bounds.")
            return

        while self.current_floor < target_floor:
            self.move_up()

        while self.current_floor > target_floor:
            self.move_down()

    def move_up(self):
        if self.current_floor < self.highest_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}.")
        else:
            print("Elevator is already on the top floor.")

    def move_down(self):
        if self.current_floor > self.lowest_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}.")
        else:
            print("Elevator is already on the lowest floor.")


# Main program
def main():
    # Create an elevator with 1 as the lowest and 10 as the highest floor
    elevator = Elevator(1, 10)

    # Move to the 5th floor
    print("Moving to the 5th floor:")
    elevator.move_to_floor(5)

    # Move back to the lowest floor
    print("\nMoving back to the lowest floor:")
    elevator.move_to_floor(1)


if __name__ == "__main__":
    main()



