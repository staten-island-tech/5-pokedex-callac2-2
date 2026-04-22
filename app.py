import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
info = json.load(pokedex)
print(info[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
""" name = {}
def pokemon(json):
    for i in pokemon[name]:
        name.append(pokemon)
        print(name) """
""" for pokemon in info:
    print(pokemon["name"]) """

# Add a language choice feature and print the pokemons name based on the user input

""" language_choice = input("enter your desired language: (1)English, (2)French, (3)Japanese, or (4)Chinese")
for pokemon in (info):
    if language_choice == "1":      
     print(pokemon["name"]['english'])
    
    elif language_choice == "2":
   
        print(pokemon["name"]['french'])

    elif language_choice == "3":
   
        print(pokemon["name"]['japanese'])

else:
        if language_choice == "4":
             print(pokemon["name"]['chinese']) """
        
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
for pokemon in (info):
   print(pokemon["type"])

search_type = input("enter your pokemon's type.")

type_list = {}

for pokemon in info:
        if pokemon['type'] == search_type:
        
           type_list.append(search_type)
else: 
        print("no pokemon are found, sorry :(")
        print(type_list)
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
match = (input("search word:"))
if match in info:
     print [match]["name"]
#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

