# File: AdvItem.py

"""This module defines a class that models an item in Adventure."""

#########################################################################
# Your job in this assignment is to fill in the definitions of the      #
# methods listed in this file, along with any helper methods you need.  #
# You won't need to work with this file until Milestone #4.  In my      #
# solution, none of the milestones required any public methods beyond   #
# the ones defined in this starter file.                                #
#########################################################################

class AdvItem:

    def __init__(self, name, description, location):
        """Creates an AdvItem from the specified properties.

        Args:
            name (str): the unique name of the item
            description (str): a short description of the item
            location (str): the name of the location where the item first appears
        """
        self._name = name
        self._description = description
        self._location = location

    def __str__(self):
        """Converts an AdvItem to a string."""
        return str(self._name)

    def get_item_name(self):
        """Returns the name of this item."""
        return self._name

    def get_item_description(self):
        """Returns the description of this item."""
        return self._description

    def get_initial_location(self):
        """Returns the initial location of this item."""
        return self._location

# Method to read an item from a file

def read_item(f):
    """Reads the next item from the file, returning None at the end.

    Args:
        f (file handle): the file handle of the opened item's text file
    Returns:
        (AdvItem or None): an AdvItem item or None if at end of the file
    """
    name = f.readline().rstrip()             # Read the item name
    if name == "":                           
        return None
    desc = f.readline().rstrip()                #Reads item description
    if desc == "":
        return None
    oglocation = f.readline().rstrip()              # Read the orginal location of the item 
    if oglocation == "":
        return None
    emptyline = f.readline().rstrip()
    return AdvItem(name, desc, oglocation)




