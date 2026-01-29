def ft_plant_age():
    age = int(input("Enter the plant age: "))
    if age < 60:
        print("Plant needs more time to grow.")
    elif age >= 60:
        print("Plant is ready to harvest!")
