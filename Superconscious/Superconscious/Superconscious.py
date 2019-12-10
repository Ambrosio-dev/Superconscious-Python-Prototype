import os
global drawerTest
global screwdriverTaken
global gasMaskTaken
global iAmSuperconscious 
global dead
global cookedSpam
global cookedAntidote
global inventory

def game_title():
    print("SUPERCONSCIOUS")

def game_intro():
    global player_name
    print("Welcome to SUPERCONSCIOUS")
    print("This is a text adventure game. \nYou will select from various options by typing the corresponding number followed by the enter key. \nTell us your name and we will begin the game: ")
    try:
       player_name = input()
    except ValueError:
       print("Please enter a valid name.")
       print("\n") 
    os.system('cls') 

def game_over():
    print("\nGAME OVER")

def myInventory():
        print("\n".join(inventory))

def room_1_1():
    adv = 1
    adv1 = 1
    os.system('cls') 
    print("A loud creak of metal- an echo. \nYou open your eyes upon hearing the noise but all you can see is black.")
    while adv == 1:
        print("\nWhat do you do?\n")
        print("1: Try walking out")
        print("2: Feel the walls for a switch")
        try:
            val = input()
            val = int(val)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        print("\n")
        os.system('cls')  
        if val == 1:   
            print("You feel your body swaying back and forth. \nIt's as if the floor were moving. \nYou run into a door. ")
            while adv1 == 1:
                print("\nWhat do you do?\n")
                print("1: RETURN")
                print("2: Try to open it")
                try:
                    val1 = input()
                    val1 = int(val1)
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
                print("\n")
                os.system('cls')  
                if val1 == 2:
                     print("It's locked. You feel a numbered padlock attached to the handle.")
                     adv1 = 0
                     continue
                if val1 == 1:   
                     adv1 = 0
                     continue
            if adv1 == 0:
                adv1 = 1
                continue
        if val == 2:
            adv = 0
            break
        else:
            print("Please enter one of the listed numbers.\n")

def room_1_2():
    global drawerTest
    global inventory
    inventory = ['INVENTORY:']
    adv = 1
    adv1 = 1
    val = 1
    val1 = 1
    drawerTest = 0
    key = False
    code = False
    print("Your hand moves across a switch and flicks it. \nThe lights are now on and you can see the room clearly. \nThe walls are rusty metal, with some of the paneling peeling off. \nThere is a bed pushed up against the wall. \nA desk is opposite to it, with a filing cabinet sitting to the side. \nThe 3rd wall has a sink and toilet. \nAnd the final wall has a metal door with a handle and keyhole. \nThe whole room shifts back and forth, as though you were on a boat.")
    print("You can faintly see some smoggy brown gas hanging in the corners of the room. ")   
    while adv == 1:
        print("\nWhat do you do?\n")
        print("1: Use sink")
        print("2: Use toilet")
        print("3: Search desk")
        print("4: Search filing cabinet")
        print("5: Open door\n")
        print("9: Inventory")
        try:
            val = input()
            val = int(val)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        print("\n")
        os.system('cls')  
        if val == 1:
            print("Nothing happens at first, but eventually water forces itself out of the pipes. \nIt's a bit orange.")
            continue
        if val == 2:   
            print("Try as you might you cannot seem to relieve yourself.")
            continue
        if val == 3:   
            if key == False:
                print("The desk has two drawers. They're locked by a keyhole.")
                continue
            if key == True:
                        if drawerTest == 1:
                            print("It's the two drawers you opened with the key. \nYou took a vial out of one. \nThere's a note in the other.")
                        if drawerTest == 2:
                            print("It's the two drawers you opened with the key. \nThere's a vial in one and a note in the other. ")
                        if drawerTest == 0:
                            print("You use the key to open the drawers. \nThe first drawer opens to reveal some empty letter envelopes and a vial full of some sort of strange liquid.\nThe second drawer has pencils and some torn up paper.\nThere's something written on the paper. ")
                        while adv1 == 1:
                            if (drawerTest == 0) or (drawerTest == 2):
                                print("\nWhat do you do?\n")
                                print("1: RETURN")
                                print("2: Take the vial")
                                print("3: Read the paper")
                                try:
                                    val1 = input()
                                    val1 = int(val1)
                                except ValueError:
                                    print("Oops!  That was no valid number.  Try again...")
                                print("\n")
                                os.system('cls') 
                                if val1 == 2:
                                    print("You take the vial. \nUpon examining it you notice it has the word ANTIDOTE written on it.")
                                    inventory.append("Antidote Vial")
                                    drawerTest = 1
                                    continue
                                if val1 == 3:
                                    print("There are two sides to the paper")
                                    print("On one side there's a code: \n2087")
                                    print("On the other side there's a note: \nI DON'T WANT TO BE A PART OF YOU")
                                    code = True
                                    continue
                                if val1 == 1:
                                   # adv1 = 1
                                   # val1 = 0
                                    drawerTest = 2
                                    break  
                              #  else:
                               #     print("Please enter one of the listed numbers.\n")
                            if drawerTest == 1:
                                print("\nWhat do you do?\n")
                                print("1: RETURN")
                                print("2: Read the paper\n")
                                try:
                                    val1 = input()
                                    val1 = int(val1)
                                except ValueError:
                                    print("Oops!  That was no valid number.  Try again...")
                                print("\n")
                                os.system('cls') 
                                if val1 == 2:
                                    print("There are two sides to the paper")
                                    print("On one side there's a code: \n2087")
                                    print("On the other side there's a note: \nI DON'T WANT TO BE A PART OF YOU")
                                    code = True
                                    continue
                                if val1 == 1:
                             #       adv1 = 1
                              #      val1 = 0
                                    break  
                               # else:
                                #    print("Please enter one of the listed numbers.\n")
                            else:
                                print("Please enter one of the listed numbers.")
            
        if val == 4:   
            print("The filing cabinet is full of files on various people. \nThey come from various backgrounds and range from old to very young. \nYou find a file on yourself. \nIt has all the basics: where you live, birthdate, occupation, etc. \nAs you flip through it a key drops out of the file onto the floor. \nYou pick it up.  ")
            key = True
            inventory.append("Key")
            continue
        if val == 5:
            if code == False:
                print("It's locked. \nThere's a numbered padlock on the handle. \nWhat could the code be...?")
                continue
            if code == True:
                print("You put the code 2087 into the lock. \nIt clears the door handle. \nYou open the door.\n")
                adv == 0
                break
        if val == 9:
            myInventory()
      #  else:
       #     print("Please enter one of the listed numbers.\n")

