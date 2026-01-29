import sys


if __name__ == "__main__":
    """Discover how programs can receive information from the command line
• Learn to process different types of input data
• Handle cases where no information is provided
• Display information in a user-friendly way"""
    arg = sys.argv
    lenght = len(arg)
    if lenght == 1:
        print("=== Command Quest ===")
        print("No arguments provided!")
        print(f"Program name: {arg[0]}")
        print("Total arguments: 1")
    elif lenght > 1:
        print("=== Command Quest ===")
        print(f"Program name: {arg[0]}")
        print(f"Arguments received: {lenght - 1}")
        for i in range(1, lenght):
            print(f"Argument {i}: {arg[i]}")
        print(f"Total arguments: {lenght}")
