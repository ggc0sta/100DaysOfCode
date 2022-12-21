"""
In OOP we're trying to model real life objects

Attributes: variables
Methods: Functions that the object can do

class [blueprint] / object [actual thing]
"""

"""
car (object) = CarBlueprint() (Class)
"""

# from turtle import Turtle, Screen
#
# timmy = Turtle()  # Turtle is a class
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
#
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

pokemon_name = ["Pikachu", "Squirtle", "Charmander"]
pokemon_type = ["Electric", "Water", "Fire"]

table.add_column("Pokemon Name", pokemon_name)
table.add_column("Type", pokemon_type)

table.align = "l"

print(table)