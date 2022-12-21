# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
# with open("my_file.txt") as f:
#     contents = f.read()
#     print(contents)
#

"""
modes:
a - append: add new lines
r - read (default)
w - write
"""

with open("my_file.txt", mode="a") as f:
    f.write("\nNew text.")

# if you open a file that doesn't exist in write mode, Python will create that file for you.
with open("new_file.txt", mode="w") as f:
    f.write("New text 2")

# use files that are in a different directory.
with open("/Users/gabrielcosta/Desktop/different_file.txt", mode="w") as file:
    file.write("found you.")

# Use a RELATIVE PATH to open the file and write on it
# "/../" goes up 2 folders
with open("../../../../../Desktop/different_file.txt", mode="a") as file:
    file.write("\nfound you again.")

