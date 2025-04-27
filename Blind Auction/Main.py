from art import logo
print(logo)
bidders = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    if bid < 0:
        print("Invalid input!")
        break
    bidders[name] = bid
    otherBidder = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if otherBidder != "yes" and otherBidder != "no":
        print("Invalid input")
    if otherBidder == "no":
        break
    print("\n"*20)
winner = ""
n = 0
for key,value in bidders.items():
    if value > n:
        n = value
        winner = key
print(f"The winner is {winner} with a bid of ${n}")