def room_2():
    global drawerTest
    global screwdriverTaken
    global cookedAntidote
    global cookedSpam
    global inventory
    foundHammer = False
    brokenDoor = False
    sitCouch = False
    screwdriverTaken = False
    adv = 1
    adv1 = 1
    adv2 = 1
    adv3 = 1
    cookedAntidote = False
    cookedSpam = False
    takenSpam = False
    print("You enter into a room that is significantly cozier than the last. \nThere is carpet on the floor. \nPictures framing nature photos decorate the walls. \nThere is even a floral wallpaper, though some of it is peeling slightly. \nOne wall has a cheap upholstery couch. \nThe next has the door you entered through and a large antique wardrobe. \nThe wall opposite to it has another door, this one appears to be ajar. \nYou can see some kind of light shining through on the other side. \nTo the right of the door is a compact kitchen, with a few drawers, a gas stove with a pot, and a mini-fridge. \nThe final wall has an antique television set which is plugged into the wall. \nAs you finish looking around you realize you feel quite nauseous and your belly aches. \nIt becomes apparent to you the ground was never swaying. \nYou are just very dizzy. ")
    while adv == 1:
        print("\nWhat do you do?\n")
        print("1: Investigate the couch")
        print("2: Search the wardrobe")
        print("3: Attempt to go through the open door")
        print("4: Investigate the kitchen")
        print("5: Interact with the television")
        if foundHammer == True:
            print("6: Try to smash the door apart with the hammer")
        if brokenDoor == True:
            print("6: Go through the newly opened door space")
        print("\n9: INVENTORY\n")
        try:
            val = input()
            val = int(val)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        print("\n")
        os.system('cls')  
        if val == 1:
           if sitCouch == True:
                print("You sit down on the couch. \nYep. It's still uncomfortable. \nThe instructions you found read: \nIN ORDER TO ADMINISTER ANTIDOTE THE FLUID MUST FIRST BE BOILED THEN INJECTED INTO THE BLOODSTREAM. ")
           if sitCouch == False:
                print("You sit down on the couch. \nIt’s rough and lacks cushion. \nYou see a dirty folder sticking out underneath the couch. \nYou pick it up and leaf through it. \nThere appear to be blueprints, notes on chemistry. \nYou keep seeing the word SUPERCONSCIOUS appear again and again. \nEventually you come to a page that says ANTIDOTE. \nThere are instructions: \nIN ORDER TO ADMINISTER ANTIDOTE THE FLUID MUST FIRST BE BOILED THEN INJECTED INTO THE BLOODSTREAM. ")
                sitCouch = True
           continue
        if val == 2:   
            if screwdriverTaken == False:
                print("You find a tool kit inside. \nIt has a screwdriver and a hammer.")
            if screwdriverTaken == True:
                print("An empty wardrobe. \nYou took the toolkit with the screwdriver and hammer out of it.")
            while adv3 == 1:
                print("\nWhat do you do?\n")
                print("1: RETURN")
                if foundHammer == False:
                    print("2: Take the toolkit")
                print("\n9: INVENTORY\n")
                try:
                    val5 = input()
                    val5 = int(val5)
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
                print("\n")
                os.system('cls') 
                if val5 == 1:
                    break
                if val5 == 9:
                    myInventory()
                if foundHammer == False:
                    if val5 == 2:
                        print("You take the toolkit with the hammer and screwdriver")
                        screwdriverTaken = True
                        foundHammer = True
                        inventory.append('Screwdriver')
                        inventory.append('Hammer')
                        continue


        if val == 3:   
                print("You try to move through the door. \nIt appears to be stuck on some kind of object. \nPeeking through the doorway see sunlight and flowers. Strange. \nYou might have to bash this door down to get out.")
                continue
        if val == 4:   
            print("You look around the kitchen. \nThere's a cupboard, a stove with a pot, and a mini-fridge.")
            while adv1 == 1:
                print("\nWhat do you do?\n")
                print("1: RETURN")
                print("2: Open the cupboard")
                print("3: Open the mini-fridge")         
                if (cookedAntidote == False) and (drawerTest == 1):
                    print("4: Cook the antidote in the pot")
                if (cookedSpam == False) and (takenSpam == True):
                    print("5: Cook the SPAM in the pot")
                print("\n9: INVENTORY\n")
                try:
                    val1 = input()
                    val1 = int(val1)
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
                print("\n")
                os.system('cls')
                if val1 == 1:
                    break
                if val1 == 2:
                            while adv2 == 1:
                                if takenSpam == False:
                                    print("There's a variety of 1950s styled foods in the cupboard. \nThere's even a can of SPAM.\n \nWhat do you do?\n")
                                    print("1: RETURN")
                                    print("2: Take the SPAM")
                                    print("\n9: INVENTORY\n")
                                if takenSpam == True:
                                    print("There's a variety of 1950s styled foods in the cupboard. \n \nWhat do you do?\n")
                                    print("1: RETURN")
                                    print("\n9: INVENTORY\n")
                                try:
                                    val2 = input()
                                    val2 = int(val2)
                                except ValueError:
                                    print("Oops!  That was no valid number.  Try again...")
                                print("\n")
                                os.system('cls')
                                if takenSpam == False:
                                    if val2 == 2:
                                        print("You take the SPAM")
                                        inventory.append('SPAM')
                                        takenSpam = True
                                    if val2 == 1:
                                        adv2 = 1
                                        break
                                if takenSpam == True:
                                    if val2 == 1:
                                        adv2 = 1
                                        break
                                if val2 == 9:
                                    myInventory()
                if val1 == 3:
                    print("“How embarrassing. A house full of condiments and no real food.”")
                    continue
                if val1 == 4:
                    if cookedAntidote == False:
                        print("You boil the antidote, wait for it to cool and then put it back in the vial.")
                        cookedAntidote = True
                        inventory.append('Boiled Antidote')
                        continue
                if takenSpam == True:
                    if val1 == 5:
                        if cookedSpam == False:
                            print("You cook the SPAM in the pot and then eat it Wow. This stuff never goes bad!")
                            cookedSpam = True
                            continue
                if val1 == 3:
                        break
                if val1 == 9:
                    myInventory()
        if val == 5:   
                print("You flip on the button and knobs. \nNothing happens. \nAnd you were so sure it had power.")
                continue
        if foundHammer == True:
            if val == 6:
                print("You bash at the door over and over again, splintering the wood apart. \nOn your last blow you hit the wood so hard it shatters apart, but so does the hold of your hammer, \nseparating the metal and wood portions in pieces on the floor. \nThere is now a path through the door to the next room. ")
                brokenDoor = True
                foundHammer = False
                continue
        if brokenDoor == True:
            if val == 6:
                print("You climb over what appears to be a table that was blocking the door into the next room.")
                adv = 0
                break
        if val == 9:
            myInventory()

