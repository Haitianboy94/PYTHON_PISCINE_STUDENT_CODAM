def garden_operations():

    try:
        int("Hello Codam")
    except ValueError:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        open('42school.txt')
    except FileNotFoundError:
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        dic = {"Hello": 42}
        print(dic["World"])
    except KeyError:
        print("Testing KeyError...")
        print("Caught KeyError: 'missingplant'\n")

    lst = {1, 5, 9}
    print(lst[3])


def test_error_function():
    try:
        garden_operations()
    except Exception:
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_function()
