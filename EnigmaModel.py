######################################################################
# Name: Derec
# Collaborators (If any):
# Section leader's name: Dash
# GenAI transcript (if used):
# List of extensions made (if any):
######################################################################

from EnigmaView import EnigmaView

# Constants

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR_PERMUTATIONS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Slow rotor      
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Medium rotor    
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Fast rotor      
]
REFLECTOR_PERMUTATION = "IXUHFEZDAOMTKQJWNSRLCYPBVG"  

# Helper Functions

def apply_permutation(index, permutation, offset):
    """Applies the rotor permutation while adjusting for the rotor's offset."""
    shifted_index = (index + offset) % 26
    permuted_char = permutation[shifted_index]
    new_index = ord(permuted_char) - ord('A')
    return new_index

def invert_key(key):
    """Inverts the given key (permutation)."""
    inverted = [''] * 26
    for i, char in enumerate(key):
        inverted[ord(char) - ord('A')] = chr(i + ord('A'))
    return ''.join(inverted)

# Enigma Rotor Class

class EnigmaRotor:
    """Defines a rotor for the Enigma machine."""
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverted_permutation = invert_key(permutation)
        self._offset = 0

    def get_offset(self):
        """Returns the current offset of the rotor."""
        return self._offset

    def get_permutation(self):
        """Returns the forward permutation string for the rotor."""
        return self._permutation

    def get_inverted_permutation(self):
        """Returns the inverted permutation string for the rotor."""
        return self._inverted_permutation

    def advance(self):
        """Advances the rotor by one notch, cycling back to 0 after 26."""
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

# Enigma Machine Model

class EnigmaModel:
    """The model representing the Enigma machine, including rotors and reflector."""
    def __init__(self):
        self._views = []
        self.key_states = {letter: False for letter in ALPHABET}
        self.lamp_states = {letter: False for letter in ALPHABET}
        self._rotors = [
            EnigmaRotor(ROTOR_PERMUTATIONS[0]),
            EnigmaRotor(ROTOR_PERMUTATIONS[1]),
            EnigmaRotor(ROTOR_PERMUTATIONS[2])
        ]
        self.reflector_permutation = REFLECTOR_PERMUTATION

    def add_view(self, view):
        """Adds a view to the model."""
        if isinstance(view, EnigmaView):
            self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        """Checks if a specific key is currently pressed."""
        return self.key_states.get(letter.upper(), False)

    def is_lamp_on(self, letter):
        """Returns whether the lamp corresponding to a letter is on."""
        return self.lamp_states.get(letter, False)

    def key_pressed(self, letter):
        """Records that a key has been pressed and lights up the corresponding lamp."""
        self.key_states[letter.upper()] = True
        if self._rotors[2].advance():
            if self._rotors[1].advance():
                self._rotors[0].advance()
        index = ord(letter.upper()) - ord('A')
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        index = apply_permutation(index, self.reflector_permutation, 0)
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_inverted_permutation(), rotor.get_offset())
        encrypted_letter = chr(index + ord('A'))
        self.lamp_states[encrypted_letter] = True
        self.update()

    def key_released(self, letter):
        """Records that a key has been released and turns off the corresponding lamp."""
        self.key_states[letter.upper()] = False
        index = ord(letter.upper()) - ord('A')
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        index = apply_permutation(index, self.reflector_permutation, 0)
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_inverted_permutation(), rotor.get_offset())
        encrypted_letter = chr(index + ord('A'))
        self.lamp_states[encrypted_letter] = False
        self.update()

    def get_rotor_letter(self, index):
        """Gets the letter currently visible in the rotor window."""
        rotor = self._rotors[index]
        offset = rotor.get_offset()
        return chr(offset + ord('A'))

    def rotor_clicked(self, index):
        """
        Advances the rotor when clicked.
        """
        rotor = self._rotors[index]
        rotor.advance()
        self.update()

# Enigma Machine Simulator

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup Code

if __name__ == "__main__":
    enigma()
