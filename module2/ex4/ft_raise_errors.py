def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if plant_name == "":
            raise ValueError(" Plant name cannot be empty!")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        if water_level > 10 or water_level < 1:
            raise ValueError(" Water level 15 is too high (max 10)")
        print(f"{water_level} is good!")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too height (max 12)")
        print(f"Sunlight hours is {sunlight_hours} is good!\n")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks():
    print("Testing good values...")
    check_plant_health("Tomato", 8, 12)
    print("Testing empty plant name...")
    check_plant_health("", 8, 12)
    print("Testing bad water level...")
    check_plant_health("", 15, 12)
    print("Testing bad sunlinght hours...")
    check_plant_health("", 15, 0)
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
