# import modules and data

import replit
import random
import game_data
from art import logo, vs

data = game_data.data

# Create a variable to track the score
score = 0
game_over = False

# Randomly select the celebrities
celebrity_a = random.choice(data)
print(logo)

# Let the user keep playing until they get one incorrect answer
while not game_over:
    celebrity_b = random.choice(data)

    # the same celebrity could be selected
    if celebrity_a == celebrity_b:
        celebrity_b = random.choice(data)

    # Concatenate comparison string

    print(f"Compare A: {celebrity_a['name']}, a {celebrity_a['description']}, from {celebrity_a['country']}")
    print(vs)
    print(f"Against B: {celebrity_b['name']}, a {celebrity_b['description']}, from {celebrity_b['country']}")

    # Take user input
    player_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if answer is correct

    answer = str
    if celebrity_a["follower_count"] > celebrity_b["follower_count"]:
        answer = "a"
    else:
        answer = "b"

    if player_guess == answer:
        # If player chooses correct answer
        score += 1

        replit.clear()
        print(logo)
        print(f"You're right! Current score: {score}.")

        # Carry over the second option to the next round
        celebrity_a = celebrity_b

    else:
        # If incorrect answer,
        replit.clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True


