from random import seed, randint


def get_rating(player_name: str) -> int:
    player_rating = 0

    with open("rating.txt") as rating_file:
        for line in rating_file:
            (name, rating) = (line.split()[0], int(line.split()[1]))
            if player_name == name:
                player_rating = rating

    return player_rating


def get_winners(choices: list, selection: str) -> list:
    if selection not in choices:
        return []

    # evaluate the final size of winners[], which will be at most half of the initial list of choices
    total_choices = len(choices)
    half_choices = int((total_choices - 1) / 2)  # subtract 1 to exclude the selection

    winners = []                     # holds the indexes for the winning options, in rapport to selection
    rank = choices.index(selection)  # selection index

    i = 1
    while i <= half_choices:
        winners.append(choices[(rank + i) % total_choices])
        i += 1

    return winners


def run_game():
    default_options = ["rock", "paper", "scissors"]

    name_prompt = "Enter your name:"
    rating_input = "!rating"
    exit_input = "!exit"

    start_msg = "Okay, let's start"
    finish_msg = "Bye!"
    invalid_option_msg = "Invalid input"

    player_name = input(name_prompt)
    print(f"Hello, {player_name}")
    player_rating = get_rating(player_name)

    options_input = input()
    if not options_input:
        options = default_options
    else:
        options = options_input.split(",")

    print(start_msg)

    while True:
        user_choice = input()

        if user_choice == exit_input:
            print(finish_msg)
            break
        if user_choice == rating_input:
            print(f"Your Rating: {player_rating}")
            continue
        if user_choice not in options:
            print(invalid_option_msg)
            continue

        win_choices = get_winners(options, user_choice)

        seed()
        computer_choice = options[randint(0, len(options) - 1)]

        if computer_choice in win_choices:
            print(f"Sorry, but the computer chose {computer_choice}")
        elif computer_choice == user_choice:
            print(f"There is a draw ({computer_choice})")
            player_rating += 50
        else:
            print(f"Well done. The computer chose {computer_choice} and failed")
            player_rating += 100




run_game()