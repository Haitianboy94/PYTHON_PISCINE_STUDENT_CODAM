class Plant:

    total_plant = 0

    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.stating_height = starting_height
        self.stating_age = starting_age
        Plant.total_plant += 1

    def display(self):
        print(f"Created: {self.name} ({self.stating_height}cm, "
              f"{self.stating_age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 25, 30)
    plant1.display()
    plant2 = Plant("Oak", 200, 365)
    plant2.display()
    plant3 = Plant("Cactus", 5, 90)
    plant3.display()
    plant4 = Plant("Sunflower", 80, 45)
    plant4.display()
    plant5 = Plant("Fern", 15, 120)
    plant5.display()
    print(f"Total plants creted: {Plant.total_plant}")
