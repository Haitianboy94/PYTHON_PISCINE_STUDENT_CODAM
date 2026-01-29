class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, name):
        self.name = name
        super().__init__(f"The {self.name} plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


if __name__ == "__main__":
    try:
        raise PlantError("Tomato")
    except PlantError as e:
        print("Testing PlantError...")
        print(f"Caught PlantError: {e}\n")

    try:
        raise WaterError()
    except WaterError as e:
        print("Testing WaterError...")
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")
