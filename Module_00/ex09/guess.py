import random as rd


def print_welcome_msg():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99", end="")
    print("to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")


def check_user_guess(input):
    if input != num_to_guess:
        if input < num_to_guess:
            print("Too low!")
        else:
            print("Too High!")
        return False
    else:
        return True


def print_win(attempts):
    if num_to_guess == 42:
        print("The answer to the ultimate question", end="")
        print(" of life, the universe and everything is 42.")
    if attempts == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("Congratulations, you've got it!")
        print(f"You won in {attempts} attempts!")


def quit_game():
    print("Goodbye!")
    exit(0)


num_to_guess = rd.randint(1, 99)
print_welcome_msg()
ret = False
attempts = 0
while (not ret):
    print("What's your guess between 1 and 99?")
    input_s = input(">> ")
    if (input_s == "exit"):
        quit_game()
    try:
        input_num = int(input_s)
        ret = check_user_guess(input_num)
        attempts += 1
    except ValueError:
        print("That's not a number.")
print_win(attempts)
