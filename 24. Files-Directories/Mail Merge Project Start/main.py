# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# readlines method returns a list containing each line in the file as a list.

with open("./Input/Names/invited_names.txt") as file:
    invited_names = file.readlines()
for name in range(len(invited_names)):
    invited_names[name] = invited_names[name].replace("\n", "")

print(invited_names)

# Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    # Save the letters in the folder "ReadyToSend".
    for name in invited_names:
        ready = letter.replace("[name]", name)

        with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as output:
            output.write(ready)


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
