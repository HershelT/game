from json import load
import turtle; from tkinter import *
from Data import *; from itemsList import *; from storyAdventure import *; from monsterList import *
import random; import os; from os import system, name ; import array; import keyboard; import time; import copy; 
from gameNounsandWords import *; import string; from animationDepartment import *; 
import sys; from colorama import init; from colorama import Fore, Back, Style
def clearScreen(): 
  
    # for windows os
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux os(The name is posix)
    else: 
        _ = system('clear') 
def mapErase(i=1):    
        sys.stdout.write("\033[F"*40)
        sys.stdout.write("\n"*7)
def erases(i):
    for x in range(0, i):
        #sys.stdout.write("\033[A")
        sys.stdout.write("\033[A\033[K")
        #print("\033[A",' '*115,"\033[A")      #Need to change randomy deending on size of screen 
def objectOfCurrentBiome(): #doesnt work yet
    for bObject in buildList:
        if User["Current Biome"] == bObject.getName():
            return bObject
def loadMap(biome = False):
    if biome == False: biome = Call.biMap
    lengthC = 0; widthC = 0
    counterM = 0; ends = " "; starts = " "*65; lineMark = "\33[94m|\033[K\33[0m"
    print(" "*65,("\33[94m"+"_"*(int(biome.getWidth()*2.8))) + "\33[0m", "\033[K", flush= True)
    for row in biome.getMap():
        if lengthC > biome.getLength(): break
        for col in row:
            counterM += 1
            if counterM > biome.getWidth() - 1: ends = "\33[94m|\33[0m \n" #change for when map is different sizes
            if counterM > biome.getWidth(): break
            print(f'{starts}{lineMark}{col}',end = f"{ends}\033[K", flush= True); starts = " "; lineMark = ""
            
            widthC+=1
        counterM = 0; ends = " "; starts = " "*65; lineMark = "\33[94m|\33[0m"   
        lengthC+=1
    print(" "*64,"", "\33[94m\u203e"*(int(Call.biMap.getWidth()*2.8)),end = "\33[0m\033[K", flush= True)
    mapErase(12)
def getNumberInSentence(sentence):
    newInt = 0 #Only gets numbers in sentence/string and ignores non numbers
    for num in sentence:
        for x in range(0, 10):
            if str(x) == num:
                newInt = newInt*10 + x
    return newInt
def help():
#Maybe make it so jeffery says help
    help.ran = True
    clearScreen()
    print("-"*56)
    print("""Do to the indcredible work of Hershel Thomas, the game now allows you to naturally
talk to the game as if it was a normal conversation. The game looks for key words and phrases in order
to run the game. For example you can write 'n' to move north or you can write something along the lines of 
'I want to move forward' or 'take a step north'. Therese are just a few examples of sentences you can do
Play around with what you can and cannot do. Its awesome! 
----------------------------------------------------------------------------------------------------
You can pick up items, drop items, attack monsters, shoot arrows, check your inventory, hold weapons and wear cloths
animate the mouth of Jeffery at the top, look at your current quest or main storyline adventure. 
craft items, check in the recipe book, check a certain crafting recipe for an item by saying 
'recipe' and the name of the item in the same sentence. ('n', 'e', 's', 'w') for shorthand movement without sentences
get the users location and item info. Just remeber you can use sentences to test out which ones work and which ones dont
to get what you want, check how many monsters have been killed, or what biome you are in
most importantly exit the game with 'exit'""")
def anys(choice ,inputCase: list):
    wordle = inputCase
    if any(word in choice for word in wordle): return True
    return False
def location():
    print("Biome: {}".format(User["Current Biome"]))
    print("Location: ")
    print("North: {}".format(space[0]))
    print("East: {}".format(space[1]))

def Movement():
    direct = words["direction"]; t = Input.choice #have to check if they said move
    Movement.saveN = Movement.spotN
    Movement.saveE = Movement.spotE #Fix boundry as boundry gets larger
    
    if (("move" or "step" in t) and any(word in t.lower() for word in direct[7: 9])) or "w" == t.lower(): space[1] -= 1; t = "w"; Movement.userImage = "???"#??????????????????????????
    elif (("move" or "step" in t) and any(word in t.lower() for word in direct[0:2])) or "n" == t.lower(): space[0] += 1; t = "n"; Movement.userImage = "???"#??????/3456
    elif (("move" or "step" in t) and any(word in t.lower() for word in direct[2:4])) or "e" == t.lower(): space[1] += 1; t = "e"; Movement.userImage = "???"#??????
    elif (("move" or "step" in t) and any(word in t.lower() for word in direct[4:7])) or "s" == t.lower(): space[0] -= 1; t = "s"; Movement.userImage = "???"#??? ?????????
    #else: print("Cannot do that"); loadMap(); return False
    #if : erases(2); 
    #(TO DO) Make world randomyl generate biomes with items located in 
    bMap = Call.biMap.getMap()
    leMap = Call.biMap.getLength()
    wiMap = Call.biMap.getWidth()
    #print("Hery 1"); time.sleep(1)
    if bMap[(leMap-1)-(space[0]) % leMap][space[1] % wiMap] in blockedItems:
        if t == "n": space[0] -= 1 
        elif t == "s": space[0] += 1
        elif t == "e": space[1] -= 1 #Change maps to use object maps (Done mostly)
        elif t == "w": space[1] += 1
        Call.biMap.setStuffPos((leMap-1)-(space[0]) % leMap,space[1] % wiMap, Movement.userImage)
        #map[(leMap-1)-(space[0]) % leMap][space[1] % wiMap] = Movement.userImage
        mapErase(1);loadMap();mapErase(1)
        print("A Wall Bloks your Path");  return False
    if (space[0]< 0) or (space[0] >= 30): 
        if t == "n": space[0] -= 1 
        elif t == "s": space[0] += 1
        Call.biMap.setStuffPos((leMap-1)-(space[0]) % leMap, space[1] % wiMap, Movement.userImage)
        mapErase(1);loadMap();mapErase(1)
        print("Cannot go past boundry on north side");  return False
    elif (space[1] < -10) or (space[1] >= 20): 
        if t == "e": space[1] -= 1
        elif t == "w": space[1] += 1
        Call.biMap.setStuffPos((leMap-1)-(space[0]) % leMap, space[1] % wiMap,  Movement.userImage )
        mapErase(1);loadMap();mapErase(1)
        print("Cannot go past boundry on east side");  return False
    #Add checks to check if chacrter is on special block or wall
    #Checks if new positon is unicode value then trigger that specific command for that unicode value
    #can make dictionaries where it is named after the unicode value
    #dont run certain things if that happens make it so it returns at the end:
   # print("Debug 0.23");time.sleep(1)
    n = (space[0]) % leMap
    e = space[1] % wiMap
    Movement.spotN = (leMap-1) - n
    Movement.spotE = e
    #print("Debnug 0.65");time.sleep(1)
    try: Call.biMap.setStuffPos(Movement.saveN, Movement.saveE, Movement.pre)
    except: 1 == 1
    #print("Debug 0.82");time.sleep(1)
    map[Movement.saveN][Movement.saveE] = Movement.pre #change for whatever was the previous spot
    #print("Debug 2");time.sleep(1)
     #Works but cannot see user because map doesnt reload. 
    #cannot make it reload because texts gets overwritten
    #Movement.pre = map[Movement.spotN][Movement.spotE]
    biome = testForNewEnv() #might be problem here with what biome it is
    n = (space[0]) % biome.getLength()
    e = (space[1]) % biome.getWidth()
    #print("Debug 2.1");time.sleep(1)
    #(TO DO) Game charces when going to different sized maps like froxen lakes
    #I believe problem is that the caluclualtion is off because my location is past 15 for second 5 
    #width map and needs to compensate but figure out
    Movement.spotN = (biome.getLength()-1) - n
    Movement.spotE = e
    north = Movement.spotN
    east = Movement.spotE
    Movement.pre = biome.getStuffPos(north, east)
    #(newProblem is droped items get displayed in all places)
    biome.setStuffPos(north, east, Movement.userImage) #(Problem might be here when putting charcter on meadows)
    #map[north][east] = Movement.userImage
    #Call.biMap = biome
    loadMap()
    #print("Debug 3");time.sleep(1)
    findEnv()
    findMonster()
    findItem()
