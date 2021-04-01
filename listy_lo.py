# In the second file, called listy_lo.py and do the following within the file:
#----------------------------------------------------------------------------------
# Create a list named food with two elements 'rice' and 'beans'.
# Append the string 'broccoli' to food using .append().
# Add the strings 'bread' and 'pizza' to food using .extend().
# Print the first two items in the food list using print() and slicing notation.
# Print the last item in food using print() and index notation.
# Create a list called breakfast from the string "eggs,fruit,orange juice" using the split() method.
# Verify that breakfast has 3 elements using the len built-in.
# prompts the user for a floating-point value until they enter stop. Store their entries in a list, and then find the average, min, and max of their entries and print them those values.

if __name__ == "__main__":
    
    food = ['rice', 'beans']
    print(food)

    food.append('broccoli')
    print(food)

    food.extend(['bread', 'pizza'])
    print(food)

    print(food[4])


    breakfast = ('eggs,fruit,orange juice')
    print(breakfast)
    breakfast = breakfast.split(',')
    print(breakfast) 

    print(len(breakfast))

    print('Please enter desired amount of numbers to calculate average, min and max', 'and', 'Enter: done when finished!')
    numlist = [] 
    while True:
        inp = input('Enter a number: ')
        if inp == 'done':
            break
        value = float(inp)
        numlist.append(value)

    print(numlist)
    
    average = sum(numlist) / len(numlist)
    print(f'Average: {average}')

    max = max(numlist)
    print(f'Max: {max}')
    
    min = min(numlist)
    print(f'Min: {min}') 