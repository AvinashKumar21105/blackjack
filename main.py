import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
def blackjack():
    game_over = False
    player=random.sample(cards, 2)
    computer=random.sample(cards, 2)
    while not game_over:
        player_score = calculate_score(player)
        computer_score = calculate_score(computer)
        print("Your cards: ", player, ", current score: ", player_score)
        print("Computer's first card: ", computer[0])
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            a = input("Type 'y' to get another card, type 'n' to pass: ")
            if a == 'y':
                player.append(random.choice(cards))
                player_score = calculate_score(player)
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer.append(random.choice(cards))
        computer_score = calculate_score(computer)  # Use calculate_score to get the current score

    print("Your final hand: ", player, ", final score: ", player_score)
    print("Computer's final hand: ", computer, ", final score: ", computer_score)

    if player_score > 21:
        return "You lose!"
    elif computer_score > 21:
        return "You win!"
    elif computer_score == player_score:
        return "It's a draw!"
    elif player_score == 0:
        return "You win!"
    elif computer_score == 0:
        return "You lose!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

print(blackjack())