def shoot():
    #(TO DO) - Make it so different weapons can shoot faster so change time speed
     #shooting mechanic for arrows later
                            #add if statement to see if location touches a monster
    try:
        isArrow = "nothing"
        for item in User["Inventory"]:
            if "arrow" in item.lower():
                isArrow = item
                break
        if isArrow == "nothing": print("No Arrows or Range weapons in inventory"); return False
        mapErase(1)
        leMap = Call.biMap.getLength()
        wiMap = Call.biMap.getWidth()
        directionN = Movement.spotN;directionE = Movement.spotE
        firstTry = True;minusNorth = directionN;minusEast = directionE 
        counter = 0
        #would have to change for different size room 
        #Make it so it only checks when you have arrows
        #(TO DO) - Make Cleaner and condense
        if Movement.userImage == "???" :newAdd = 1;compare = directionN < leMap; test = compare
        elif Movement.userImage == "???":newAdd = -1;compare = directionN > 0; test = compare
        if Movement.userImage == "???" :newAdd = -1;compare = directionE > 1; test = compare
        elif Movement.userImage == "???":newAdd = 1;compare = directionE < (wiMap-1); test = compare
        while compare:
            if Movement.userImage == "???"or Movement.userImage == "???":
                directionN += newAdd;minusNorth = directionN - newAdd
            else: 
                directionE += newAdd;minusEast = directionE - newAdd 
            if firstTry == False: 
                Call.biMap.setStuffPos(minusNorth, minusEast, shoot.pre)
                map[minusNorth][minusEast] = shoot.pre       
            shoot.pre = Call.biMap.getStuffPos(directionN, directionE)
            if shoot.pre in blockedItems: #tests if wall to block
                break  
            map[directionN][directionE] = "??"
            Call.biMap.setStuffPos(directionN,directionE, "??")
            firstTry = False 
            if Movement.userImage == "???": compare = directionN < (leMap-1)
            elif Movement.userImage == "???": compare = directionN > 0
            if Movement.userImage == "???" : compare = directionE > 0 
            elif Movement.userImage == "???": compare = directionE < (wiMap-1)
            loadMap()
            time.sleep(0.2)
            counter+=1
        if test:
            map[directionN][directionE] = shoot.pre
            Call.biMap.setStuffPos(directionN,directionE, shoot.pre)
        else: print("Shot can't leave biome"); return False
        if counter>0: User["Inventory"].remove(isArrow)
        else: print("Shot cant shoot through walls"); return False #Maybe make certaub utens shoot through different walls
        mapErase(1);loadMap();mapErase(1)
    except: 
        print("Cant Shoot there") 
def teleport():
    try:
        tp = [0, 0]
        tpStr = Input.choice[11:-1]
        for x in range(0, 2):
            tp[x] = int(tpStr.partition(',')[x*2])
            space[x] = tp[x]
        
        
        mapErase(1)
        Movement()
        print(f"teleporting...{space}")
    except:
        print("Command Input wrong")
def specItemInfo(item):
    br = False
    for rows in itemInfo:
        for elem in rows:
            if elem in item:
                print(item + rows[elem])
                br = True
                break
        if br:
            break
def dice(start, limit):
    roll = random.randint(start, limit)
    return roll           
def attackMonster(mon):
    buff = 0; roll = 0; attackMonster.cL = 0; listI = itemBuffs[2]
    if User["Main Hand"] != "":
        for lists in itemBuffs[2]:
            if User["Main Hand"] == lists:
                listB = listI[lists]
                listBuff = listB[0]
                buff = int(listBuff)
                break
    roll = dice(1, 6); totalDG = roll + buff
    time.sleep(0.35)
    print("<------>|Attacking|<------>")
    time.sleep(0.5)
    print(f"You rolled a {roll}")
    if buff != 0: 
        time.sleep(0.5)
        print(f'And your {User["Main Hand"]} attack damage of {buff} was added to roll')
        attackMonster.cL = 1
    time.sleep(0.5)
    print(f"-->Damage done: {totalDG}")
    findMonster.HP -= totalDG
    time.sleep(0.5)
    print(f"----{mon}----\n-> Health: {findMonster.HP} <-")
    return totalDG
def monsterAttacks(mon):
    print(mon)
    #Make it so armor takes away damage from weapons, but if armor causes weapon to do no damage make it 
    #so the person always does 1 damage