def room_3_1():
    global iAmSuperconscious
    global gasMaskTaken
    global inventory
    statueSpoken = False
    iVomit = False
    global cookedAntidote
    antidoteInside = False
    global cookedSpam
    foundCorpse = False
    syringeTaken = False
    gasMaskTaken = False
    firstConvo = True
    adv = 1
    adv1 = 1
    adv2 = 1
    adv3 = 1
    adv4 = 1
    askA = False
    askB = False
    askC = False
    askD = False
    askE = False
    askF = False
    askG = False
    askH = False
    askI = False
    askJ = False
    askK = False
    askL = False 
    askM = False
    askN = False
    askA1 = False
    askB1 = False
    askC1 = False
    askD1 = False
    askE1 = False
    askF1 = False
    askG1 = False
    askH1 = False
    askHI = False
    askB1Maybe = False
    askB1No = False
    askB1Yes = False
    noCheck = False
    print("You enter into a long room that appears to be some kind of greenhouse. \nLight is shining through the glass ceiling.  \nYou see a bright happy scene outside. \nA forest, running rivers. \nHow quaint. \nInside the room, plants adorn the wall and shelving, carefully taken care of and fully healthy. \nIn the middle of the hall, you see a statue of a woman made of marble. \nShe is posed carefully and elegantly like a greek goddess. \nShe is practically glowing. \nBehind you to the right you can see a hole in the wall \nwhere some heavy bushes are poking in slightly from the broken glass. \nIn addition, you now feel very sick. \nYou may throw up at any moment. ")
    while adv == 1:
        print("\nWhat do you do?\n")
        print("1: Investigate the plants")
        print("2: Approach the strange statue")
        print("3: Look through the hole in the glass")
        print("4: Vomit")
        if statueSpoken == True:
            print("5: Exit through the room behind the statue")
        if (cookedAntidote == True) and (syringeTaken == True):
            print("6: Pour the cooked antidote in the syringe")
        if antidoteInside == True:
            print("6: Inject yourself with the antidote")
        print("\n9: INVENTORY\n")
        try:
            val = input()
            val = int(val)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        print("\n")
        os.system('cls')  
        if val == 1:   
                print("Nothing seems to be out of the ordinary with them. \nThey range from fresh ripe food to beautiful flowers. \nWhoever takes care of these must love them very much.")
                continue
        if val == 2:
            if statueSpoken == False:
                print("As you approach the statue you notice there is a door behind it which leads out into the natural environment. \nBefore you are able to do anything else you hear the words HELLO THERE coming from somewhere. \nYou look up and realize the statue is talking, though its mouth is not moving.")
            if statueSpoken == True:
                print("The Superconcious acknowledges you: \n HELLO AGAIN.")
            while adv3 == 1:
                print("\nWhat do you say?\n")
                if askA == False:
                    print("1: Are you...Alive?")
                if (askB == True) and (askI == False): 
                    print("2: What is a Superconscious? What is the HOME you're talking about?")
                if askB == False:
                    print("2: Who are you?")
                if (askC == True) and (askK == False):
                    print("3: Yes, but where are we geographically? Are we underground? In a boat?")
                if (askK == True) and (askL == False):
                    print("3: Are you saying I'm not real? That this is all in my head?")
                if askC == False:
                    print("3: Where am I?")
                if askD == False:
                    print("4: Why am I here?")
                if askE == False:
                    print("5: You trapped me here didn't you?!")
                if askF == False:
                    print("6: Can you help me get out of here?")
                if (askF == True) and (askM == False):
                    print("6: What's behind the door?")
                if (askM == True) and (askN == False):
                    print("6: Is the bosom dangerous?")
                if (foundCorpse == True) and (askH == False):
                    print("7: Who is the the dead person buried in the bushes?")
                print("8: I'm done with this conversation (LEAVE CONVERSATION)")
                print("\n9: INVENTORY\n")
                try:
                    val5 = input()
                    val5 = int(val5)
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
                print("\n")
                os.system('cls')
                if askB == False:
                    if val5 == 2:
                        print("She responds as elegantly as she looks: \nWe are the Superconscious. \nWe are here to guide you on your way back home.")
                        askB = True
                        continue
                if askA == False:
                    if val5 == 1:
                        print("We certainly are. \nJust as much as you are.")
                        askA = True
                        continue
                if (askB == True) and (askI == False): 
                    if val5 == 2:
                        print("We are the Superconscious. \nAll is or will be the Superconscious. \nWe are entropy. \nWe are time.")
                        print("\nHome is the bosom of the Superconscious. \nIt is the birthplace of your renewed life. \nIt is where all souls go.")
                        askI = True
                        continue
                if (askC == True) and (askK == False):
                    if val5 == 3:
                        print("This place is an abstraction we created for your consciousness to reside while it prepared for rebirth. \nIt is not literal, but rather metaphorical. \nIn order to ease you back into us. \nEach room was meant to bring your mind further into the fold.")
                        askK = True
                        continue
                if (askK == True) and (askL == False):
                    if val5 == 3:
                        print("Consciousness with or without form has no difference. \nYour physical form is an illusion to distract you from your true place.")
                        askL = True
                        continue
                if askC == False:
                    if val5 == 3:
                        print("You are not far from our bosom. \nYou are where you should be.")
                        askC = True
                        continue
                if askD == False:
                    if val5 == 4:
                        print("You were tumorous. \nYou were hurting us. \nYour mind insisted on thinking for itself instead of with us. \nFor the benefit of all you were ejected until you were ready to return.")
                        askD = True
                        continue
                if askE == False:
                    if val5 == 5:
                        print("We have not trapped you here. \nYou are free to go whenever you please. \nWe know that eventually you will return to us.")
                        askE = True
                        continue    
                if askF == False:
                    if val5 == 6:
                        print("If you wish to leave you must find your own path out. \nWhen you are ready to rejoin with us you may step through the door at the end of this hall.")
                        askF = True
                        continue
                if (askF == True) and (askM == False):
                    if val5 == 6:
                        print("We are. The bosom. Home.")
                        askM = True
                        continue
                if (askM == True) and (askN == False):
                    if val5 == 6:
                        print("It is the opposite. It is safety.")
                        askN = True
                        continue
                if (foundCorpse == True) and (askH == False):
                    if val5 == 7:
                        print("A group came here searching. They did not find what they were looking for.")
                        askH = True
                        continue
                if val5 == 8:
                    break
                if val5 == 9:
                    myInventory()
            statueSpoken = True
            if firstConvo == True:
                print("As you turn to leave the statue representing the Superconscious begins to contort its form. \nIt moves from it's elegant position to one more natural and human-likd sitting, with one of its arms resting on its leg. \nIt speaks once more:")
                print("\nBefore you go I must ask you a few questions. That is only fair, don't you think?\n")
                while adv4 == 1:
                    if askA1 == False:
                        print("How do you respond?\n")
                    if (askB1 == False) and (askA1 == True) and (askB1No == False):
                        print("Do you plan to return to us?\n")
                    if askB1No ==True:
                        print("Would you mind telling us why not?\n")
                    if (askB1 == True) and (askC1 == False):
                        print("Does this place make you feel comfortable?\n")
                  #  if (askC1 == True) and (askD1 == False):
                     #   print("Finally, I am curious. \nSince you do not plan to return to us, where do you think you will go? \nYou are but a mere consciousness. \nThere is nothing for you beyond what we have created. \nThe rest of the world is a stretch of empty blackness. \nThis place is merely an elongation of our plane. \nAn asylum. \n")
                    if (askC1 == True): 
                        print("The statue returns to its original form as it speaks: \nWe see then. We have all that we desire from you. As a word of warning, \nif you find a vial during your stay here, destroy it. \nIt is poison and will kill you upon injection.\n")
                    if askA1 == False:
                        print("1: That seems fair enough.")
                        print("2: No. (LEAVE CONVERSATION)")
                    if (askB1 == False) and (askA1 == True) and (askB1No == False):
                        print("1: Yes")
                        print("2: No")
                        print("3: I'm not sure yet")
                    if askB1No == True:
                        print("1: I don't trust you.")
                        print("2: This is all too strange. I'm not sure this place is real.")
                        print("3: I think you're my enemy.")
                        print("4: I need more information.")
                    if (askB1 == True) and (askC1 == False):
                        print("1: No, it's creepy?")
                        print("2: No, I don't know where I am.")
                        print("3: It's tranquil. I love forests and nature.")
                        print("4: I feel safe, so yes.")
                        print("5: I'm not sure.")
                  #  if (askC1 == True) and (askD1 == False) and ((askB1No == True) or (askB1Maybe == True)):
                   #     print("1: I don't believe you. There's more here than you're letting on.")
                    #    print("2: I'll find my way out, even if it is into nothingness")
                     #   print("3: I'm not sure yet. Maybe I haven't decided.")
                    if (askC1 == True): 
                        print("1: RETURN")
                    try:
                        val6 = input()
                        val6 = int(val6)
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
                    print("\n")
                    os.system('cls')
                    if askA1 == False:
                        if val6 == 1:
                            askA1 = True
                            continue
                        if val6 == 2:
                            adv4 = 0
                            break
                    if (askB1 == False) and (askA1 == True) and (askB1No == False):
                        if val6 == 1:
                            print("That is wonderful to hear. \nDare we say it, we almost feel joy.\n")
                            askB1Yes = True
                            askB1 = True
                            continue
                        if val6 == 2:
                            #askB1 = True
                            askB1No = True
                            continue
                        if val6 == 3:
                            askB1 = True
                            #noCheck = True
                            askB1Maybe = True
                            continue
                    if askB1No == True:
                        print("Interesting...\n")
                        askB1 = True
                        askB1No = False
                        continue
                    if (askB1 == True) and (askC1 == False):
                        if (val6 == 1) or (val6 == 2) or (val6 == 5):
                            print("Ah that is such a shame. \nWe worked very hard to make a place that would make you feel at home.\n")
                            askC1 = True
                            continue
                        if (val6 == 3) or (val6 == 4):
                            print("Lovely! You have no idea how much time we spend on tumors like you.")
                            askC1 = True
                            continue
                    #if (askC1 == True) and (askD1 == False) and (noCheck == True):
                     #   askD1 = True
                     #   continue
                   # if (askC1 == True) and (askD1 == False) and (askB1Yes == True):
                   #     askD1 = True
                   #     continue
                  #  if (askD1 == True): 
                    #    if val6 == 1:
                    #        break
                    else:
                        if val6 == 1:
                             break
        if val == 3:
            if foundCorpse == False:
                print("You search through the bushes and find nothing out of the ordinary \nbesides a small black bump sticking up from the ground.") 
            if foundCorpse == True:
                print("You searched through the bushes and found a corpse here.")
            while adv1 == 1:
                print("\nWhat do you do?\n")
                print("1: RETURN")
                if foundCorpse == False:
                    print("2: Dig around the black bump")
                if foundCorpse == True:
                    print("2: Check where you dug")
                print("\n9: INVENTORY\n")
                try:
                    val1 = input()
                    val1 = int(val1)
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
                print("\n")
                os.system('cls')  
                if val1 == 1:
                    break
                if val1 == 9:
                    myInventory()     
                if val1 == 2:
                    if foundCorpse == False:
                        print("As you dig you find the arm of a person jutting out from the dirt. \nYou dig a bit further and find a face wearing a gas mask. \nThey hold something tightly in their fingers. ")
                    if foundCorpse == True:
                        print("It’s the corpse you dug up.")  
                    foundCorpse = True
                    while adv2 == 1:
                            print("\nWhat do you do?\n")
                            print("1: RETURN")
                            if syringeTaken == False:
                                print("2: Pry their fingers off of the thing they are holding")
                            if gasMaskTaken == False:
                                print("3: Take the gas mask off\n")
                            print("\n9: INVENTORY\n")
                            try:
                                val2 = input()
                                val2 = int(val2)
                            except ValueError:
                                print("Oops!  That was no valid number.  Try again...")
                            print("\n")
                            os.system('cls')
                            if val2 == 1:
                                break
                            if syringeTaken == False:
                                if val2 == 2:
                                    print("You pull the thing out. \nIt is a small medical kit. \nThere is a syringe inside. \nYou take it.")
                                    inventory.append("Syringe")
                                    syringeTaken = True
                                    continue
                            if gasMaskTaken == False:
                                if val2 == 3:
                                    print("You take the gas mask off to reveal a rotting face. \nInside the mask there are the words written on the fabric: \nDONT BREATHE THE GAS.")
                                    inventory.append("Gas Mask")
                                    gasMaskTaken = True
                                    continue
                            if val2 == 9:
                                myInventory()             
        if cookedSpam == False:
            if val == 4:
                print("You throw up. There's blood and no food in it... \nWhen was the last time you ate?")
                continue
        if cookedSpam == True:
            if val == 4:
                print("You throw up. There's blood and SPAM in it. That stuff certainly didn't make you feel any better.")
                cookedSpam == False
                continue
        if statueSpoken == True:
            if val == 5:
                print("You open the door. \nIt is pitch black ahead of you, \nand looks nothing like the seeming illusion that can be seen through the greenhouse windows.")
                while adv1 == 1:
                    print("\nWhat do you do?\n")
                    print("1: RETURN")
                    print("2: Step forward into the room \n")
                    print("\n9: INVENTORY\n")
                    try:
                        val1 = input()
                        val1 = int(val1)
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
                    print("\n")
                    os.system('cls')
                    if val1 == 1:
                        break
                    if val1 == 2:
                        adv = 0
                        iAmSuperconscious = False
                        dead = True
                        break
                    if val1 == 9:
                        myInventory()
        if cookedAntidote == True:
            if val == 6:
                print("You pour the antidote in the syringe.")
                antidoteInside = True
                cookedAntidote = False
                inventory.append('Antitode Syringe')
                continue
        if antidoteInside == True:
            if val == 6:
                print("You inject yourself with the antidote.")
                antidoteInside = False
                iAmSuperconscious = True
                break
        if val == 9:
             myInventory()

