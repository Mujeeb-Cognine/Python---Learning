# How to Add Python Packages and use PyPi
# https://pypi.org/
# https://pokemondb.net/pokedex/game/x-y
# https://pypi.org/project/prettytable/

#  Practice Modifying Object Attributes and Calling Methods

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