def findMonster():
    findMonster.list = []; findMonster.HP = 0; findMonster.DG = 0; attack = " "; cLine = 0; findMonster.yes = False
    try: #Checks if position equals a pos of item alos checks if pick up command is used and pos is right
        for monster in monstersClear:
            if space == monstersClear[monster]:
                findMonster.yes = True
                #erases(30); animation(Call.level, True, True, False) #FIx tests to make it so it prints and you can still see it
                
                if "-" in monster: monsterN = monster.rpartition('-')[0]
                else: monsterN = monster
                findMonster.list = monMDandHP[monsterN]
                findMonster.HP = findMonster.list[1]
                findMonster.DG = findMonster.list[0]
                rewM = findMonster.list
                print(f'-------------------\nA wild {monsterN} appeard: \n <---->|Combat Mode|<---->')
                while findMonster.HP > 0:
                    if attack != "":time.sleep(0.5)
                    print(f'{monsterN} Health: {findMonster.HP}'); cLine += 1
                    print(f'{monsterN} Min Damage: {findMonster.DG}'); cLine += 1
                    if attack != "": time.sleep(0.25)
                    attack = input("Attack or Flee? (a/f) \n->"); cLine+=2
                    mapErase(1)
                    loadMap()
                    mapErase(1)
                    if "attack" in attack.lower() or "a" == attack: 
                        #erases(cLine); cLine = 0
                        print(f"You choose to attack the {monsterN}"); cLine +=1
                        attackMonster(monsterN); cLine+=5
                        cLine += attackMonster.cL
                        #choose betwene armor increasing health or preventing more damage
                    elif "flee" in attack or "f" == attack: #(TO DO): Make it so when you flee you lose damage
                        #erases(2)
                        mapErase(1)
                        loadMap()
                        mapErase(1)
                        print("-Fleeing Combat Like a COWARD-\n")
                        return 0 #Make it so when you flee you lose health #and when enemy attacks chance not to hit anf you too/
                    elif anys(attack, words["hand"]):
                        item = checkItemInfo(attack)
                        print('Mainhand: ')
                        if attack == "mainhand" or attack == "mainhand ": 
                            print(f'{User["Main Hand"]}'); cLine += 2
                        else: mainhand("MH", item); cLine += 2 
                    elif anys(attack, words["wear"]):
                        wear = checkItemInfo(attack)
                        print("Wearing: ")
                        if attack == "equip " or attack == "wear" or attack == "wear ":
                            print(f'{User["Wearing"]}'); cLine += 2
                        else: mainhand("Wear", wear); cLine += 2
                    elif "/kill" in attack: findMonster.HP = -1    
                    else:
                        cLine = 0
                #Add a return if health is below or equal to 0
                mapErase(1)
                dropProb = dice(1, 10);dropA = []
                # if dropProb >= (10 - rewM[4]): 
                dropArr = rewM[3]
                itemArr = rewM[2]
                counter = 0
                for item in itemArr:
                    dropAmount = dice(0, dropArr[counter]) + rewM[4]
                    for it in range(dropAmount):
                        dropA.append(item)
                        User["Inventory"].append(item)
                        User["InventoryCollected"].append(item) 
                    counter += 1    
                #print(dropAmount)Change dnyamix where there is no probability drop count
                #But there is more items that can drop from monster Problem is individual
                #items should have higher drop chance if they are from bosses or lower level items
                #Make it so it can drop a random item from each list or a certain amounts of items from each list
                                            #It chooses randomly which items are dropped and stuff can add another drop percantage for each item
                if dropA != []:
                    sortDrop = sortItemCount(dropA, "")
                    sortDrop = " ".join(sortDrop) 
                else: sortDrop = "Nothing"            
                #else: sortDrop = Nothing
                time.sleep(0.5)
                erases(30)
                print("<-","-"*40,"->")
                changeMessage(f"""#--|Congrats on defeating {monsterN}|--\n${monsterN} Dropped: \n$->{sortDrop}""")
                animation("Spokesman", True, False, f"    Killed {monsterN}:")
                Call.level = "Spokesman"; Call.thing = True; Call.message = f"    Killed {monsterN}:"#could add this in changeMessage board
                User["Monsters Killed"].append(monsterN)
                monstersClear.pop(monster)
                mapErase(1)
                loadMap()
                mapErase(1)
                return 0
    except:
        return 0
def mainhand(type,item):
    ch = 0
    if type == "MH": ch = 2
    if type == "Wear": ch = 1
    if item in User["Inventory"] and item != User["Main Hand"] and item != User["Wearing"]:
        for obj in itemInfo[ch]:
            if item == obj and ch == 2:
                User["Main Hand"] = item
                print(f'Putting {item} in Main Hand')
                return 0
            elif item == obj and ch == 1:  
                User["Wearing"] = item
                print(f'Equipping {item} on Body')
                return 0 
    if item == User["Main Hand"] and ch == 2: print(f'{item} already in mainhand')
    elif item in User["Wearing"] and ch == 1: print(f"Already wearing {item}") 
    elif checkItemInfo(item) == "nothing": print("Item not in game")
    elif item not in User["Inventory"]: print(f"Dont have {item} in inventory")
    elif ch == 1: print(f"Can't equip {item}")
    elif ch == 2: print(f"Can't put {item} in Mainhand")  
def findItem(): #cut it into multiple definitions so its easier with new noun system
    #Checks if location has item, then puts item in inventory and deletes item from dictionary and biome items
    #if findItem.skip == True and findItem.c != True: erases(3)
    #Checks if position equals a pos of item alos checks if pick up command is used and pos is right
    try: 
        for items in itemLoc:
            drops = list(itemLoc[items])
            if space == itemLoc[items] or space == drops[0]:
                if "DROP" in items: itemN = items.rpartition("DROP")[0]
                if "-" in items: itemN = items.rpartition('-')[0]
                else: itemN = items
                if takeItem.s: 
                    
                    #if findEnv.yes == False and findMonster.yes == False: erases(30); animation(Call.level, True, True, False)
                    #else: print(f"\n ")
                    print(f"Unbelievable, you come across a {itemN}! (Pick it up)")
                #map[9-(space[0]%10)][space[1]%10] = itemN[0]
                
                return items
        return "False"       
    except: 
        return "False"
