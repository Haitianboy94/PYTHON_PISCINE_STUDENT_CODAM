import sys


if __name__ == "__main__":
    """Accept player scores from the command line (like cheat codes,but legal!)
• Use lists to store and organize the scores
• Calculate some basic stats that would make any game dev happy
• Handle the "oops, I typed ’banana’ instead of ’1000’" scenarios gracefully
• Make the output look cool enough to impress your gaming buddies"""
    list_of_score = []
    arg = sys.argv
    lenght = len(arg)
    if lenght == 1:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            for i in range(1, lenght):
                list_of_score.append(int(arg[i]))
            print("=== Player Score Analytics ===")
            print(f"Score processed: {list_of_score}")
            print(f"Total players: {lenght - 1}")
            print(f"Total score: {sum(list_of_score)}")
            average_score = sum(list_of_score) / (lenght-1)
            print(f"Average score: {average_score}")
            print(f"High score: {max(list_of_score)}")
            print(f"Low score: {min(list_of_score)}")
            print(f"Score range: {max(list_of_score) - min(list_of_score)}")
        except ValueError:
            print("You can only enter digit")
