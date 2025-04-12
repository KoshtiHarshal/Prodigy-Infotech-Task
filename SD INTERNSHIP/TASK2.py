import random

def guessing_game():
    print("🎯 Welcome to the Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempt(s).")
                break
        except ValueError:
            print("🚫 Invalid input. Please enter a number.")

if __name__ == "__main__":
    guessing_game()