def takeItem():
    takeItem.s, Call.erase, findItem.era  = False, False, 0
    wF, ch, item = words["itemFind"], Input.choice, findItem()
    #Make alternate for describing (DONE)
    gridI = gridItems[User["Current Biome"]]
    if "-" in item: itemN = item.rpartition('-')[0]
    else: itemN = item 
    if "DROP" in item: itemN = itemN.rpartition('DROP')[2]
    if item != "False" and anys(ch.lower() ,wF[3:]):
        
        User["Inventory"].append(itemN); User["InventoryCollected"].append(itemN)
        itemLoc.pop(item)
        #Fix for later if armor becomes array
        gridIt = list(gridI[0]); gridNum = list(gridI[1])
        for x in range(0, len(gridI[0])):
            if gridIt[x] == item:
                break
        gridNum[x] = (gridNum[x] - 1)
        if gridNum[x] == 0: 
            gridNum.pop(x)
            gridIt.pop(x); 
        if item in itemDrop:
            itemDrop.pop(item) 
        gridItems[User["Current Biome"]] = [gridIt, gridNum]
        specItemInfo(itemN)
        findItem.ItemMemory = itemN; findItem.era = 3
        # if Movement.pre == "D" and itemIsDroped:
        #     n = (space[0]) % 10; e = space[1] % 10
        #     map[9-n][e] = Movement.userImage
        itemIsDroped = False
        for drop in itemDrop:
            listDrop = itemDrop[drop]
            if space == listDrop[0]:
                Movement.pre = drop[0]
                itemIsDroped = True 
                break 
        if itemIsDroped == False:    
            Movement.pre = '\033[31m' + "*" + '\033[39m'
        mapErase(1);loadMap(); mapErase(1)
        print(f"-------PICKING UP--------\n{itemN} added to your inventory!")
        # dropItem.count -= 1
    elif item != "False": specItemInfo(itemN)
    elif anys(ch.lower(), wF[3:]): print("Nothing to pick up Man!")
    else: print("Nothing to describe over here Dude!")
    takeItem.s = True
def scatterItem(t, envir, nS, nE, eS, eE, scatter : bool):
    try:
        if "monster" in t:  
            monstersClear.clear(); t = monstersClear; 
            if storyLevel.level >= len(storyNum):
                gridI = monsters[storyNum[len(storyNum) - 1]]
            else: gridI = monsters[storyNum[storyLevel.level]]
        
        elif "item" in t:  
            t = itemLoc
            if scatter == True:
                itemLoc.clear(); 
                gridI = gridItems[envir]            
        if scatter == True:        
            itemArray = [];itemCounter = 1; stepCounter = 0; 
            itemMultipliyer = gridI[1]; 
            for item in gridI[0]:
                itemCounter = 1
                for x in range(0, itemMultipliyer[stepCounter]):
                    newItem = (f'{item}-{itemCounter}')
                    itemCounter += 1
                    itemArray.append(newItem)
                stepCounter += 1
            for items in itemArray:
                t[items] = [random.randint(nS,nE - 1), random.randint(eS,eE - 1)]
        if t == itemLoc:
            for drops in itemDrop:
                spot = itemDrop[drops]
                spotList = spot[0]
                if User["Current Biome"] in spot[1]:
                    sizes = Call.biMap
                    leMap = sizes.getLength()
                    wiMap = sizes.getWidth()
                    itemLoc[drops] = spot[0]
                    n = (spotList[0]) % leMap
                    e = spotList[1] % wiMap
                    if "Wall" in drops: Call.biMap.setStuffPos((leMap-1)-n,e,"???")#Add mechanic to destory walls. Make it so instead
                    elif "Door" in drops: Call.biMap.setStuffPos((leMap-1)-n,e,"???") #OF checking with each name make an array with all the names
                                                            #then make it so theres another array or in same 2d array it has picyure to place down
                    else: Call.biMap.setStuffPos((leMap-1)-n,e,str(drops[0]))
                    if spotList == space:
                        if "Wall" in drops: Movement.pre = "???" 
                        elif "Door" in drops: Call.biMap.setStuffPos((leMap-1)-n,e,"???")
                        else:Movement.pre = str(drops[0])      
        
    except:
        print("Did not run")
        time.sleep(5.5)
        return 0
def testForNewEnv():
    counter = 0
    for bObject in buildList:
        bounds = bObject.getCordinate()
        if not User["Current Biome"] == bObject.getName():
            if space[0] >= bounds[0] and space[0] < bounds[1] and space[1] >= bounds[2] and space[1] < bounds[3]:
                return buildList[counter] 
        counter+=1    
    return Call.biMap
    
def findEnv():
    findEnv.yes = False; counter = 0
    for bObject in buildList:
        bound = bObject.getCordinate()
        if not User["Current Biome"] == bObject.getName():
            if space[0] >= bound[0] and space[0] < bound[1] and space[1] >= bound[2] and space[1] < bound[3]:
            #Trying to make boundry lines for each qaudrant
            #Cehcks boundries for each environment location (Can save memory later by doing onyl whats touching)
                display1 = User["Current Biome"]; User["Current Biome"] = bObject.getName()
                display2 = "Entered Biome: {}".format(User["Current Biome"])
                Call.biMap = bObject
                scatterItem("item", User["Current Biome"], bound[0], bound[1], bound[2], bound[3], True)
                scatterItem("monster", User["Current Biome"], bound[0], bound[1], bound[2], bound[3], True)
                mapErase(1);loadMap();mapErase(1) 
                print(f"--------------\nLeaving Biome: {display1}\n{display2}\n--------------")
                #Make a for loop to spawn monsters from old adventures if decide to use that ma=echanic (will be  lot of monsters but can change that)
                #Can also make a loop to give each place a new random amount of monsters, super eas
                #also need to make a thing to place stuff on map
                if (not User["Current Biome"] in User["Biomes Discovered"]): 
                    User["Biomes Discovered"].append(User["Current Biome"])
                    print(f"New Biome Discovered!")
                #print(f'Monsters for Story: {s} are roaming across the land')
                arrB = [bound[0], bound[1], bound[2], bound[3]]
                return arrB 
        counter +=1                
    return False        
def itemDesc():
    #Prints out the description of items that are only in the inventory
    c = 0; t = 0; cInv = User["Inventory"][:]
    print("."*8)
    for i in itemInfo:
        for j in i:
            if j in cInv:
                print(j + itemInfo[c][j])
                t = 0
                while t < len(cInv):
                    if cInv[t] == j:
                        cInv.remove(j)
                    t += 1
        c += 1
    print("."*8)    
