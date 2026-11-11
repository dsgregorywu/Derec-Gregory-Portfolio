#include <stdio.h>
#include <string.h>

#define ALPHABET_SIZE 26 /* wow */

char plugboard[ALPHABET_SIZE] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
char rotors[3][ALPHABET_SIZE] = { 
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  /*fast*/
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  /*medium*/
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"  /*slow*/
};
char reflector[ALPHABET_SIZE] = "YRUHQSLDPXNGOKMIEBFZCWVJAT"; /*reflector*/
int rotor_positions[3] = {0, 0, 0};

void configure_plugboard(char *pairs);   /*Why do I call my functions up here w/o defining them? I could've saved like 6 lines of code.*/
char substitute_plugboard(char input);
void rotate_rotors();
char pass_through_rotors(char input, int forward);
char reflect_signal(char input);
char encrypt_character(char input);

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <message>\n", argv[0]);
        return 1;
    }
    char message[100];
    strncpy(message, argv[1], sizeof(message) - 1);
    message[sizeof(message) - 1] = '\0';
    configure_plugboard("AB CD EF");
    rotor_positions[0] = 0;
    rotor_positions[1] = 0;
    rotor_positions[2] = 0;

    for (int i = 0; message[i] != '\0'; i++) {
        if (message[i] >= 'A' && message[i] <= 'Z') {
            message[i] = encrypt_character(message[i]);
        }
    }
    printf("Encrypted: %s\n", message);
    return 0;
}

/* Functions to define !  - done now mwahahaha*/
void configure_plugboard(char *pairs) {
    /*sets up plogbord*/
    for (int i = 0; i < strlen(pairs); i += 3){
        char a = pairs[i];
        char b = pairs[i + 1];
        plugboard[a - 'A'] = b;
        plugboard[b - 'A'] = a;
    }
}

char substitute_plugboard(char input) {
    /*subs letters in plogbord */
    return plugboard[input - 'A'];
}

void rotate_rotors() {
    /* rotates rotors*/
    rotor_positions[0] = (rotor_positions[0] + 1) % ALPHABET_SIZE;
    if (rotor_positions[0] == 0){
        rotor_positions[1] = (rotor_positions[1] + 1) % ALPHABET_SIZE;
        if (rotor_positions[1] == 0){
            rotor_positions[2] = (rotor_positions[2] + 1) % ALPHABET_SIZE;
        }
    }
}

char pass_through_rotors(char input, int forward) {
    /*encrypts things but only a little*/
    int index = input - 'A';
    for (int i = 0; i < 3; i++) {
        int rotor_index = forward ? i : 2 - i;
        int pos = (index + rotor_positions[rotor_index]) % ALPHABET_SIZE;
        if (forward) {
            index = rotors[rotor_index][pos] - 'A';
        } else {
            for (int j = 0; j < ALPHABET_SIZE; j++) {
                if (rotors[rotor_index][j] - 'A' == pos) {
                    index = (j - rotor_positions[rotor_index] + ALPHABET_SIZE) % ALPHABET_SIZE;
                    break;
                }
            }
        }
    }
    return 'A' + index;
}
char reflect_signal(char input){
    /*reflects signal*/
    return reflector[input - 'A'];
}

char encrypt_character(char input){
    /*encrypts character the whole way*/
    char substituted = substitute_plugboard(input);
    substituted = pass_through_rotors(substituted, 1);
    substituted = reflect_signal(substituted);
    substituted = pass_through_rotors(substituted, 0);
    substituted = substitute_plugboard(substituted);
    rotate_rotors();
    return substituted;
}