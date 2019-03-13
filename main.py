from Player import Player
from BotPlayer import BotPlayer


# True/False returns yes/no
def bool_to_english(bool):
    if bool:
        return "yes"
    else:
        return "no"


def ask_dice():
    return int(input("Enter dice number\n"))


# Asks player str, returns bool
def ask_bool(str, default):
    answer = input(str + f" (default is {bool_to_english(default)})\n")
    while True:
        if (answer.lower() == "yes") | (answer.lower() == "y"):
            return True
        elif (answer == "") | (answer.lower() == "no") | (answer.lower() == "n"):
            return False
        answer = input("Please answer blank or type yes/no or y/n\n")


if __name__ == "__main__":
    # Create human player and bot player
    player = Player()
    bot = BotPlayer()

    # Run until stopped
    run = True
    while run:
        print("Please throw the dice")
        # Player (hopefully) throws dice

        # Get dice rolls and dice hold decision
        for die in player.dice:
            if die.hold:
                die.hold = ask_bool(f"A die ({die.value}) is currently held. Release?", False)
            else:
                die.value = ask_dice()
                die.hold = ask_bool("Would you like to hold this die?", False)
        bot.think()