def arrayChecker(OG, inThis: list, lengths: list): #checks if array contains other elements by sorting them through magic
                              #use  with len function to make sure you  use apprpriate one
                              #Doesnt matter order
                                
    sortedItems = [] 
    itemIndex, count = OG, 0
    thing = inThis.copy()
    for item in OG:
        if item in itemIndex[count] and item in thing:
            sortedItems.append(item)
            thing.remove(item)
            count += 1
    if sortedItems == OG and len(OG) == len(lengths): return True
    else: return False
def craftItem(create, inp): #can Change the whole dynamic where you type in the thing you want
                       #and then it checks if you have those items in your inventory
                       #and therfore dont need to write down all items
                       #leaves room for guessing and fun, but tedious if recipes are large
                       #Can add something to display recipee book for objects
    cho = Input.choice; buildTypes = itemCraft; name = "CRAFT"
    if anys(cho.lower(), words["craft"]): buildTypes = itemCraft; 
    elif anys(cho.lower(), words["smelt"]): buildTypes = itemCook; name = "SMELT"
    if inp == False:
        creUp = string.capwords(create) 
        arrCraft = creUp.split(", ")
    userInv = False; ItemArray = False; sortedItems = False    
    for i in buildTypes:
        itemCount = sortItemCount(buildTypes[i], "add")
        if inp == False:
            ItemArray = arrayChecker(itemCount, arrCraft, arrCraft)
            sortedItems = arrayChecker(itemCount, User["Inventory"], arrCraft)
        elif create == i:
            userInv = arrayChecker(itemCount, User["Inventory"], itemCount) 
        if (ItemArray == True and sortedItems == True) or userInv == True:# Tests if arrays match up and then gets rid of items and creates new
            for ele in itemCount:
                User["Inventory"].remove(ele) 
            times = buildTypes[i]; itemList = []; tTwo = times[2]
            for x in range(tTwo[0]):
                User["Inventory"].append(i)
                User["InventoryCollected"].append(i)
                itemList.append(i)
            countItemList = sortItemCount(itemList, "None")
            print(f"|          |--[{name}ING]--|           |\n|          .............              |")
            time.sleep(0.3)
            print(f"|          [{name}ED:]                 |")
            print(f"|       {countItemList} |")
            findItem.ItemMemory = i
            return 0 
        elif ItemArray: #TO DO(Problem is for cooking you have to say final product now what you want to put in, like if i say cook iron axe, it will say cant smelt it, you have to say smelt iron ore)
                        #change for singal smelts or add new book for smelting
            print("Do not have required items in inventory for {}".format(i))
            return 0
    if inp == True: 
        if create in buildTypes: 
            print(f"Don't have enough items in inventory for {create}")
            craftRecipe(create)
            print("You only have")
            needs = []; listUI = list(User["Inventory"])
            craftItems = sortItemCount(buildTypes[create], "add")
            setUser = set(User["Inventory"])
            for i in craftItems:
                if i in setUser:
                    needs.append(f"{i} ({listUI.count(i)})")
                    setUser.remove(i)
            if needs == []: needs = "No Items"
            print(f"->{needs}")        
        else: print(f"Non craftable recipe for {create}")    
    else: print("Not a craftable recipe!")
def craftRecipe(craftable): #Describes crafting recipee for whatever you put down
    cho = Input.choice; name = "Building"; buildT = itemCraft
    if craftable in itemCook: buildT = itemCook; names = "smelt for"; name = "smelt"
    elif craftable in itemCraft: buildT = itemCraft; name = "craft"; names = "craft"
    for ele in buildT:
        if craftable == ele:
            print(f'To {names} {ele} You will need: ')
            print(sortItemCount(buildT[ele], "count"))
            return 0
    print(f"Non {name}able item") # Can write code to figure out which one        if its not in game or just not cratfable
def recipeBook(type): #make it so you can change to different recipe book and journals
    page = 1; sR = 0; eR = 4; lineDraw = True; erase = True; t = 0; cLine = 0; 
    if "Cook" in type: types= itemCook
    elif "Craft" in type: types = itemCraft
    elif "Item Locate" in type: types = itemLoc
    else: types = type
    print("")#Make a checker to see if it is a book in game
    keys = list(types)
    while True:
        if erase:
            erases(cLine+1);cLine = 0
        if lineDraw and erase:
            print(" \n----------------------: Arrow keys to move left and right");cLine+=1
        if lineDraw:
            print("Page {}".format(page));cLine+=1
        lineDraw = False
        try:   
            if erase:           
                for x in range(sR, eR-1):

                    if "Item Locate" not in type:#FIX TO MAKE ANY BOOK 
                        multType = types[keys[x]]
                        tTwo = multType[2]

                        print((f'({tTwo})'),keys[x], ": ",sortItemCount(types[keys[x]], "count")); cLine += 1
                    else:
                        print(keys[x], ":", types[keys[x]]); cLine += 1
                t = 0 
        except: t = 1
        if erase: print("---------------------: Press 'Enter' to leave book \n  "); cLine+=2 
        erase = True      
        keyboard.read_key()
        if keyboard.is_pressed("right"):
            keyboard.release("right")
            if  t == 0: sR = eR-1; eR += 3; page+=1; lineDraw = True
            else: erase = False
        elif keyboard.is_pressed("left"):
            keyboard.release("left")
            if sR - 3 > -1: eR -= 3; sR -= 3; page-=1; lineDraw = True
            else: erase = False
        elif keyboard.is_pressed("Enter"):
            input(" ")
            if (keyboard.is_pressed("Enter")): erases(1)
            return 0
        else: erase = False
