# File: AdvRoom.py

"""This module is responsible for modeling a single room in Adventure."""

#########################################################################
# Your job in this assignment is to fill in the definitions of the      #
# methods listed in this file, along with any helper methods you need.  #
# The public methods shown in this file are the ones you need for       #
# Milestone #1.  You will need to add other public methods for later    #
# milestones, as described in the handout.                              #
#########################################################################

# Constants

from AdvItem import read_item
from AdvItem import AdvItem


MARKER = "-----"

class AdvRoom:

    def __init__(self, name, shortdesc, longdesc, passages, set_visited, itemsdict):
        """Creates a new room with the specified attributes.
        
        Args:
            name (str): the unique name of the room
            shortdesc (str): a short description of the room
            longdesc (list[str]): a list of strings making up a longer description
            passages (list[tuple]): a list of possible directions and
                corresponding room names
        Returns:
            None
        """
        self._name = name
        self._shortdesc = shortdesc
        self._longdesc = longdesc
        self._passages = passages
        self._set_visited = set_visited
        self._itemsdict = itemsdict


    def get_name(self):
        """Returns the name of this room."""
        return self._name

    def get_short_description(self):
        """Returns the one-line short description of this room.."""
        return self._shortdesc

    def get_long_description(self):
        """Returns the list of lines describing this room."""
        return self._longdesc

    def get_passages(self):
        """Returns the list mapping directions to names."""
        return self._passages

    def get_set_visited(self):
        """Returnes the boolean of if a room has been visited"""
        return self._set_visited
    
    def add_item(self, item):
        """Adds an item to the room"""
        itemname = item.get_item_name()
        self._itemsdict[itemname] = item


    def remove_item(self, item):
        """Removes an item from the room"""
        itemname = item.get_item_name()
        if self._itemsdict[itemname] == item:
            del self._itemsdict[itemname]
        else:
            return None

    def contains_item(self):
        """Checks to see if an item is in the room, returns True or False bool"""
        if self._itemsdict == None:
            return False
        else: return True

    def get_contents(self):
        if self._item != None:
            return self._itemsdict
        else: return None

    def item_in_room(self):
        """Returns item in the room"""
        if self._itemsdict != None:
            for item in self._itemsdict:
                return item
        else: return None

    def lit_item_in_room(self):
        if self._itemsdict != None:
            return self._itemsdict
        else: return None

    
# Method to read a room from a file


def read_room(f):
    """Reads the next room from the file, returning None at the end.

    Args:
        f (file handle): the file handle of the text file being read
    Returns:
        (AdvRoom or None): either an AdvRoom object or None if at end of file
    """
    name = f.readline().rstrip()             # Read the question name
    if name == "":                           # Returning None at the end
        return None
    shortdesc = f.readline().rstrip()
    if shortdesc == "":
        return None
    longdesc = [ ]                               # Read the question text
    finished = False
    while not finished:
        line = f.readline().rstrip()
        if line == MARKER:
            finished = True
        else:
            longdesc.append(line)
    passages = []                            # Creates a list of tuples for passages
    finished = False
    while not finished:
        line = f.readline().rstrip()
        if line == "":
            finished = True
        else:
            colon = line.find(":")
            if colon == -1:
                raise ValueError("Missing colon in " + line)
            slash = line.find("/")
            response = line[:colon].strip().upper()
            if slash == -1:
                next_room = line[colon + 1:].strip()
                keyitem = None
            else: 
                next_room = line[colon + 1:slash].strip()
                keyitem = line[slash + 1:]
            tupleadd = (response, next_room, keyitem)
            passages.append(tupleadd)
    set_visited = False
    itemsdict = {}

    return AdvRoom(name, shortdesc, longdesc, passages, set_visited, itemsdict)  # Return the completed object

