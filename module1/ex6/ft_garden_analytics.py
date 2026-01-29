class Plant:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew {self.height}cm")

    def get_info(self):
        return f"{self.name}: {self.height}cm"

    @staticmethod
    def validate_height(height):
        if height > 0:
            return True


class FloweringPlant(Plant):

    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def get_info(self):
        if self.blooming is True:
            status = "blooming"
        else:
            status = "Not blooming"
        return f"{self.name}, {self.height}cm, {self.color} flower ({status})"


class PrizeFlower(FloweringPlant):

    def __init__(self, name, height, color, point):
        super().__init__(name, height, color)
        self.point = point

    def get_info(self):
        base = super().get_info()
        return f"{base}, Prize point: {self.point}\n"


class GardenManager:

    total_garden = 0

    class Garden_stats:

        def __init__(self):
            self.plant_added = 0
            self.total_growth = 0
            self.regular_count = 0
            self.flowering_count = 0
            self.prize_count = 0

        def record_plant_added(self, plant):
            self.plant_added += 1
            if isinstance(plant, PrizeFlower):
                self.prize_count += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering_count += 1
            else:
                self.regular_count += 1

        def record_growth(self):
            self.total_growth += 1

        def get_summary(self):
            return (f"Plants added: {self.plant_added}, "
                    f"Total growth: {self.total_growth}cm")

        def get_type_breakdown(self):
            return (f"Plant types: {self.regular_count} regular, "
                    f"{self.flowering_count} flowering, "
                    f"{self.prize_count} prize flowers")

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.Garden_stats()
        GardenManager.total_garden += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.record_plant_added(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth()

    def calculate_score(self):
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.point + 30
        return score

    def generate_report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print(self.stats.get_summary())
        print(self.stats.get_type_breakdown())

    @classmethod
    def create_garden_network(cls, owners):
        gardens = []
        for owner in owners:
            gardens.append(cls(owner))
        return gardens

    @classmethod
    def get_total_gardens(cls):
        return cls.total_garden

    @staticmethod
    def compare_gardens(garden1, garden2):
        score1 = garden1.calculate_score()
        score2 = garden2.calculate_score()
        print(f"Garden scores - {garden1.owner}: {score1}, "
              f"{garden2.owner}: {score2}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.help_all_grow()

    alice_garden.generate_report()

    print(f"\nHeight validation test: {Plant.validate_height(50)}")

    pine = Plant("Pine Tree", 80)
    tulip = FloweringPlant("Tulip", 12, "pink")
    bob_garden.add_plant(pine)
    bob_garden.add_plant(tulip)

    GardenManager.compare_gardens(alice_garden, bob_garden)

    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
