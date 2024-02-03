

numbers = []  # Empty list to store the numbers
smallest_num = None
largest_num = None

# loop creates list of numbers from user input
while True:
    x = input("Enter a number or type done: ")
    if x == 'done':
        break
    try:
        the_num = float(x)
    except:
        print('Invalid input')
        continue
    numbers.append(the_num) # Add the number to the list

    # loop finding largest number in list
for largest_so_far in numbers:
    if largest_num is None:
        largest_num = largest_so_far
    elif largest_so_far > largest_num:
        largest_num = largest_so_far
        
# loop finding smallest number in list
for smallest_so_far in numbers:
    if smallest_num is None:
        smallest_num = smallest_so_far
    elif smallest_so_far < smallest_num:
        smallest_num = smallest_so_far

maximum = int(largest_num)
minimum = int(smallest_num)
    
print("Maximum is",maximum)
print('Minimum is',minimum)


