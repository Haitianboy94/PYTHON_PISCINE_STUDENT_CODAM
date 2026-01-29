class GardenError(Exception):
    pass


class Plant:
    def __init__(self, name):
        self.name = name
        self.water = 0
        self.sun = 0


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, name):
        try:
            if name == "":
                raise GardenError("Plant name can not be empty!")
            plant = Plant(name)
            self.plants.append(plant)
            print(f"Added {name} successfully")
            return plant
        except GardenError as e:
            print(f"Error adding plant: {e}")
            return None

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant, water, sun):
        try:
            if water > 10:
                raise GardenError(f"Water level {water} is too high (max 10)")
            elif water < 1:
                raise GardenError(f"Water level {water} is too low (min 1)")
            elif sun > 12:
                raise GardenError(f"Sunlight hours {sun} is too high (max 12)")
            elif sun < 2:
                raise GardenError(f"Sunlight hours {sun} is too low (min 2)")
            elif plant.name == "":
                raise GardenError("Plant name can not be empty!")

            plant.water = water
            plant.sun = sun
            print(f"{plant.name}: healthy (water: {water}, sun: {sun})")
        except GardenError as e:
            print(f"Error checking {plant.name}: {e}")


if __name__ == "__main__":
    print("Adding plants to garden...")
    garden = GardenManager()

    plant1 = garden.add_plant("Tomato")
    plant2 = garden.add_plant("Lettuce")
    plant3 = garden.add_plant("")

    print()
    garden.water_plants()

    print("\nChecking plant health...")
    if plant1:
        garden.check_plant_health(plant1, 5, 8)
    if plant2:
        garden.check_plant_health(plant2, 0, 0)
    if plant3:
        garden.check_plant_health(plant3, 5, 9)
    print()
    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuig...\n")
    print("Garden management system test complete!")
