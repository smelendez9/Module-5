# In the first file, called loopy_loops.py do the following:
#--------------------------------------------------------------------------------------------------------
# Create a tuple named pokemon that holds the strings 'picachu', 'charmander', and 'bulbasaur'.
# Using index notation, print() the string that located at index 1 in pokemon
# Unpack the values of pokemon into the following three new variables with names starter1, starter2, starter3.
# Create a tuple using the tuple() built-in, that contains the letters of your name.
# Check whether the character i is in your tuple representation of your name.
# Write a for loop that prints out the integers 2 through 10, each on a new line, by using the range() function.
# Use a while loop that prints out the integers 2 through 10.
# Write a for loop that iterates over the string 'This is a simple string' and prints each character.
# Using a nested for loop, iterate over the following set ('this', 'is', 'a', 'simple', 'set') and print each word, three times.
#_____________________________________________________________________________________
if __name__ == "__main__":

    poke_tuple = ('picachu', 'charmander', 'bulbasaur')
    print(poke_tuple[1])

    (starter1, starter2, starter3) = poke_tuple
    # print(starter1)
    # print(starter2)
    # print(starter3)

    myname_tup= ('Sergio')
    print(tuple(myname_tup))
    
    print('i' in myname_tup)

    for i in range(2,11):
        print(i)

    print('-------------------')
    
    n = 11
    while n > 2:
        n -= 1
        print(n)

    print('-------------------')
    
    for simpstr in 'This is a simple string':
        print(simpstr)

    print('-------------------')

    simpstr = 'This', 'is', 'a', 'simple', 'string', 'set'
    for line in range(3):
        simpstr_result = simpstr * 1
        print(simpstr_result)