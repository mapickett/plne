
def game_over():
    print("\nPoor Choice. Game Over")
    print('''
           _  _
     ___ (~ )( ~)
    /   \\_\\ \\/ /
   |   D_ ]\\ \\/
   |   D _]/\\ \\ 
    \\___/ / /\\ \\ 
         (_ )( _)\n''')

def you_win():
    print("\nCongratulations, You found the Treasure!!!")
    print('''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'\n''')
    
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
choice1 = input("Enter your choice(right or left): ").lower()
if choice1 == "left":
    print('''
You've come to a lake. There is an island in the middle of the lake
Type "wait" to wait for a boat. Type "swim" to swim across''')
    choice2 = input("Enter your choice(wait or swim): ").lower()
    if choice2 == "wait":
        print('''
You arrive at the island unharmed. There is a house with 3 doors.
One red, one yellow and one blue. Which color door do you choose?''')
        choice3 = input("Enter your choice(red, yellow or blue): ").lower()
        if choice3 == "yellow":
            you_win()
        elif choice3 == "red":
            print("You were burned by Fire.")
            game_over()
        elif choice3 == "blue":
            print("You were eaten by Beasts.")
            game_over()
        else:
            game_over()
    else: 
        print("You were attacked by Trout.")
        game_over()
else:
    print("You fell into a Hole.")
    game_over()
