numbers = [5, 22, 29, 39, 19, 51, 78, 96, 84]
i = 0

# while means to loop. 
# loop while zero is less than the length of the numbers in the array - 1. 
while (i < len(numbers) - 1) and (numbers[i] < numbers[i+1]):
    # print(numbers[i])
    i += 1

x = numbers[i] 
numbers[i] = numbers[i+1]
numbers[i+1] = x
print(numbers)




# while - With the while loop we can execute a set of statements as long as a condition is true.

# len function - The len() function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.