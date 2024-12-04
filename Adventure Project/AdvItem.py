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

    def __str__(self):
        """Converts an AdvItem to a string."""

    def get_name(self):
        """Returns the name of this item."""

    def get_description(self):
        """Returns the description of this item."""

    def get_initial_location(self):
        """Returns the initial location of this item."""

# Method to read an item from a file

def read_item(f):
    """Reads the next item from the file, returning None at the end.

    Args:
        f (file handle): the file handle of the opened item's text file
    Returns:
        (AdvItem or None): an AdvItem item or None if at end of the file
    """