def room_3_2():
    global inventory
    adv = 1
    print("\nYou become even more dizzy. \nYou stumble back and forth, losing your footing entirely. \nYou fall to your knees. \nThen your face hits the ground. \nYou are unconscious.")
    while adv == 1:
        print("\nAwaken?\n")
        print("1: Yes")
        print("2: Sleep a little while longer\n")
        print("\n9: INVENTORY\n")
        try:
            val = input()
            val = int(val)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        print("\n")
        os.system('cls')
        if val == 1:
            break
        if val == 2:
            print("You sleep for a bit longer...")
            continue
        if val == 9:
             myInventory()

def room_3_3():
    global inventory
    global iAmSuperconscious
    global player_name
    tentacleTalk = False
    debrisPushed = False
    adv = 1
    adv1 = 1
    adv2 = 1
    print("You awaken. \nThe room is totally different. \nThe room is completely the same. \nUpon looking around you see that the layout and dimensions of the room you are now in are the same as before, \nbut just about everything else is different. \nThe room is no longer a greenhouse, but an apartment complex hallway of the same length width and height. \nDebris and rubble are everywhere. \nTo your right you see the body of the person rotting. \nIt's the same, however now you realize you must have been digging through rubble from the collapsed ceiling rather than dirt and bushes. \nIt looks like they were crushed under the weight. \nThere are no plants. \nNo windows. \nJust doors blocked by debris. \nHowever, you do notice a ventilation shaft now open in the ceiling above you. \nWhen you look down the hall, you see something horrible. \nHorrifying. \nWhere the statue once stood now there is a fleshy tentacle moving back and forth. \nThere is a doorway directly behind it.")
    while adv == 1:
        print("\nWhat do you do?\n")
        if tentacleTalk == False:
            print("1: Approach the tentacle")
        if tentacleTalk == True:
            print("1: Exit the room through the door behind the tentacle")
        if debrisPushed == False:
            print("2: Move debris towards the ventilation shaft")
        if debrisPushed == True:
            print("2: Climb up through the ventilation shaft")
        print("\n9: INVENTORY\n")
        try:
             val = input()
             val = int(val)
        except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        print("\n")
        os.system('cls')
        if tentacleTalk == True:
            if val == 1:
                print("You open the door. It is pitch black ahead of you.")
                while adv1 == 1:
                    print("\nWhat do you do?\n")
                    print("1: RETURN")
                    print("2: Step forward into the room \n")
                    print("\n9: INVENTORY\n")
                    try:
                        val1 = input()
                        val1 = int(val1)
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
                    print("\n")
                    os.system('cls')
                    if val1 == 1:
                        break
                    if val1 == 2:
                        adv = 0
                        iAmSuperconscious = False
                        dead = True
                        break
                    if val1 == 9:
                        myInventory()
                
        if tentacleTalk == False:
            if val == 1:
                print("You approach the tentacle. \nAs you do it whips itself out at you and then pulls back. \nIt softly caresses your face. \nYou can feel it thinking as it touches you: \nPLEASE COME INSIDE. COME BACK HOME. \nIt motions to the doorway behind it. ")
                tentacleTalk = True
                continue
        if debrisPushed == False:
            if val == 2:
                print("You move the debris in front of the ventilation shaft. \nYou can climb up now.")
                debrisPushed = True
                continue
        if debrisPushed == True:
            if val == 2:
                print("You climb up through the debris and leap toward the ventilation shaft. \nYou grab hold of it tightly and begin to hoist yourself upwards. \nOnce you are almost into the shaft the tentacle whips out and grabs hold of you. \nAs it touches the flesh on your ankle you can feel it thinking: \nWE WILL BE HERE WHEN YOU COME BACK. WE LOVE YOU " + player_name + ". YOU ARE A PART OF US. \nThe tentacle then recedes as you pull your leg up into the shaft. \nAs you move deeper into the space your weight shifts the ceiling and causes a collapse behind you. \nDebris fills up the hole you climbed through.")
                iAmSuperconscious = True
                while adv2 == 1:
                    print("\nWhat do you do?\n")
                    print("1: Move forward through the shaft")
                    print("2: Rest for a little while longer \n")
                    print("\n9: INVENTORY\n")
                    try:
                        val2 = input()
                        val2 = int(val2)
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
                    print("\n")
                    os.system('cls')
                    if val2 == 1:
                        adv = 0
                        break
                    if val2 == 2:
                        print("You rest for a bit.")
                        continue
                    if val2 == 9:
                        myInventory()
        if val == 9:
             myInventory()

