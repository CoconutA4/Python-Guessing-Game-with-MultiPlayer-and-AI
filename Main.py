import random

import string

import time


def bug():
    print("Well something went wrong!, maybe u typed something wrong")
    print("Im restarting the game :)")
    time.sleep(2)
    sg()


def troll():
    print("Ok, thats not funny, stop trolling")
    print("Im restarting the game :)")
    time.sleep(2)
    sg()


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.2)
        time.sleep(.05)


def sg():
    # I - This function restarts SinglePlayer

    def restart_sp():
        user_input = input("Would you like to play again? Type 'Yes' or 'No'\n\n")

        if user_input.lower() == "no":  # Converts input to lowercase for comparison
            print("It was good while it lasted! Good bye :(")
            exit()
        if user_input.lower() == "yes":
            sp()
        else:
            print("U can only type yes or no")
            restart_sp()

    # I - This function restarts AI

    def restart_ai():
        user_input = input("Would you like to play again? Type 'Yes' or 'No'\n\n")

        if user_input.lower() == "no":  # Converts input to lowercase for comparison
            print("It was good while it lasted! Good bye :(")
            exit()
        if user_input.lower() == "yes":
            ai()
        else:
            print("U can only type yes or no")
            restart_ai()

    # I - This function restarts MultiPlayer

    def restart_mp():
        user_input = input("Would you like to play again? Type 'Yes' or 'No'\n\n")

        if user_input.lower() == "no":  # Converts input to lowercase for comparison
            print("It was good while it lasted! Good bye :(")
            exit()
        if user_input.lower() == "yes":
            mp()
        else:
            print("U can only type yes or no")
            restart_mp()

    # I - This function starts the tutorial

    def tut():
        global modeselector
        tut = input("Would you like to go trough a tutorial? (recommended) [Y/N]\n")

        if tut == "Y" or tut == "y":
            print("I see you chose to go trough the tutorial, nice choice\n")
            time.sleep(1)
            typewriter_simulator(
                "The game is quite simple, you have 3 game modes, SP (playing alone), MP (2 players) and AI (playing against the computer)\n")
            typewriter_simulator(
                "The objective is guessing a random number, generated between a limit (depends on the difficulty)\n")
            typewriter_simulator(
                "Theres 4 dificulties, 1 is from 1-20 (5 tries), 2 is from 1-100 (6 tries), 3 is from 1-250 (10 tries), and 4 from 1-400 (10 tries)\n")
            modeselector = int(input(
                "\n" + myName + " after what u were taught, would you like to play SP (1), PVP (2) or PVC (3)? \n"))
        else:
            print("No tutorial? hm ur harcore. I like it\n")

    # NI - Line  -  is pure roleplay, making the game interesting

    # NI - Using FSymbols.com to make the text

    print("░██████╗░██╗░░░██╗███████╗░██████╗░██████╗")
    print("██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝")
    print("██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░")
    print("██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗")
    print("╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝")
    print("░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░")
    # NI - Credits -> https://github.com/monkeythatprograms
    print("A python based guessing game :) by @CoconutA4")
    myName = input(
        '\nHello! traveller i see you stuped upon my guessing game. First i need to know ur name, yes i know im a stranger, but i really need to know :) \n')
    print("Owwww " + myName + ", you have a interesting name, but enought talking, lets play")

    # I - Line  -  Starting the tutorial function

    tut()

    # I - SinglePlayer Function

    def sp():
        print("\nWelcome to Single-Player\n")

        level = int(input('Pick a level of difficulty (1 to 4): '))
        if level == 1:
            top = 20
            tries = 5
        elif level == 2:
            top = 100
            tries = 6
        elif level == 3:
            top = 250
            tries = 10
        elif level == 4:
            top = 400
            tries = 10

        # create a '%' formatted string
        sf = "Well, %s, I am thinking of a number between 1 and %d"
        print(sf % (myName, top))

        # pick the random integer
        number = random.randint(1, top)
        print('Try to guess it!.')

        guessesTaken = 0
        while guessesTaken <= tries:
            guess = int(input('Take a guess: '))
            guessesTaken += 1
            if guess < number:
                print('Your guess is too low.')
            if guess > number:
                print('Your guess is too high.')
            if guess == number:
                print("Spot ON! nice guess")
                restart_sp()

        if guess == number:
            # create a '%' formatted string
            sf = "Good job, %s! You guessed my number with %d guesses!"
            print(sf % (myName, guessesTaken))
            restart_sp()

        if guess != number:
            number = str(number)
            art_over = r"""

               $$$$$$\                                           $$$$$$\                                 
               $$  __$$\                                         $$  __$$\                                
               $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$ /  $$ |$$\    $$\  $$$$$$\   $$$$$$\  
               $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\       $$ |  $$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
               $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |  $$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
               $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$ |  \$$$  /  $$   ____|$$ |      
               \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\        $$$$$$  |   \$  /   \$$$$$$$\ $$ |      
                \______/  \_______|\__| \__| \__| \_______|       \______/     \_/     \_______|\__|                                                                                         

            """
            print(art_over)
            print('Awf u have no more trys. The number I was thinking of was ' + number, "better luck next time")
            restart_sp()

    # I - Ai Function

    def ai():

        print("Hello " + myName + "!")
        print("You chose to play against ai!")
        print("Don't let the computer beat you (hes smart!) Good luck!")

        level = int(input('Pick a level of difficulty (1 to 4): '))

        if level == 1:
            top = 20
            tries = 5
        elif level == 2:
            top = 100
            tries = 6
        elif level == 3:
            top = 250
            tries = 10
        elif level == 4:
            top = 400
            tries = 10

        the_number = random.randint(1, top)
        guess = 0

        # Iniciating the limits that the computer will use
        minPossible = 0
        maxPossible = 400


        # Guessing Game - Player
        while guess != the_number:
            guess = int(input("Please enter a number: \n"))
            if guess > the_number:
                print(myName + ", guess lower...")
                if guess < maxPossible:
                    maxPossible = guess - 1
            elif guess < the_number:
                print(myName + ", guess higher...")
                if guess > minPossible:
                    minPossible = guess + 1
            else:
                art_over = r"""

                   $$$$$$\                                           $$$$$$\                                 
                   $$  __$$\                                         $$  __$$\                                
                   $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$ /  $$ |$$\    $$\  $$$$$$\   $$$$$$\  
                   $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\       $$ |  $$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
                   $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |  $$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
                   $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$ |  \$$$  /  $$   ____|$$ |      
                   \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\        $$$$$$  |   \$  /   \$$$$$$$\ $$ |      
                    \______/  \_______|\__| \__| \__| \_______|       \______/     \_/     \_______|\__|                                                                                         

                """
                print(art_over)
                print("Game Over! The number was", the_number, "," + myName + " wins!\n")
                restart_ai()

            guess = random.randint(minPossible, maxPossible)

            if level == 1:
                maxPossible < 20
            if level == 2:
                maxPossible < 100
            if level == 3:
                maxPossible < 250
            if level == 4:
                maxPossible < 400

            # Guessing Game - AI
            if guess > the_number:
                print("Ai, choose the number ", guess, "and needs to guess lower...")
                maxPossible = guess - 1
            elif guess < the_number:
                print("Ai, choose the number ", guess, "and needs to guess higher...")
                minPossible = guess + 1
            else:
                art_over = r"""

                   $$$$$$\                                           $$$$$$\                                 
                   $$  __$$\                                         $$  __$$\                                
                   $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$ /  $$ |$$\    $$\  $$$$$$\   $$$$$$\  
                   $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\       $$ |  $$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
                   $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |  $$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
                   $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$ |  \$$$  /  $$   ____|$$ |      
                   \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\        $$$$$$  |   \$  /   \$$$$$$$\ $$ |      
                    \______/  \_______|\__| \__| \__| \_______|       \______/     \_/     \_______|\__|                                                                                         

                """
                print(art_over)
                print("Game Over! The number was", the_number,
                      "The Ai wins!, im telling you, one day they will take over the world!!!!\n")
                restart_ai()

    # I - MultiPlayer Function

    def mp():
        print("\nWelcome to MultiPlayer\n")
        level = int(input('Pick a level of difficulty (1 to 4): '))
        if level == 1:
            top = 20
            tries = 5
        elif level == 2:
            top = 100
            tries = 6
        elif level == 3:
            top = 250
            tries = 10
        elif level == 4:
            top = 400
            tries = 10

        num = random.randrange(1, top)

        player1PlayCount = 0
        player2PlayCount = 0
        """enter and assign names to players"""
        player1Name = myName
        player2Name = input('Whats the second player name?\n')

        player1 = player1Name

        player2 = player2Name

        player = player1

        print(player1, 'turn')

        while ((player1PlayCount and player2PlayCount) != tries):
            guessNum = int(input("Guess Number: "))

            if guessNum == num:
                print(player, "won")
                restart_mp()
            if guessNum < num:
                print('Your guess is too low.')
            if guessNum > num:
                print('Your guess is too high.')

            elif player == player1:
                player1PlayCount += 1
                player = player2
                print(player2, 'turn')

            elif player == player2:
                player2PlayCount += 1
                player = player1
                print(player1, 'turn')

            else:
                print("Both ", player1, " and ", player2, " lose")
                restart_mp()

    # I - Calling the functions to the respective game modes

    modeselector = int(input("\n" + myName + ", would you like to play SP (1), PVP (2) or PVC (3)? \n"))

    if modeselector == 1:
        sp()
    if modeselector == 2:
        mp()
    if modeselector == 3:
        ai()
    else:
        bug()


sg()
