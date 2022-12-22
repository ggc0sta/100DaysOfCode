try:
    file = open("a_file.txt")  # this file might not exist
    a_dictionary = {"key": "banana"}
    print(a_dictionary["asdasd"])  # non existing key

except FileNotFoundError:
    file = open("a_file.txt", mode="w")  # if file doesn't exist, create one
    file.write("Some text")

except KeyError as error_message:
    # if we use a non-existing key
    print(f"the key {error_message} does not exist.")

else:
    content = file.read()
    print(content)
finally:
    # This section runs no matter what happens
    file.close()
    print("File was closed")

# # Example 2 - raise your own errors ----------------------------
# If user enters a non-realistic value
height = float(input("Height in cm: "))
weight = int(input("Weight in kg: "))

if height > 300:
    raise ValueError("Human height should not be over 3 meters")
bmi = weight / height ** 2
print(bmi)


# # Example 3 -----------------------------------------------------
# IndexError

fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

    make_pie(4)