def dropItem(said):
    it = checkItemInfo(said)
    if it == "nothing":
        print("item does not exist")
        return False
    elif it not in User["Inventory"]:
        print("Item not in Inventory")
        return False
    if it in User["Main Hand"]: User["Main Hand"] = "" 
    elif it in User["Wearing"]: User["Wearing"] = "" 
    gridList = gridItems[User["Current Biome"]] 
    gridItem = gridList[0]; gridNum = gridList[1]
    User["Inventory"].remove(it)
    it = (f'{it}-DROP{dropItem.count}')
    dropItem.count += 1
    itemDrop[it] = [[space[0], space[1]],[User["Current Biome"]]]
    
    gridItems[User["Current Biome"]] = [gridItem, gridNum] 
     #(TO DO) Change to use bi map so now i keep track on whatever biome I am on
        #for ele in text:
    bound = Call.biMap.getCordinate()
    # if space[0] >= bound[0] and space[0] < bound[1] and space[1] >= bound[2] and space[1] < bound[3]:
    scatterItem("item", User["Current Biome"], bound[0],bound[1],bound[2],bound[3], False)
    mapErase(1);loadMap();mapErase(1)
    leMap = Call.biMap.getLength()
    wiMap = Call.biMap.getWidth()
    if "Wall" in it: Movement.pre = "???" #Add mechanic to destory walls (???????????????????????????)
                                        #DO the array thing so each specialty item has a special object font,
                                        #like walls and doors and EVEN ANY ITem has its unique texture
    elif "Door" in it: Movement.pre = "???"
    else: Movement.pre = it[0]
    n = (space[0]) % leMap
    e = space[1] % wiMap
    Call.biMap.setStuffPos((leMap-1)-n,e, Movement.userImage)
    map[(leMap-1)-n][e] = Movement.userImage #Fix so correct letter is displayed when you pick up
    print(f"~~~Dropping {it.rpartition('-')[0].rpartition('DROP')[0]} at [{space[0]}, {space[1]}]~~~")
    return True
def addItem(item):
    x = 0; item = string.capwords(item)
    while x < len(itemInfo):
        for list in itemInfo[x]:
            if item == list:
                User["Inventory"].append(item)
                User["InventoryCollected"].append(item)
                print("Adding {} to your inventory".format(item))
                findItem.ItemMemory = item
                return 0
        x += 1
    print("Not an item in the game")    
def Info():
    print(f'Health: {User["Health"]}')
    print(f'Current Biome: \n{User["Current Biome"]}')
def invLoc(): 
    Inventory1 = copy.deepcopy(Inventory)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f'Main Hand: ({User["Main Hand"]}) \nWearing: ({User["Wearing"]})')
    for i in User["Inventory"]: #Can just do this when retrieve item so it doesnt have to use space
        CT = 0
        for j in Inventory:  
            if (test0 := (i in itemInfo[CT] and i) or
                        (i.rpartition("-")[0] in itemInfo[CT] and i.rpartition("-")[0])):
                if test0 in itemInfo[CT]:
                    Inventory1[j].append(test0)
                    break
            CT+=1  
    arrJ = []; sortU = []
    for name in Inventory: arrJ.append(name)
    for x in range(0, len(arrJ)): #fix to use itemCountSort()
        sortU = []
        for item in Inventory1[arrJ[x]]:
            itemC = (f'{item} ({Inventory1[arrJ[x]].count(item)})')
            if itemC not in sortU:
                sortU.append(itemC)
        print(f'{arrJ[x]}: {sortU}')   
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")         
def storyAdv(): #Prints out story for levek you Are on
                
                
    lev = storyLevel.level
    if lev >= len(storyNum):
        Call.level = "Spokesman"; Call.message = f"    Completed all levels"
        changeMessage(f"""#You Rock!!!\n$Lets Celebrate!!!!\n$Have a slice of cake""")
        animation("Spokesman", True, False, Call.message)
        return True
    else: 
        print(f'To complete Story: {storyNum[lev]}')
        storyList(story[storyNum[lev]] , False, 0,0,0,0,0, True)
        return False
def storyLevel(check): #Sets what level you are on. Pops all other Stories so youi only can do one Need to make deep copy
    storyLevel.skip = False
    try:
        if check == True:
            storyLevel.level += 1
            if storyLevel.level < len(storyNum):
                Call.level = storyNum[storyLevel.level]; 
                animation(storyNum[storyLevel.level], True, False, False)
                time.sleep(0.3)
                bA = User["Current Biome"]
                for bObject in buildList:
                    #for ele in text:
                        bA = bObject.getCordinate()
                        if User["Current Biome"] == bObject.getName():
                            
                            scatterItem("monster", storyNum[storyLevel.level], bA[0], bA[1], bA[2], bA[3], True)
                            time.sleep(0.3)
                            mapErase(1)
                            loadMap()
                            mapErase(1)
                            print(f"----Starting Adventure: {Call.level}----\n|\/Ferocious new Monsters Roam the Land\/|")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                input("")
                input("")
                print("\r\033[A", " "*63, "\r\033[A", " "*63)
               
                time.sleep(0.6)
                return storyNum[storyLevel.level]
    except: storyLevel.level = storyLevel.level      
    if storyLevel.level >= len(storyNum): storyAdv()
    else: return 0
def storyObjs(type): #Returns the array of items needed to achieve compeltion of level
    arrRew = type
    itemArray = []; stepCounter = 0; itemMultipliyer = arrRew[1]; 
    for item in arrRew[0]:
        if item not in itemArray:
            for x in range(0, itemMultipliyer[stepCounter]):
                itemArray.append(item)
        stepCounter += 1   
    return itemArray
def changeMessage(message) :
    t  = animations["Spokesman"]  
    animations["Spokesman"] = [t[0], message, t[2], t[3], t[4], t[5], t[6], t[7]]
def checkStoryComplete(): #Checks if completion happens, and then triggers change of level
    try:
        arrSt = sortItemCount(storyBoard[storyNum[storyLevel.level]], "add")
        monSt = sortItemCount(storyBoardMon[storyNum[storyLevel.level]], "add")
        levelNum = storyLevel.level 
        objCoLe = arrayChecker(arrSt, User["InventoryCollected"], arrSt)
        MoCoKilled = arrayChecker(monSt, User["Monsters Killed"], monSt)
        if objCoLe and MoCoKilled and levelNum + 1 <= len(storyNum):
            awardAdd = sortItemCount(storyAward[storyNum[storyLevel.level]], "add")
            awardCount = sortItemCount(storyAward[storyNum[storyLevel.level]], "count")
            erases(30) 
            time.sleep(0.2)
            clearScreen() 
            print("<-","-"*40,"->")  
            changeMessage(f"""#Congrats on completing level: {storyNum[storyLevel.level]}\n$For your acomplishment you will recieve: \n$->{awardCount}\n$(press 'f' to go to next page) """)
            animation("Spokesman", True, False, f"    Rewarding System for completing {storyNum[levelNum]}:")
            keyboard.wait('f')
            erases(20)
            print("<-","-"*40,"->")
            try:
                for item in awardAdd:
                    User["Inventory"].append(item)
            except: erases(1)
            storyLevel(True)
    except:
        return False
