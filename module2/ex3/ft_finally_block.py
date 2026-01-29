def water_plants(plant_list):
    print("Open watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception(" Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("Testing normal watering...")
    list_plant = ["Tomato", "Lettuce", "Carrots"]
    water_plants(list_plant)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    lst_plnt = ["Tomato", None, "Lettuce"]
    water_plants(lst_plnt)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
