class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):

    def __init__(self, name, height, age, trunck_diameter):
        super().__init__(name, height, age)
        self.trunck_diameter = trunck_diameter
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunck_diameter}cm diameter")

    def produce_shade(self):
        canopy_diameter = self.trunck_diameter * 20 * 0.01
        canopy_radius = canopy_diameter / 2
        shade_area = 3.14159 * (canopy_radius ** 2)
        result = int(shade_area)
        print(f"{self.name} privides {result} square meters of shade\n")


class Vegetable(Plant):

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {nutritional_value}\n")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    flower = Flower("Rose", 25, 30, "red")
    flower.bloom()

    flower2 = Flower("Sunflower", 20, 32, "yellow")
    flower2.bloom()

    tree = Tree("Oak", 500, 1825, 50)
    tree.produce_shade()

    tree2 = Tree("Mapou", 1000, 10000, 200)
    tree2.produce_shade()

    vegetable = Vegetable("Tomato", 80, 90, "summer", 'C')
    vegetable2 = Vegetable("Avocado", 100, 400, "summer", "B5")
