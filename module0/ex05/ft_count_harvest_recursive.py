def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))

    def count_down(current_day):
        if current_day > day:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        count_down(current_day + 1)
    count_down(1)
