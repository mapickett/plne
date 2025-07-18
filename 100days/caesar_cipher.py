

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_action():
    while True:
        act = str(input("Enter 'encode' to encrypt or 'decode' to decrypt:")).lower().strip()
        if act in ['encode', 'decode']:
            return act
        else:
            print("Invalid choice.")

def get_message():
    while True:
        msg = str(input("Enter your message:")).lower().strip()
        if msg.isalpha():
            return msg
        else:
            print("Invalid choice. Message must only contain letters.")

def get_shift():
    while True:
        shift = input("Enter the shift number:").strip()
        try:
            int(shift)
            return int(shift)
        except ValueError:
            print("Invalid choice.")

def run_cipher(message, shift, action):
    result = ""
    if action == "decode":
        shift *= -1
    for c in message:
        if c in alphabet:
            result += alphabet[(alphabet.index(c) + shift) % 25]
        else:
            result += c
    return result

if __name__ == "__main__":

    go_again = True
    print(logo)
    while go_again:
        action = get_action()
        message = str(input("Enter your message: "))
        shift = get_shift()
        result = run_cipher(message, shift, action)
        print(f'Here is the {action}d result: {result}')
        while True:
            choice = str(input("Do you want to go again? Enter 'yes' or 'no': ")).lower()
            if choice in ['yes', 'no']:
                if choice == 'no':
                    go_again = False
                break
            else:
                print("Invalid choice.")
