class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant1.print_info()
    plant2 = Plant("Sunflower", 80, 45)
    plant2.print_info()
    plant3 = Plant("Cactus", 15, 120)
    plant3.print_info()
