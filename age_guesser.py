from random import randint


def main():
    print("Hello. I am going to guess your age.")
    name = input("What's your name? ")
    total_guesses = 0
    lowest_guess = 15
    highest_guess = 30
    while total_guesses < 5:
        total_guesses += 1
        age = randint(lowest_guess, highest_guess)
        print("Are you", age, "years old?")
        correct = input("Y for yes, and N for no: ")
        if (correct == "Y"):
            print(name, "is", age, "years old.")
            return
        else:
            print("Rats.")
            delta = input("Are you older or younger? (Older/Younger): ")
            if (delta == "Older"):
                lowest_guess = age + 1
            else:
                highest_guess = age - 1
    print("I failed after 5 attempts.")


main()

# Greet you and tell you that it is going to try to guess your age.
# Ask for your name
# Guess an age between 15 and 30 and let you answer 'y' or 'n'
# If it guesses right, it exults and says "<your name> is <age> years old." and quit.
# If it guesses wrong, it says "Rats." and tries to guess again.