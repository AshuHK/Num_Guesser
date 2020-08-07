import time
import random


def main():
    while True:
        try:
            user_input = input("Enter a number: ")
            max_guess = int("9" * len(user_input))
            user_input = int(user_input)
            break
        except ValueError:
            pass

    guess_count = 0
    while True:
        guess = random.randint(0, max_guess + 1)
        print("{:,}".format(guess))
        guess_count += 1

        if guess == user_input:
            break

    print("It took {:,} guess(es) to randomly get {:,}".format(guess_count, user_input))

if __name__ == "__main__":
    main()