def sortItemCount(key, countOrAdd):
    countItemsinKey = []; counter = 0
    if "count" in countOrAdd or "add" in countOrAdd: k = key[0]; tea = True
    else: k = set(key); tea = False; listK = list(key)
    for item in k:
        if tea: count = key[1]
        if "count" in countOrAdd:
            countItemsinKey.append(f'{item} ({count[counter]})')
        elif "add" in countOrAdd:
            for x in range(0, count[counter]):
                countItemsinKey.append(item)
        else:
            countItemsinKey.append(f'{item} ({listK.count(item)})')
        counter += 1
    return countItemsinKey    
def checkItemInfo(said):
    saidObj = "nothing"
    for row in itemInfo:
        for obj in row:
            if obj in string.capwords(said):
                saidObj = obj
    return saidObj

def Call():
    
    #to save space for else statement maybe make the entire 
    #thng a for loop that checkswat you wrote against the names
    #of other functions. can store dictionary with names of all functions
    #an then they trigure the funtions assigned to dictionry
    #mamish im a genius
    com, direct = Input.choice, words["direction"]
    if "animate" in com: 
        Call.thing = False; help.ran = True
        # if not storyLevel.level >= len(storyNum):Call.level = storyNum[storyLevel.level]; 
        # else: Call.level = "Spokesman" #animation("Beginning", True, False)   
    elif anys(com.lower(), words["story"]):
        if not storyLevel.level >= len(storyNum):Call.level = storyNum[storyLevel.level]; Call.message = False
        else: Call.level = "Spokesman"; 
        Call.thing = True; help.ran = True#storyAdv()
    elif "quest" in com and "/quest" not in com: help.ran = True;Call.level = "Jeffery"; Call.thing = False; #Call.message = False#Change for quest
    skip = True
    #erases(30);  #Fix blinking issue (Fixed without system clear a lot better)!!!!!!
            #Can make a number that calculates how many lines are printed
            #dont need to rewrite quest objective every times
    
        #change for quest system later
        #Make it so cant animate anymore after reaching max quests
        #make it soa  guy tells you, you have completed the game
        #(TO DO) Make a visible board that gets printed eveyrtime
        #(TO DO) ADD chat features with the guy!!!!
    if not "animate" in com and not "quest" in com or "/quest complete" in com: Call.thing = True
    mess = False
    if not "/quest complete" in com: 
        if "quest" in com: mess = False
        else: mess = Call.message
    if help.ran == True:
        print("Help is true")
        clearScreen()
        print("<-","-"*40,"->")
        animation(Call.level, True, Call.thing, mess); help.ran = False

    if not com == "":
        #print("\033[K")
        mapErase(40)
        #animation(Call.level, True, Call.thing, mess)    
        # input("")
        # erases(1)

        loadMap(); 
    if Call.thing == False: Call.thing == True
    Call.skipe = False
    ##; findItem.skip = False; #Call.move = True
    if Input.choice == "/item locate": #Cheats for all items in game (For testing)
        print(itemLoc)
        recipeBook("Item Locate") #not really needed annoying to flip through, but cleaner
    elif com == "/item drop":
        print(itemDrop)#Maybe create recipe book for itemDrop to Super Easy
    elif com == "/item count":
        try:
            gridI = gridItems[User["Current Biome"]]
            print("Items", gridI[0], "\nCount", gridI[1])
        except: print("Unfinished items in that locations")    
    elif Input.choice == "/build locate": #Cheats for environment locations of everywhere
        for i in buildList:
            print(i.getName(),": ",i.getCordinate())
    elif com[0:9] == "/teleport": #make it later so by typing /you get list of commands
                                  #Make it so dictionary has master commands and does stuff, 
                                  #but maybe not since each command does something
        teleport()
    elif com[0:4] == "/add": addItem(com[5: ])
    #Call.level = "Jeffery"; Call.thing = False#Placeholders to test head system (Change for what quest you are doing)
        #animation("Jeffery", True, False) #Make a definition that tells you what quest you are doing
        #Or/and make a book that keeps track of all the quests you are doing
    elif com == "/clear":  
        clearScreen()
        print("<-","-"*40,"->")
        animation(Call.level, True, Call.thing, mess)    
        input("")
        erases(1)
        mapErase(1)
        loadMap()
        mapErase(1)
    elif com == "/story": #Can make system where if you kill all monsters on map you get bonus
        print(f'{storyLevel.level}\n{len(storyNum)}')
        if (storyLevel.level < len(storyNum)):
            gridI = sortItemCount(storyBoard[storyNum[storyLevel.level]], "count")
            gridMon = sortItemCount(storyBoardMon[storyNum[storyLevel.level]], "count")
            print(f'To complete {storyNum[storyLevel.level]}\nItems/Count: {gridI}')
            print(f'Monsters to kill/Count {gridMon}')
        else: print("Completed all levels")
    elif com == "/quest complete":
        if not storyLevel.level >= len(storyNum):
            Call.message = False
            questArrItem = sortItemCount(storyBoard[storyNum[storyLevel.level]], "add")
            for item in questArrItem: 
                User["Inventory"].append(item)
                User["InventoryCollected"].append(item)
            questArrMonster = sortItemCount(storyBoardMon[storyNum[storyLevel.level]], "add")
            for mon in questArrMonster: 
                User["Monsters Killed"].append(mon)
            print(f"Completing {storyNum[storyLevel.level]}")
        else: clearScreen(); print("<-","-"*40,"->");storyAdv(); mapErase(1); loadMap(); mapErase(1)      
    elif com == "/monster":
        print(monstersClear)
        if not storyLevel.level >= len(storyNum): print(sortItemCount(monsters[storyNum[storyLevel.level]], "count"))
        else: storyAdv()
    elif com == "/setMap":
        print(Call.biMap.getName())  
    elif anys(com.lower(), words["insults"]): print("You have a tiny dick")
    elif anys(com.lower(), words["shoot"]): shoot()
    elif "discover" in com: print(User["Biomes Discovered"])    
    elif "quest" in com: h = ""#Call.message = False
    elif "animate" in com: h = ""#Call.message = False;#Call.level = storyNum[storyLevel.level]; Call.thing = False#animation("Beginning", True, False)   
    elif anys(com.lower(), words["story"]): h = ""#Call.message = False#Call.level = storyNum[storyLevel.level]; Call.thing = True; #storyAdv()
    elif "help" in Input.choice: help()
    elif Input.choice == "info": Info()
    elif Input.choice == "item info": itemDesc()
    elif "drop" in com: dropItem(string.capwords(com))
    elif Input.choice == "exit": 
        while True:
            mapErase(1)
            loadMap()
            exits = input("Are you sure you want to exit ('y' or 'n')").lower()
            if exits == "y" or "yes" in exits: print("Shalom"); exit()
            elif exits == "n" or "no" in exits: break
    elif anys(com.lower(), words["recipeCraft"]) or anys(com.lower(), words["recipeCook"]):#"recipe" in com or "cook" in com or "craft" in com or "ingredient" in com : 
        #Make a list of nouns and check if {com} is any of the nouns pro strats - Done!!!!! Great invention past hershel
        choice = words["recipeCraft"] #change for recipesss
        if choice[2] == com[0: 7].lower(): print("Cant find recipe for something blank")
        elif "book" in com.lower() and anys(com.lower(), words["recipeCraft"]): recipeBook("Craft")
        elif "book" in com.lower() and anys(com.lower(), words["recipeCook"]): recipeBook("Cook")
        else: craftRecipe(checkItemInfo(com))
    elif anys(com.lower(), words["craft"]) or anys(com.lower(), words["smelt"]): #Add so you can do 'craft Bomb' an it checks if you have 
                                  #items and does same thing as craft items but dont have to type in all items\
                                  #Faster!!!1
        if checkItemInfo(com) == "nothing":     #Add user checkability to see if person is on furnace                  
            if anys(com.lower(), words["craft"]): print("Type in items you want to craft together (seperate items with ', '): ")
            else: print("Type in items you want to cook or smelt together (seperate items with ', '): ")
            craft = input("->")
            if craft != "": craftItem(craft, False); 
            else: "Crafting Nothing"
        else: craftItem(checkItemInfo(com), True)    
    elif com == "killed": killed = sortItemCount(User["Monsters Killed"], "None");print(f'Monster kill list: \n{killed}') #fix
    elif ("check" in com or "what" in com or "?" in com) and anys(com.lower(), words["hand"]): print(f'Mainhand: \n{User["Main Hand"]}')    
    elif anys(com.lower(), words["hand"]):
        if checkItemInfo(com) != "nothing": item = checkItemInfo(com)
        elif checkItemInfo(com) == "nothing" and findItem.ItemMemory != "": item = findItem.ItemMemory
        else: item = "nothing"
        mainhand("MH", item)
    elif ("check" in com or "what" in com or "?" in com) and anys(com.lower(), words["wear"]): print(f'Wearing: \n{User["Wearing"]}') 
    elif anys(com.lower(), words["wear"]) or ("put" in com.lower() and "on" in com.lower()): #maybe make it so it has to be first word
        if checkItemInfo(com) != "nothing": armor = checkItemInfo(com)
        elif checkItemInfo(com) == "nothing" and findItem.ItemMemory != "": armor = findItem.ItemMemory
        else: armor = "nothing" 
        mainhand("Wear", armor) #Problem is that is check for if item in armor not equal so if share name is 
                                #is similar like stone armor or stone then it will break (fix by changing to equal, but problem is armorwil
                                # later be an array so wont work)
    elif anys(com.lower(), words["inv"]): invLoc()
    elif anys(com.lower(), words["locate"]): location()      
    elif anys(com.lower(), direct[0:9]) or ("n"==com or"e"==com or"s"==com or"w"==com) or (("move" or "step" in com) and anys(com.lower(), direct[0:9])):
        Movement() #Fix Find item and make a definiton for any(word) so its not super long (any(com.lower() == word for word in direct[9:13]))
        #if findItem.skip == False: 
    elif anys(com.lower(), words["itemFind"]): takeItem()
    else: 
        Call.skipe = True
        if not com == "":
           # erases(2)
            print(wrongKey[random.randint(0, 4)]); Call.first = True
        else: print("\033[A\033[A"," "*63, end = "\r")
    checkStoryComplete()
    Input()        
