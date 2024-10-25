class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor
        print(f"Elevator is now on floor {self.current_floor}")

    def move_to_floor(self, target_floor):
        if target_floor < self.lowest_floor or target_floor > self.highest_floor:
            print("Invalid floor!")
            return
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.highest_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.lowest_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

# Main program
elevator = Elevator(1, 10)  # Create an elevator with floors 1 to 10
elevator.move_to_floor(5)   # Move elevator to the 5th floor
elevator.move_to_floor(1)   # Move elevator back to the lowest floor
