"""
Creating a pokedex from the popular game "Pokemon" as a python dictionary.
Should be able to create entries, which accept several parameters such as
name of the pokemon, what type(s) the pokemon might be, health points, etc.
Program can also take a multiline string, extract the data and create the 
pokedex dictionary.
"""

def types_tuple(type_1, type_2):
    """
    Return tuple of type 1 and type 2, and if type 2 is empty then assign value as None
    """
    
    #Checking if type_2 is empty string or not
    if type_2 == "":
        type_2 = None
        return (str(type_1), str(type_2))

    else:
        return (str(type_1), str(type_2))


def attributes_dict(health_points, attack, defense, speed):
    """
    Return dictionary of attributes of pokemon
    """
    
    return {'HP': int(health_points), 'Attack': int(attack), 'Defense': int(defense), 'Speed': int(speed)}


def create_entry(number, name, type_1, type_2, health_points, attack, defense, speed, is_legendary):
    """
    Create and return dictionary entry for pokedex
    """

    #Defining variables for returned values of called functions
    tuple_types = types_tuple(type_1, type_2)
    dict_attributes = attributes_dict(health_points, attack, defense, speed)

    #Creating entry as a dictionary
    dict_stats = {'Number': int(number),
    'Name': str(name),
    'Types': tuple_types,
    'Battle Stats': dict_attributes,
    'Legendary': bool(is_legendary)}

    return dict_stats


POKEMON_DATA = """#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False
2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60,1,False
3,Venusaur,Grass,Poison,525,80,82,83,100,100,80,1,False
3,VenusaurMega Venusaur,Grass,Poison,625,80,100,123,122,120,80,1,False
4,Charmander,Fire,,309,39,52,43,60,50,65,1,False"""

NUM_IDX, NAME_IDX, TYPE_1_IDX, TYPE_2_IDX, HP_IDX, ATTACK_IDX, DEFENSE_IDX, SPEED_IDX, LEGENDERARY_IDX = 0, 1, 2, 3, 5, 6, 7, 10, 12


def create_pokedex(pokemon_data):
    """
    Extracts data and create pokedex dictionary
    """
    
    #Defining pokedex dictionary
    pokedex = {}

    #Splitting data by newline character
    pokemon_data = pokemon_data.split('\n')

    #Iterating through each line, ignoring the header
    for line in pokemon_data[1:]:
        #Preparing list for data extraction
        datum_list = line.split(',')

        #Calling creat_entry function to create dictionary of pokemon
        value = create_entry(datum_list[NUM_IDX], datum_list[NAME_IDX], datum_list[TYPE_1_IDX], datum_list[TYPE_2_IDX], datum_list[HP_IDX], datum_list[ATTACK_IDX], datum_list[DEFENSE_IDX], datum_list[SPEED_IDX], datum_list[LEGENDERARY_IDX])
        key = value['Name']

        #If this entry doesn't already exist in our dictionary, add it
        if key not in pokedex:
            pokedex[key] = value

    return pokedex


def main():
    pokedex = create_pokedex(POKEMON_DATA)
    pokemon_key = "Ivysaur"

    if pokemon_key not in pokedex:
        print (f"ERROR: Pokemon {pokemon_key} does not exist!")

    else:
        print (f"PRINTING {pokemon_key}'S INFORMATION...")

        my_favourite_pokemon = pokedex[pokemon_key]

        for key in my_favourite_pokemon.keys():
            print (f"{key}: {my_favourite_pokemon[key]}")


main()