def Input():   
    if findItem.skip != True:         
        Input.choice = input("\nAdventurer Input: ")
    findItem.skip = False    
    Call()            
Call.biMap = mapGreenland 
try:
    clearScreen()
    mess = ""
    # numList = ["???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???,"???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???","???"]
    # print(numList)
    #Call.inits = False
    #while True:
    #    clearScreen()
    #    type = input("\nAre you running this on Command Prompt or similar?\n(Windows CMD or Mac OS)\nBreaks game if given incorrect answer!!!!\n->")
    #    mess = type.lower()
    #    if "y" == mess or "yes" in mess: inits = True; Call.inits = True; break
    #    elif "n" == mess or "no" in mess: inits = False; break
    #if Call.inits == True: print("Running init")
    print("Testing...")
    time.sleep(2)
    clearScreen(); storyLevel.skip = False; Movement.userImage = "???"; help.ran = False; dropItem.count = 1
    Call.level = "Beginning"; Call.thing = True; Call.direction = True; Call.message = False; Input.f = True
    storyLevel.level = 0;findMonster.list = []; findMonster.HP = 0; findMonster.DG = 0; findItem.era  = 0
    space = [0, 0]; Movement.spotN = 9; Movement.spotE = 0; Movement.saveN = 9; Movement.saveE = 0; findItem.ItemMemory = ""; takeItem.s = True; findEnv.yes = False
    storyBC["Beginning"] = storyBoard["Beginning"][:]; Call.skipe = False
    recipeBook.choice = 1; findItem.skip = False; Call.first = True; Movement.pre = '\033[31m' + "*" + '\033[39m'
    scatterItem("item", "Greenland", 0, 9, 0, 9, True)
    scatterItem("monster", "Greenland", 0, 9, 0, 9, True)
    Input.f = False
    print("<-","-"*40,"->")
    time.sleep(0.3)
    animation("Beginning", True, False, False)
    input("")
    time.sleep(0.8)
    print("Type 'help' for help")
    time.sleep(0.2)
    #loadMap()
    Input()
except:
    print(" ")
    print("End of the Most Glorious Adventure")
   