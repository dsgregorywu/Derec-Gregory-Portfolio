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

MARKER = "-----"

class AdvRoom:

    def __init__(self, name, shortdesc, longdesc, passages):
        """Creates a new room with the specified attributes.
        
        Args:
            name (str): the unique name of the room
            shortdesc (str): a short description of the room
            longdesc (list[str]): a list of strings making up a longer description
            passages (dict[str:str]): a dictionary of possible directions and
                corresponding room names
        Returns:
            None
        """

    def get_name(self):
        """Returns the name of this room."""

    def get_short_description(self):
        """Returns the one-line short description of this room.."""

    def get_long_description(self):
        """Returns the list of lines describing this room."""

    def get_passages(self):
        """Returns the dictionary mapping directions to names."""

    def __init__(self, name, text, answers):
        """Creates a new TMQuestion object with these attributes."""
        self._name = name
        self._text = text
        self._answers = answers

    def get_name(self):
        """Returns the name of this question."""
        return self._name

    def get_text(self):
        """Returns the list containing the text of this question."""
        return self._text

    def get_answers(self):
        """Returns the map between a response and the next question."""
        return self._answers.copy()

# Method to read a room from a file

def read_room(f):
    """Reads the next room from the file, returning None at the end.

    Args:
        f (file handle): the file handle of the text file being read
    Returns:
        (AdvRoom or None): either an AdvRoom object or None if at end of file
    """
