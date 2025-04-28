import random
from art import logo

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    index = random.choice(cards)
    return cards[index]

def check(cards):
    if cards > 21:
        return True
    return False

while True:
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    for i in range(2):
        user_card = draw_card()
        computer_card = draw_card()
        if user_card == 11 and user_score+user_card > 21:
            user_card = 1
        user_cards.append(user_card)
        user_score += user_card
        if computer_card == 11 and computer_score+user_card > 21:
            computer_card = 1
        computer_score += computer_card
        computer_cards.append(computer_card)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    while True:
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw == "y":
            user_card = draw_card()
            if check(user_score) and check(computer_score):
                break
            if user_card == 11 and user_score + user_card > 21:
                user_card = 1
            user_score += user_card
            user_cards.append(user_card)
            print(f"Your final hand: {user_cards}, final score: {user_score}")
        else:
            break
    while not check(computer_score) and computer_score<17:
        computer_card = draw_card()
        if computer_card == 11 and computer_score + computer_card > 21:
            computer_card = 1
        computer_score += computer_card
        computer_cards.append(computer_card)
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    
    if user_score > 21:
        print("You went over. Opponent Wins!")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score == computer_score and user_score>21:
        print("Draw!")
    elif user_score == 21:
        print("You got blackjack, You Win!")
    elif computer_score == 21:
        print("Opponent got blackjack. Opponent Wins!")
    elif user_score>computer_score:
        print("You Win!")
    elif computer_score>user_score:
        print("You Lose!")
    else:
        print("Draw!")
    
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == "y":
        print("\n"*20)
    else:
        break
