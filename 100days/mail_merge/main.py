#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

LETTER = "input/letters/starting_letter.txt"
NAMES = "input/names/invited_names.txt"
MAILBOX = "output/readytosend/"

if __name__ == '__main__':

    with open(LETTER) as f:
        letter = f.read()

    with open(NAMES) as f:
        name_list = f.readlines()

    for name in name_list:
        new_letter = letter.replace("[name]", name.strip())

        with open(f"{MAILBOX}/letter_to_{name}.txt", 'w') as f:
            f.write(new_letter)
