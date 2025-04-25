import os

from constants import MAX_HIGH_SCORE_ENTRIES, HIGH_SCORE_FILE_NAME


def print_high_scores():
    print()
    print("High Scores:")
    print("Name       Score")
    print("----------------")
    try:
        with open("highscores.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, score = line.strip().split(":")
                print(f"{name:<10} {score:>5}")
    except FileNotFoundError:
        print("Error: high scores file not found.")
    except Exception as e:
        print(f"an error occurred: {e}")
    print("----------------\n\n")


def update_high_scores(username, score):
    """
    Updates a high scores file with a new score and username, keeping at most
    max_entries.

    Args:
        username (str): The username associated with the score.
        score (int): The new score to add.
        filename (str): The name of the high scores file.
        max_entries (int): The maximum number of high scores to keep.
    """
    scores = []

    # Read existing scores
    if os.path.exists(HIGH_SCORE_FILE_NAME):
        try:
            with open(HIGH_SCORE_FILE_NAME, 'r') as file:
                for line in file:
                    try:
                        name, score_str = line.strip().split(':')
                        scores.append((int(score_str), name))
                    except ValueError:
                        print(f"Warning: Invalid score format in line: {line.strip()}")
        except FileNotFoundError:
            print(f"Warning: File '{HIGH_SCORE_FILE_NAME}' not found. Creating a new one.")

    # Add the new score and username and sort
    scores.append((score, username))
    scores.sort(reverse=True)

    # Keep only the top max_entries scores
    scores = scores[:MAX_HIGH_SCORE_ENTRIES]

    # Write the updated scores back to the file
    try:
        with open(HIGH_SCORE_FILE_NAME, 'w') as file:
            for score_val, name in scores:
                file.write(f"{name}:{score_val}\n")
    except Exception as e:
        print(f"Error updating high scores: {e}")