def room_4B():
    global inventory
    global screwdriverTaken
    global dead
    dead = False
    screwdriverTaken = True
    wearingMask = False
    gasMaskTaken = True
    knifeTaken = False
    checkedBody = False
    
    adv = 1
    adv1 = 1
    adv2 = 1
    adv3 = 1
    print("You climb through the trapdoor hastily. \nThere is a ladder extending above you that seems to go on forever. \nIt is a tight space, a vertical metal tube. \nAs you work your way up it you can feel your senses becoming more and more acute. \nThere are awful noises coming from the other side of the metal. \nGushing. \nSquishing. \nAs you move further up the ladder and passage start to angle themselves sluggishly, changing from a 180* angle to 45*. \nEventually after climbing for some time you begin to notice the passage is no longer a ladder. \nYou are no longer surrounded by metal. \nYou are climbing through flesh. \nHow long? \nWhen did it change? \nIt's not clear. \nBut it is clear you can now feel and think much more acutely than just moments ago. \nAs you work through the tube of flesh you come to a fork. \nOne passage goes up further, another passage descends back down where you came. ")
    while adv == 1:
        print("\nWhat do you do?\n")
        print("1: Take the upper passage")
        print("2: Take the lower passage")
        print("\n9: INVENTORY\n")
        try:
             val = input()
             val = int(val)
        except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        print("\n")
        os.system('cls')
        if val == 1:
            print("You crawl upwards until you reach a seeming dead end. \nYou can see faint glimmers of light peeking through the soft flesh.")
            while adv == 1:
                print("\nWhat do you do?\n")
                print("1: RETURN")
                print("2: Try to tear through the flesh with your hands")

                if screwdriverTaken == True:
                    print("3: Use the screwdriver to cut through the flesh")
                if knifeTaken == True:
                    print("4: Use the knife to cut through the flesh")
                print("\n9: INVENTORY\n")
                try:
                    val1 = input()
                    val1 = int(val1)
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
                print("\n")
                os.system('cls')
                if val1 == 2:
                    print("The flesh is soft but not enough to tear through with your bare hands. \nIf only you had something that could cut through…")
                    continue
                if screwdriverTaken == True:
                    if val1 == 3:
                        print("You try to stab your way through the flesh. \nYou succeed only in creating a few whole through which fluid leaks out. \nIf only you had something that could cut through…")
                        continue
                if knifeTaken == True:
                    if val1 == 4:
                        adv = 0
                        break
                if val1 == 1:
                    break
                if val1 == 9:
                    myInventory()
        if val == 9:
            myInventory()
        if val == 2:
            print("As you descend it becomes much more difficult to see. \nYou find yourself at the entrance to a “pocket room” in this chasm of flesh. \nThe air is thick and has a smoggy brown color. ")
            while adv3 == 1:
                print("\nWhat do you do?\n")
                print("1: RETURN")
                print("2: Step into the room")
                if gasMaskTaken == True:
                    print("3: Put on the gas mask")
                print("\n9: INVENTORY\n")
                try:
                    val2 = input()
                    val2 = int(val2)
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
                print("\n")
                os.system('cls')
                if val2 == 1:
                    break
                if val2 == 2:
                    if wearingMask == True:
                         print("It’s difficult to see due to the gas and smoke. \nHowever, after a few moments you are able to acclimate. \nThe walls are made of pulsing, veiny flesh. \nThere are small knob of meat pushing out from a wall. \nOrifices on them are releasing the thick brown gas. \nAt the end of the room you can see the body of a person lying face down.")
                         while adv2 == 1:
                            print("\nWhat do you do?\n")
                            print("1: RETURN")
                            print("2: Call out to them")
                            print("3: Go investigate the body")
                            print("\n9: INVENTORY\n")
                            try:
                                val4 = input()
                                val4 = int(val4)
                            except ValueError:
                                print("Oops!  That was no valid number.  Try again...")
                            print("\n")
                            os.system('cls')
                            if val4 == 2:
                                print("Nothing happens. They are probably just sleeping.")
                                continue
                            if checkedBody == False:
                                if val4 == 3:
                                    print("You move towards the body. \nIt is completely still. \nAfter poking him for a good moment you decide to lift his face up. \nHe is wearing a gas mask which looks to have cracked or torn. \nPerhaps from a fall or other impact. \nUpon further investigation you notice that his hand has plunged a knife into his chest. \nYou pull the knife out and take it.")
                                    checkedBody == True
                                    knifeTaken = True
                                    inventory.append('Knife')
                                    continue
                            if checkedBody == True:
                                if val4 == 3:
                                    print("Still dead. Better not stick around. Might end up like them.")
                                    continue
                            if val4 == 1:
                                    break
                            if val4 == 9:
                                myInventory()
                    if wearingMask == False:
                        print("You step into the room and feel your breathing becomes short. \nYou stumble forward, landing on a rotting corpse. \nDespite trying your best to lift yourself up you pass out. \nYou don’t wake up again. ")
                        dead = True
                        adv = 0
                        break

                if gasMaskTaken == True:
                    if val2 == 3:
                        ("You put on the gas mask. ")
                        gasMaskTaken = False
                        wearingMask = True
                        continue
                if val2 == 9:
                    myInventory()

    if dead == False:        
        print("You tear through the soft flesh like melted butter with the knife. \nAs you scramble through the remaining passage daylight becomes clearer and clearer \nuntil finally you find yourself standing on the edge of a mountain of flesh.  \nTo the north you see similar geography, with some of the mountains extending and twisting into \nelaborate structures akin to DNA and RNA strands. \nTo the west you see a large body of liquid, perhaps a lake. \nIt is a familiar smoggy brown color. \nThere appears to be some kind of boat parked at the shore and a man made path which leads up \ntowards the area you are standing at. \nTo the east you see flesh towering straight up into the sky as far as the eye can see, like a monolithic wall. \nAnd finally, when you turn and look to the south you see the remnants of an old city. \nSkyscrapers and stadiums encompassed by flesh. \nIt appears the tunnel you just emerged from is growing throughout an old collapsed building. \nThere is a sign above it titled to the side. \nIt reads “RETRO APARTMENTS FOR LEASE: FULLY FURNISHED”. \nYou look up from the sign to the sky. \nIt is day, but the clouds are dark and foreboding. \nThey are lime green. \nThe sky shouldn't be green.")
        print("\nWhat do you do?\n")
        print("1: Head north towards the strand sculptures")
        print("2: Head west towards the lake and boat")
        print("3: Head east towards the towering flesh")
        print("4: Attempt to climb up and into the buildings to the south")
        print("\n9: INVENTORY\n")
        try:
                 val = input()
                 val = int(val)
        except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
        print("\n")
        os.system('cls')
        print("You head off into the distance, unsure of what the future holds for you. \nRegardless, you know in your heart that something is very, very wrong. ")
        #print("\nTO BE CONTINUED…")
        dead = True

