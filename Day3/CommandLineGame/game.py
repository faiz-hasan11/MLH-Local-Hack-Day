import random


def mistakes0():
    print("  |------|-")
    print("  |      | ")
    print("  |        ")
    print("  |        ")
    print("  |        ")
    print("  |        ")
    print(" /|\\       ")
    print("/ | \\      ")


def mistakes1():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |        ")
    print("  |        ")
    print("  |        ")
    print(" /|\\       ")
    print("/ | \\      ")


def mistakes2():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |      | ")
    print("  |      |  ")
    print("  |        ")
    print(" /|\\       ")
    print("/ | \\      ")


def mistakes3():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /| ")
    print("  |      | ")
    print("  |        ")
    print(" /|\\       ")
    print("/ | \\      ")


def mistakes4():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /|\\")
    print("  |      | ")
    print("  |        ")
    print(" /|\\       ")
    print("/ | \\      ")


def mistakes5():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /|\\")
    print("  |      | ")
    print("  |     /  ")
    print(" /|\\       ")
    print("/ | \\      ")


def mistakes6():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /|\\")
    print("  |      | ")
    print("  |     / \\")
    print(" /|\\       ")
    print("/ | \\      ")


def game_status():
    if mistakes == 0:
        mistakes0()
    elif mistakes == 1:
        mistakes1()
    elif mistakes == 2:
        mistakes2()
    elif mistakes == 3:
        mistakes3()
    elif mistakes == 4:
        mistakes4()
    elif mistakes5 == 5:
        mistakes5()
    else:
        mistakes6()

    print("Word:", end="")
    for element in guesses:
        print(element + " ", end="")
    print("\nRemaining Guesses:" + str(remaning_guesses))


words = ["MLH", "Local", "Hack", "Day", "Major",
         "League", "Hackathon", "Blahaj", "Project"]
guesses = []
remaning_guesses = 5
mistakes = 0
word_index = random.randint(0, len(words))
word = words[word_index].upper()

for i in range(len(word)):
    guesses.append("_")

game_over = False

while not game_over:
    game_status()
    user_input = input("PLease Enter a letter\n")
    if not user_input:
        print("Not a Valid Input.Re Enter")
    else:
        letter = user_input[0].upper()
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guesses[i] = letter
            if "_" not in guesses:
                game_over = True
        else:
            print("Sorry Not Part of the Word")
            remaning_guesses -= 1
            mistakes += 1
            if mistakes == 6:
                game_over = True
if mistakes == 6:
    game_status()
    print("You Lost.The word was " + word)
else:
    print("Hurray!You Won.The word was " + word)
