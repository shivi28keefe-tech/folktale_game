room = 'starting'
statues = 0
game_running = True
while game_running:
    if room == 'starting':
        print (" ")
        print ("Welcome, trainee. You have entered the grounds of your 1st trial: Güllen Dungeon. Your mission is to escape.")
        print (" ")
        print ("To your left, you see a locked door with 2 empty slots. To your right, you see a stairwell leading down to a large room.")
        print ("If you want to try to unlock the door, enter '1'. To go down the stairwell, enter '2'.")
        print (" ")

        answer = input ("Which do you select? ")
        if answer == "1":
            room = "door"
        elif answer == "2":
            room = "large"
        else:
            print (" ")
            print ("Invalid input entered")
    elif room == "door":
        if statues >= 2:
            print ("You hear whirling through the door and the door creakes open.")
            print ("Well done. You have succeeded on your 1st mission. Onwards, Agent.")
            game_running = False
        else:
            print (" ")
            print ("You must acquire 2 statues to unlock this door. You possess " + str(statues) + " at the moment.")
            room = 'starting'
    elif room == "large":
        print (" ")
        print ("You enter the large room down the stairs.")
        print (" ")
        print ("On the wall in front of you, a photo and a piece of text hangs, and a typewriter sits on a table under it.")
        print ("On your right, you see a locked, wooden case and 4 buttons; a screen above it displays a question.")
        print (" ")
        print ("Enter '1' to go closer to the typewriter and photo+text frame. Enter '2' to attempt the question on your right. Enter '3' to go back up to the staring room.")
        print (" ")

        answer = input ("Which do you select? ")

        if answer == '1':
            room = "anagram"
        elif answer == '2':
            room = "question"
        elif answer == '3':
            room = 'starting'
        else:
            print (" ")
            print ("Invalid input entered")
    elif room == "anagram":
        print (" ")
        print ("Nearer to the frame, you see the photo is of the painting 'The Mona Lisa'.")
        print ("The piece of text scribbled under it reads 'O, Draconian Devil'. You realize this is an anagram and try to solve it.")
        print (" ")

        answer = input("Type your answer on the typewriter: ").lower()

        if answer == "leonardo da vinci":
            print (" ")
            print ("A hidden compartment under the table shoots open and a bronze statue falls out. You pick it up.")
            statues += 1
            room = 'large'
        else:
            print (" ")
            print ("Nothing happens. Try again.")
            answer = input("Unlock hint? Type 'yes' or 'no': ").lower()
            if answer == 'yes':
                print (" ")
                print ("Hint: The Da Vinci Code")
                room = "anagram"
            elif answer == 'no':
                room = "anagram"
            else:
                print (" ")
                print ("We take that as a 'no'.")
                room = "anagram"
    elif room == "question":
        print (" ")
        print ("The question asks:")
        print ("What color is the sky, mi amor?")
        print (" ")
        print ("The 4 buttons are all of different colors: Purple, Blue, Red, and Orange")
        print (" ")

        answer = input ("Which button do you choose to press? ").lower()
        if answer == 'purple' or answer == 'blue' or answer == 'orange':
            print (" ")
            print ("The room shakes, you have a panic attack, but the wooden box doesn't open. Try again.")
            answer = input("Unlock hint? Type 'yes' or 'no': ").lower()
            if answer == 'yes':
                print (" ")
                print ("Hint: The 'mi amor' is the hint, dear uncultured participant.")
                room = "question"
            elif answer == 'no':
                room = "question"
            else:
                print (" ")
                print ("We take that as a 'no'.")
                room = "question"
        elif answer == "red":
            print (" ")
            print ("The song 'Un Poco Loco' plays and the wooden case lifts open to reveal a bronze statue. You pick it up.")
            statues += 1
            room = "large"
        else:
            print ("Invalid input entered")
    print (" ")