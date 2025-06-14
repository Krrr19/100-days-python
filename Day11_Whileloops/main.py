import random

while True:
    player_name = input("Enter your name: ")
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0
    max_attempts = 6

    print("🎯 I'm thinking of a number between 1 and 100.")
    print(f"🧠 You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        try:
            guess = int(input("👉 Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.\n")
        elif guess > secret_number:
            print("📈 Too high! Try again.\n")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} tries! 🥳")
            result = "Win"
            break
    else:
        print(f"💥 You’ve run out of attempts. The number was {secret_number} 😢")
        result = "Loss"

    # Write result to scores.txt
    with open("scores.txt", "a") as file:
        if result == "Win":
            file.write(f"Player: {player_name} | Result: Win | Attempts: {attempts}\n")
        else:
            file.write(f"Player: {player_name} | Result: Loss | Secret number was: {secret_number}\n")

    # Ask for next action
    new_player = input("👤 Would a new player like to play? (yes/no): ").lower()
    if new_player != "yes":
        print("👋 Thanks for playing! See you next time!")
        break
