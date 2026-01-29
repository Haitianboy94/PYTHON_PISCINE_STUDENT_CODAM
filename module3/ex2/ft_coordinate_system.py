import sys
import math

argvs = sys.argv
fix_distance = (0, 0, 0)
tuple_list = []
lenght = len(argvs)


def printErrormsg(arg):
    """Print Error message"""
    print(f"Error parsing coordinates: "
          f"invalid literal for int() with base 10: '{arg}'")
    print(f"Error details - Type: ValueError, Args: ("
          f"invalid literal for int() with base 10: '{arg}'"",)")


def parsing_coordinate(arg):
    """Create 3D positions like a game’s spawn points: (x, y, z)
• Calculate distances using the 3D Euclidean distance formula: sqrt((x2-x1)2 +
(y2-y1)2 + (z2-z1)2)
• Parse coordinate strings (like teleport commands!)
• Show off tuple unpacking magic (it’s like unwrapping a present!)"""
    try:
        parse_split = tuple(int(i) for i in arg.split(','))
        print(f"Position created: {parse_split}")
        x1 = fix_distance[0]
        y1 = fix_distance[1]
        z1 = fix_distance[2]

        x2 = parse_split[0]
        y2 = parse_split[1]
        z2 = parse_split[2]
        calcul = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
        distance = math.sqrt(calcul)
        print(f"Distance between {fix_distance} "
              f"and {parse_split}: {distance:.1f}")
        print("\nUnpacking demonstration:")
        print(f"Player at x={x2}, y={y2}, z={z2}")
        print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
        # return parse_split
    except ValueError:
        bad_parse = None
        parts = arg.split(',')
        for part in parts:
            try:
                int(part)
            except ValueError:
                bad_parse = part
                break
        printErrormsg(bad_parse)


def normalArgument(arg):
    """Normal argument"""
    try:
        for i in range(1, lenght):
            tuple_list.append(int(arg[i]))
        new_tuple = tuple(tuple_list)
        print(f"Position created: {new_tuple}")

        x1 = fix_distance[0]
        y1 = fix_distance[1]
        z1 = fix_distance[2]

        x2 = new_tuple[0]
        y2 = new_tuple[1]
        z2 = new_tuple[2]

        calcul = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
        distance = math.sqrt(calcul)
        print(f"Distance between {fix_distance} and {new_tuple}: "
              f"{distance:.2f}")
        print("\nUnpacking demonstration:")
        print(f"Player at x={x2}, y={y2}, z={z2}")
        print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
    except ValueError:
        bad_arg = None
        for i in range(1, lenght):
            try:
                int(arg[i])
            except ValueError:
                bad_arg = arg[i]
                break
        printErrormsg(bad_arg)


if __name__ == "__main__":

    print("=== Game Coordinate System ===")
    if lenght > 1:
        if ',' in argvs[1]:
            for coord_string in argvs[1:]:
                parsing_coordinate(coord_string)
        else:
            normalArgument(argvs)
    else:
        print("No arguments provided!")