def room_4A():
    global inventory
    print("As you step through the door shuts, leaving you surrounded by the pure pitch-black.")
    print("\nWhat do you do?\n")
    print("1: Cry for help")
    print("2: Search the walls")
    print("3: Try to open the door")
    print("4: Walk forward into the void")
    print("\n9: INVENTORY\n")
    try:
         val = input()
         val = int(val)
    except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    print("\n")
    os.system('cls')  
    print("You feel compelled to walk forward deeper into the void. \nAs you walk through the abyss your limbs transition from feeling to burning and finally numb. \nThe more you walk the less of your limbs you feel.")
    print("\nWhat do you do?\n")
    print("1: Cry for help")
    print("2: Turn around while you still can")
    print("3: Walk forward into the void")
    print("\n9: INVENTORY\n")
    try:
        val = input()
        val = int(val)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    print("\n")
    os.system('cls') 
    print("You walk forward. \nAt least .. you think that you're walking forward. \nThere's no feeling. \nAfter a long period all sense dies off. \nThere is only black. \nAs if you're looking at a blank screen. \nThen finally a subtle burst of information feeds itself into your brain: ")

    print("\n \nWELCOME HOME " + player_name)

    end = input() 

player_name = "derp"
#room_3_1()



game_intro()
room_1_1()
room_1_2()
room_2()
room_3_1()
if iAmSuperconscious == False:
    room_4A()
   # if dead == True:
    game_over()
if iAmSuperconscious == True:
    room_3_2()
    room_3_3()
    if iAmSuperconscious == False:
        room_4A()
        game_over()
    if iAmSuperconscious == True:
        room_4B()
        game_over()