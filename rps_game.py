import random


def main():
    print("Welcome to Rock Paper Scissors!")

    print("\nGame Rules:")
    print("Rock beats Scissors.")
    print("Scissors beats Paper.")
    print("Paper beats Rock.")
    print("If both players choose the same option, it is a tie.")
    print("A tie means you automatically rematch.")

    choices = ["rock", "paper", "scissors"]

    while True:
        player_choice = input(
            "\nEnter your choice (rock, paper, or scissors): "
        ).lower().strip()

        if player_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        print("You chose:", player_choice)

        computer_choice = random.choice(choices)

        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie! Let's Rematch!")
            continue

        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "scissors" and computer_choice == "paper")
            or (player_choice == "paper" and computer_choice == "rock")
        ):
            print("You win!")
            break

        else:
            print("Computer wins!")
            break


if __name__ == "__main__":
    main()
