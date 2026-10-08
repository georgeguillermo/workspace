floor = 'bottom'
strength = 0
game_running = True
first_time_bottom = True
first_time_right = True
first_time_middle = True
puzzle_1 = False
puzzle_2 = False
puzzle_3 = False

while game_running:
    if floor == 'bottom':
        if first_time_bottom == True:
            print("You have found yourself at the bottom of a multi-floored dungeon. You are in an unknown room, but you see two doors, one to your left, and the other to your right.")
            print("")
            print("The door to the left has heavy breathing behind it, as if there's an enemy waiting behind the door, ready to knock you out when you open it.")
            print("")
            print("The door to the right is eerily silent, leaving the mystery of what's behind it.")
            print("")
            print("Do you choose door 1, the door to your left, or door 2, the door to your right?")
        else:
            print("You have found yourself back at the crossroads from the beginning of your journey, which door will you choose now, door 1 on the left, or door 2 on your right?")
        answer_1 = int(input(""))
        if answer_1 == 1 and strength == 0:
            print("A monster jumps out from behind the door and knocks you out, leaving you in the same room you were in before. :(")
            first_time_bottom = False
        elif answer_1 == 1 and strength != 0:
            print("You successfully battle the monster and, after fighting with all your might, manage to knock it out, leaving the monster sitting on the floor against the wall.")
            print("You have made it to the next floor! :)")
            floor = 'middle'
        if answer_1 == 2 and first_time_right == True:
            print("You have found your trusty bat and hastily put it on before any other monsters attack.")
            strength += 1
            first_time_bottom = False
            first_time_right = False
        elif answer_1 == 2 and first_time_right == False:
            print("There is nothing else except eerie silence left in this room.")
        if answer_1 != 1 and answer_1 != 2:
            print("That is not a valid door number :(.")
    if floor == 'middle':
        if first_time_middle == True:
            print("")
            print("You have found yourself in a strangely peculiar room.")
            print("")
            print("There are three doorways in front of you:")
            print("")
        elif first_time_middle == False:
            print("You are back, standing before 3 doorways with puzzles in them.")
            print("")
        print("To your right, there is a doorway with a math sign above it.")
        print("")
        print("To your left, there is a doorway with a chemistry sign above it.")
        print("")
        print("In front of you, there is a doorway with a literary sign above it, but there's an odd sense of doom coming from it, as if there's someone, or something, really powerful behind it.")
        print("")
        print("Which doorway will you go through?")
        print("1. To the right")
        print("2. To the left")
        print("3. Straight ahead")
        first_time_middle = False
        answer_1 = int(input(""))

        if answer_1 == 1:
            if puzzle_1 == False:            
                print("Before you, you see a locked glass box containing a helmet.")
                print("However, it isn't just any helmet, it's your old helmet you used to wear when going on adventures all the time")
                print("You see a sign above it that says 'Who is the inventor of Calculus?'")
                print("1. Archimedes")
                print("2. Issac Newton")
                print("3. Albert Einstein")
                print("4. Nikola Tesla")
                answer_1 = int(input(""))
                if answer_1 != 2:
                    print("An EXTREMELY loud incorrect buzzer rings throughout the entire room, shaking the floor.")
                    print("You can only assume that you got the question wrong because the glass door has not opened :(.")
                elif answer_1 == 2:
                    print("Hidden confetti cannon explode into the rooms, celebrating your correct answer!!!")
                    print("The locked glass box pops open, letting you grab your helmet!")
                    print("You put on your helmet and feel its embrace fit snugly onto your head.")
                    strength += 1
                    puzzle_1 = True
            elif puzzle_1 == True:
                print("You have already completed this puzzle, so you go back to the main room")
        if answer_1 == 2:
            print("The first thing you see is a very bright monitor that asks 'what is the element with 3 protons?'")
            print("The burning in your eyes reminds you that you haven't seen the sun in a lot of time and that this dungeon is very dimly lit.")
            print("A microphone appears before you along with a periodic table, as if wanting you to say the answer.")
        if answer_1 == 3:
            print("WIP")