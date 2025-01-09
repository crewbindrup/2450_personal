from random import randint


def main():
    print("Hello. I am going to guess your age.")
    name = input("What's your name? ")
    while True:
        age = randint(15, 30)
        print("Are you ", age, " years old?")
        correct = input("Y for yes, and N for no: ")
        if (correct == "Y"):
            print(name, "is", age, "years old.")
            return
        else:
            print("Rats.")


main()

# Greet you and tell you that it is going to try to guess your age.
# Ask for your name
# Guess an age between 15 and 30 and let you answer 'y' or 'n'
# If it guesses right, it exults and says "<your name> is <age> years old." and quit.
# If it guesses wrong, it says "Rats." and tries to guess again.