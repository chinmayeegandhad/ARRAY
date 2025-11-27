import sys

def process_scores():
    if len(sys.argv) < 2:
        print("Usage: python array.py 5,10,15,20,25")
        return

    # Read scores from the first command-line argument
    scores = list(map(int, sys.argv[1].split(",")))

    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    print("Scores:", scores)
    print("Total Score:", total)
    print("Average Score:", round(average, 2))
    print("Maximum Score:", maximum)
    print("Minimum Score:", minimum)

if _name_ == "_main_":
    process_scores()