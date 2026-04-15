import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
info = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
""" name = {}
def pokemon(json):
    for i in pokemon[name]:
        name.append(pokemon)
        print(name) """
for index, pokemon in enumerate(info):
    print(index, ":", pokemon["name"])

# Add a language choice feature and print the pokemons name based on the user input

language_choice = input("enter your desired language: (1)English, (2)French, (3)Japanese, or (4)Chinese")
if language_choice == "1":
    for index, pokemon in enumerate(info):
            print(index, ":", pokemon["name"]['english'])
    
elif language_choice == "2":
    for index, pokemon in enumerate(info):
        print(index, ":", pokemon["name"]['french'])

elif language_choice == "3":
    for index, pokemon in enumerate(info):
        print(index, ":", pokemon["name"]['japanese'])

else:
        if language_choice == "4":
            for index, pokemon in enumerate(info):
             print(index, ":", pokemon["name"]['chinese'])
        
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
search_type = input("enter your pokemon's type. options (1)Grass or Poison, (2)Fire, (3)")
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

