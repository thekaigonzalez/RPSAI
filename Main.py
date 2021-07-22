import random

defaults = ["rock", "paper", "scissors"]


def add(integer: int):
    return integer + 1


def calculate_decision(limits: int):
    """
    Calculates the decision between the array `defaults`.
    LIMITS Decides how many times it is able to iterate through the defaults table for a more precise and genuine
    decision.

    :param limits
    :return: RANDOM CHOICE

    """
    i = 0
    n = []
    for c in defaults:
        i = add(i)  # add i and update on every tick to check for the limit
        if i == limits:  # ticks for limit
            pass
        else:
            n.append(c)  # add it to the new array
    return random.choice(n)  # Return a choice in the array


def start():

    try:
        print("choose how primitive you would like the AI to be")

        num = int(input("> "))

        GameLoop = True

        while GameLoop:
            print("choose an option ('rock', 'paper', 'scissors')")

            option = str(input(">> "))

            if option not in defaults:
                print("a valid option is required!")

            else:
                GameLoop = False  # lets not break to prevent any errors. You never know these days
        cpu = calculate_decision(num)

        # noinspection PyUnboundLocalVariable
        if cpu == option:
            print("You picked the same object! CPU Picked " + cpu + " and you picked " + option)
        else:
            if cpu == 'rock' and option == "paper":
                print("You beat me. I picked " + cpu + " and you chose " + option + ". Well done.")
            elif cpu == "paper" and option == "rock":
                print("Hah! I beat you: You picked " + option + " and I picked " + cpu)
            elif cpu == "rock" and option == "scissors":
                print("Hah! I beat you: You picked " + option + " and I picked " + cpu)
            elif cpu == 'scissors' and option == "rock":
                print("You beat me. I picked " + cpu + " and you chose " + option + ". Well done.")
            elif cpu == 'paper' and option == "scissors":
                print("You beat me. I picked " + cpu + " and you chose " + option + ". Well done.")

        print("Go Again?")
        goagain = input("y/n>")
        if goagain == "y":
            start()
        else:
            return



    except ValueError:
        print("an integer is required!")


if __name__ == '__main__':
    start()
