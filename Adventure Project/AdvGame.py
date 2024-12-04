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


# File: AdvGame.py

from AdvRoom import AdvRoom

class AdvGame:
    def __init__(self, prefix):
        """
        Initializes the Adventure game by reading game data from files with the given prefix.

        Args:
            prefix (str): Prefix for the game data files (e.g., "Tiny", "Small").
        """
        self.rooms = {}  # Dictionary to hold room objects keyed by their names

        # Read room data
        with open(f"{prefix}Rooms.txt", "r") as room_file:
            while True:
                room = AdvRoom.get_name(room_file)
                if room is None:
                    break
                self.rooms[room.get_name()] = room

        # Initialize starting room
        self.current_room = self.rooms.get("START", None)

    def get_room(self, name):
        """
        Returns the AdvRoom object with the specified name.

        Args:
            name (str): The unique name of a room

        Returns:
            AdvRoom: The corresponding AdvRoom object, or None if not found.
        """
        return self.rooms.get(name)

    def run(self):
        """
        Main game loop. Allows the user to navigate through the rooms using commands.
        """
        while self.current_room:
            print(self.current_room.get_description())
            command = input("> ").strip().upper()
            if command in ["QUIT", "EXIT"]:
                print("Thanks for playing!")
            next_room = self.current_room.get_next_room(command)
            if next_room:
                self.current_room = self.get_room(next_room)
            else:
                print("You can't go that way!")

