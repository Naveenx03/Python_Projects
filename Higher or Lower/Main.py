import random
from art import logo,vs
from game_data import data

def check(a, b, guess):
    if a>b:
        return guess == "A"
    return guess == "B"

def format_account(account, serial):
    return f"Compare {serial}: {account['name']}, {account['description']}, {account['country']}."

def game():
    print(logo)
    score = 0
    while True:
        q1_no = random.choice(data)
        q2_no = random.choice(data)

        while q1_no == q2_no:
            q2_no = random.choice(data)

        q1 = format_account(q1_no, "A")
        q2 = format_account(q2_no, "B")

        q1_follower = q1_no['follower_count']
        q2_follower = q2_no['follower_count']

        print(q1)
        print(vs)
        print(q2)

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if check(q1_follower, q2_follower, choice):
            score += 1
            print("\n" * 20)
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            print("\n" * 20)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break



game()
