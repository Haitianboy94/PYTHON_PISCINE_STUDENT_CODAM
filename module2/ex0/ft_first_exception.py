def check_temperature(temp_str):

    try:
        tmp = int(temp_str)
        if tmp >= 0 and tmp <= 40:
            print(f"Temperature {tmp}°C is perfect for plants!\n")
        elif tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    user = input("Testing temperature:")
    check_temperature(user)
