class Plant:

    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.height = starting_height
        self.age = starting_age

    def set_height(self, new_height):
        self.new_height = new_height
        if (self.new_height < 0):
            print(f"Invalid operation attempted: height "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print("\n")
            print(f"Current plant: {self.name} ({self.height}cm, "
                  f"{self.age} days)")
            print("\n")
        else:
            self.height = new_height

    def set_age(self, new_age):
        self.new_age = new_age
        if (self.new_age < 0):
            print(f"Invalid operation attempted: age "
                  f"{new_age} days [REJECTED]")
            print("Security: Negative age rejected")
            print("\n")
            print(f"Current plant: {self.name} "
                  f"({self.height}cm, {self.age} days)")
        else:
            self.age = new_age

    def get_height(self):
        print(self.height)

    def get_age(self):
        print(self.age)

    def display(self):
        print(f"Plant created: {self.name}")
        print(f"Height updated: {self.height}cm [OK]")
        print(f"Height updated: {self.age}days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 25, 30)
    plant1.display()
    plant1.get_age()
    plant1.get_height()
