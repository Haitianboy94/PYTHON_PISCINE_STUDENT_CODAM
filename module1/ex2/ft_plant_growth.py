class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_day = age

    def print_info(self):
        print(f"{self.name}: {self.height}cm, {self.age_day} days old")

    def grow(self):
        self.height += 1

    def age(self):
        self.age_day += 1


if __name__ == "__main__":
    day = 1
    print(f"=== Day {day} ===")
    plant1 = Plant("Rose", 25, 30)
    initial_height = plant1.height
    plant1.print_info()

    for i in range(100):
        plant1.grow()
        plant1.age()
        day += 1
    print(f"=== Day {day} ===")
    last_height = plant1.height
    plant1.print_info()
    print(f"Growth this week: +{last_height - initial_height}cm")
