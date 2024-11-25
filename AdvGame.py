# File: AdvGame.py

"""
This module defines the AdvGame class, which records the information
necessary to play a game.
"""

###########################################################################
# Your job in this assignment is to fill in the definitions of the        #
# methods listed in this file, along with any helper methods you need.    #
# Unless you are implementing extensions, you won't need to add new       #
# public methods (i.e., methods called from other modules), but the       #
# amount of code you need to add is large enough that decomposing it      #
# into helper methods will be essential.                                  #
###########################################################################

from AdvRoom import read_room
from AdvItem import read_item
from AdvItem import AdvItem
from AdvRoom import AdvRoom

class AdvGame:

    def __init__(self, prefix):     
        """Reads the game data from files with the specified prefix and
        stores that information in attributes.

        Args:
            prefix (str): The prefix starting each of the file names
        Returns:
            None
        """
        with open(prefix + "Rooms.txt") as f:        #Creates rooms
            self._rooms = {}
            finished = False
            while not finished:
                room = read_room(f)
                if room is None:
                    finished = True
                else:
                    name = room.get_name()
                    if len(self._rooms) == 0:
                        self._rooms["START"] = room
                    self._rooms[name] = room
            

        with open(prefix + "Items.txt") as f:        #Creates items and inventory
            self._items = { }
            finished = False
            while not finished:
                item = read_item(f)
                if item is not None:
                    self._items[item.get_item_name()] = item
                else:
                    finished = True
        self._inventory = {}
        
        for item in self._items:              #Sorts items into rooms and inventory
            location = self._items[item].get_initial_location()
            if location == "PLAYER":
                self._inventory[item] = self._items[item]
            else:
                self._rooms[location].add_item(self._items[item])

        self._synonyms = {}

        with open(prefix + "Synonyms.txt") as f:          #Creates synonyms dictionary
            for line in f:
                line = line.strip()  
                if not line:  
                    continue
                if "=" in line:
                    chrkey, chrdesc = line.split("=", 1) 
                    self._synonyms[chrkey] = chrdesc
                

    def get_room(self, name):
        """Returns the AdvRoom object with the specified name.
        Args:
            name (str): the unique name of a room
        Returns:
            (AdvRoom): the corresponding AdvRoom object
        """
        for room in self._rooms:
            roomname = room.get_name()
            if roomname == name:
                return room

    def check_inventory(self):
        """Checks the player's inventory"""
        if len(self._inventory) > 0:
            print("You are carrying:")
            for item in self._inventory:
                desc = self._inventory[item].get_item_description()
                print(desc)
        else: print("You are empty-handed")

    def take_item(self):
        """Takes a certain item in a room"""

    def drop_item(self):
        """Drops a certain item into the player's current room."""
        

    def run(self):
        """Plays the adventure game stored in this object."""
        current = "START"
        printed = True
        while current != "EXIT":
            room = self._rooms[current]
            forced = False
            itemnoti2 = False
            answers = room.get_passages()
            roomitem = room.lit_item_in_room()               #Handles items
            if roomitem != None:
                itemdesc = str()
                for item in roomitem:
                    description = self._items[item].get_item_description()
                    itemdesc += description + "\n"
            else:
                itemdesc = ""
            newitemdesc = str(itemdesc)
            if newitemdesc != []:
                newitemdesc2 = newitemdesc[2:-1:]
            else:
                newitemdesc2 = ""
            if printed == True:
                if room._set_visited == False:                 #Handles short vs long descriptions based on if visited 
                    for line in room.get_long_description():
                        print(line)
                    if newitemdesc2 != "":    
                        for item in roomitem:
                            indivdesc = roomitem[item].get_item_description()
                            print("There is", indivdesc, "here")
                    room._set_visited = True
                else:
                    desc = room.get_short_description()
                    if desc != "-":
                        print(desc)
                    else:
                        desc = room.get_long_description()
                        for line in desc:
                            print(line)
                    if newitemdesc2 != "":
                        for item in roomitem:
                            indivdesc = roomitem[item].get_item_description()
                            print("There is", indivdesc, "here")
            else:
                printed = True

            for answer in answers:
                if not forced:  #Handles FORCED passages
                    if answer[0] == "FORCED" and answer[2] is not None:
                        itemforced = answer[2].upper()
                        if itemforced in self._inventory:
                            current = answer[1]
                            room = self._rooms[current]
                            for line in room.get_long_description():
                                print(line)
                            forced = True
                            printed = True
                        else:
                            itemnoti2 = True
                    elif answer[0] == "FORCED" and answer[2] is None:
                        current = answer[1]
                        if current != "EXIT":
                            room = self._rooms[current]
                        else:
                            quit()
                        for line in room.get_long_description():
                            print(line)
                        forced = True
                        printed = True
            if itemnoti2:
                print("You do not have the necessary item to enter this room.")
                continue  

            response = input("> ").strip().upper()       #Handles synonyms
            words = response.split()  
            new_response = []
            for word in words:
                if word in self._synonyms:  
                    new_response.append(self._synonyms[word]) 
                else:
                    new_response.append(word)  
            response = " ".join(new_response)  

            answers = room.get_passages()          #Handles locked rooms
            next_room = None
            passagesame = 0
            wentthruitemroom = False
            itemnoti = False
            for passage in answers:
                if passage == response:
                    passagesame += 1
            for passage in answers:
                if wentthruitemroom != True:
                    if passage[0] == response and passage[2] == None:
                        next_room = passage[1]
                    elif passage[0] == response and passage[2] != None:
                        itemneeded = passage[2].upper()
                        for item in self._inventory:
                            if str(item) == str(itemneeded):
                                next_room = passage[1]
                                wentthruitemroom = True
                            elif passagesame == 2:
                                itemnoti = True
            if itemnoti == True:
                print("You do not have the necessary item to enter this room.")


            totalitemsinroom = len(roomitem)


            if response == "HELP":      #Checks help command
                for line in HELP_TEXT:
                    print(line)
                if newitemdesc2 != "":    
                    for item in roomitem:
                        indivdesc = roomitem[item].get_item_description()
                        print("There is", indivdesc, "here")
                printed = False


            elif response == "LOOK":       #Checks look command
                for line in room.get_long_description():
                    print(line)
                if newitemdesc2 != "":
                    for item in roomitem:
                        indivdesc = roomitem[item].get_item_description()
                        print("There is", indivdesc, "here")
                printed = False


            elif response == "INVENTORY":   #Checks inventory command
                self.check_inventory()
                printed = False


            elif totalitemsinroom > 0 and response[0:4] == "TAKE":     #Checks take command
                taken = False
                removeditem = None
                if taken == False:
                    for item in roomitem:
                        itemname = roomitem[item].get_item_name()
                        if response == "TAKE " + item:
                            if self._rooms[current].contains_item() == True:
                                iteminroom = self._items[item]
                                removeditem = self._items[item]
                                self._inventory[itemname] = iteminroom
                                print("Taken.")
                                taken = True
                            else: print("This item is not in this room.")    
                        else: 
                            iteminresponse = response[5:]
                            if iteminresponse not in self._items and taken != True:
                                print("This item is not in this room.")
                                taken = True
                        printed = False
                if removeditem != None:
                    self._rooms[current].remove_item(removeditem)


            elif "DROP" in response:       #Checks drop command
                droppedstring = response[5::]
                going = True
                done = False
                for item in self._inventory:
                    if going == True:
                        if item == droppedstring:
                            itemdropped = self._inventory[item]
                            self._rooms[current].add_item(itemdropped)
                            print("Dropped.")
                            going = False
                            done = True
                    else:
                        if done == False:
                            print("There is no such item in your inventory.")
                if going == False:
                    del self._inventory[droppedstring]
                else:
                    print("There is no such item in your inventory.")
                printed = False

            elif response == "QUIT":   #Checks quit command
                quit()
                printed = False

            elif next_room is not None:
                current = next_room

            else:
                print("I don't understand that response.")
                printed = False

        quit()
            
            
# Constants

HELP_TEXT = [
    "Welcome to Adventure!",
    "Somewhere nearby is Colossal Cave, where others have found fortunes in",
    "treasure and gold, though it is rumored that some who enter are never",
    "seen again.  Magic is said to work in the cave.  I will be your eyes",
    "and hands.  Direct me with natural English commands; I don't understand",
    "all of the English language, but I do a pretty good job.",
    "",
    "It's important to remember that cave passages turn a lot, and that",
    "leaving a room to the north does not guarantee entering the next from",
    "the south, although it often works out that way.  You'd best make",
    "yourself a map as you go along.",
    "",
    "Much of my vocabulary describes places and is used to move you there.",
    "To move, try words like IN, OUT, EAST, WEST, NORTH, SOUTH, UP, or DOWN.",
    "I also know about a number of items hidden within the cave which you",
    "can TAKE or DROP.  To see what items you're carrying, say INVENTORY.",
    "To reprint the detailed description of where you are, say LOOK.  If you",
    "want to end your adventure, say QUIT."
]
