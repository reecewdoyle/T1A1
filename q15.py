raining = True if input("Is it raining? (type yes or no) ").lower() == "yes" else False
temperature = int(input("What is the temperature? "))


if raining == True:
    if temperature <= 15:
        print("It's wet and cold")
    else:
        print("It's warm and raining")

if raining == False:
    if temperature <= 15:
        print("It's not raining but it's cold")
    else:    
        print("It's warm but not raining")







# You have access to two variables: raining (boolean) and temperature (integer). 

# If it’s raining and the temperature is less than 15 degrees, print to the screen “It’s wet and cold”.

# If it is NOT raining and less than 15 degrees, print to the screen “It’s not raining but cold”.

# If it’s NOT raining and greater than or equal to 15 dgrees, print to the screen “It’s warm but not raining”, 

# and otherwise (raining and more than 15 degrees) tell them “It’s warm and raining”.
