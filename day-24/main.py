#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/Users/theyi/Desktop/day-24/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for each_name in names:
        with open("/Users/theyi/Desktop/day-24/Input/Letters/starting_letter.txt", mode="w") as letter_file:
            letter_file.write(names.replace("[name]", each_name))