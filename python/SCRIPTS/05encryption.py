# =======================
#    Encryption system
# =======================

from os import system  

TITLE = """
█▀▀ █▄░█ █▀▀ █▀█ █▄█ █▀█ ▀█▀ █ █▀█ █▄░█
██▄ █░▀█ █▄▄ █▀▄ ░█░ █▀▀ ░█░ █ █▄█ █░▀█ 
"""

# ======= Binary ========

# ---- Text to binary ----
def ascii_to_binary(letter):
    letter_value = ord(letter) 
    return "{0:08b}".format(letter_value)

def text_to_binary(text): 
    binary_text = "" 
    counter = 0
    for letter in text:
        binary_text += ascii_to_binary(letter) 
        if counter < len(text): 
            binary_text += " " 
        counter += 1
    return binary_text 

# ---- Binary to text ----
def binary_to_text(uinput):   
    pass 


# ======= Base 64 =======

# ---- Encode base 64 ----
def encode_base(uinput):
    pass

# ---- Decode base 64 ----
def decode_base(uinput): 
    pass


# ==== main function ====

def main():
    system("clear")
    print(TITLE) 

    chosen_option = int(input('== CHOOSE A OPTION ==\n1 = Text to binary\n2 = Binary to text\n3 = Encode Base 64\n4 = Decode Base 64\nAnother one to go out\n ')) 
    
    if chosen_option >= 1 and chosen_option <= 4:

        system("clear") 
        print(TITLE) 
        user_input = str(input('INPUT\n '))  
        print('\nOUTPUT\n ', end='')

        if chosen_option == 1:
            print(text_to_binary(user_input))
        elif chosen_option == 2: 
            print(binary_to_text(user_input))
        elif chosen_option == 3: 
            print(encode_base(user_input))
        elif chosen_option == 4: 
            print(decode_base(user_input))

if __name__ == '__main__':
    main()
