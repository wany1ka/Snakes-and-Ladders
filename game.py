import random

ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}

def dice_roll():
    return random.randint(1, 6)

def get_position(player, current_position):
    # If player lands on a ladder
    if current_position in ladders:
        new_position = ladders[current_position]
        print(f"Player {player} climbed a ladder! Moved to position {new_position}.")
        return new_position
    # If player lands on a snake
    elif current_position in snakes:
        new_position = snakes[current_position]
        print(f"Player {player} landed on a snake! Moved to position {new_position}.")
        return new_position
    else:
        return current_position

def play():
    player1_position = 0
    player2_position = 0

    while True:
        # Player 1
        input("Player 1, press Enter to roll the dice...")
        dice_result = dice_roll()
        player1_position += dice_result
        print(f"Player 1 rolled a {dice_result}.")
        player1_position = get_position(1, player1_position)
        print(f"Player 1 is now at position {player1_position}.\n")

        # If Player 1 wins
        if player1_position >= 100:
            print("Player 1 wins!")
            break

        # Player 2
        input("Player 2, press Enter to roll the dice...")
        dice_result = dice_roll()
        player2_position += dice_result
        print(f"Player 2 rolled a {dice_result}.")
        player2_position = get_position(2, player2_position)
        print(f"Player 2 is now at position {player2_position}.\n")

        # If Player 2 wins
        if player2_position >= 100:
            print("Player 2 wins!")
            break

play()
