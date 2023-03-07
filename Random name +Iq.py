
Riddle = "Nobody"
answer = ""
amount_of_tries_that_you_have_made = 0
max_tries = 5
out_of_guesses = False

while answer != Riddle and not(out_of_guesses):
    if amount_of_tries_that_you_have_made < max_tries:
        answer = input("Who is better than you? ")
        amount_of_tries_that_you_have_made += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("To my unfortune you've lost the game")
else:
    print("You won the game, congratulations!!!")



