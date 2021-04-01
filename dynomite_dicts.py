# In the third file, called dynomite_dicts.py do the following:
#--------------------------------------------------------------
# Create an empty dictionary called pokedex.
# Add the following key, value pairs to the dictionary:
# 'Venosaur': ['Grass', 'Poisen']
# 'Charizard': ['Fire', 'Flying']
# 'Blastoise': ['Water']
#_______________________________________
# Remove 'Blastoise' from the dictionary.

if __name__ == "__main__":
    pokedex = {

    }
    
    pokedex['Venosaur'] = ['Grass','Poisen']
    pokedex['Charizard'] = ['Fire', 'Flying']
    pokedex['Blastoise'] = ['Water']
    print(pokedex)
    
    del pokedex['Blastoise']
    print(pokedex)