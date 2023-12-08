coding_skills = {
    "Python" : 1,
    "Ruby" : 2,
    "Bash" : 4,
    "Git" : 8,
    "HTML" : 16,
    "TDD" : 32,
    "CSS" :64,
    "JavaScript" : 128
}

missing_skills = {}
user_score = 0

print("Welcome to the ACME Corporation Junior Developer Skills Assessment")
for key,value in coding_skills.items(): 
    answer = input("Do you know " + key + "? Y/N: ")
    if answer == "Y" or answer == "y":
        user_score += value
    else:
        missing_skills[key] = value
print("Your score is: " + str(user_score))
print("If you had known these languages, your score would have increased by this much: ")
print(missing_skills)
print("Thank you! We'll be in touch!")
        



# user_input_skills = input("Please enter the languages you can use: ")

# if user_input_skills == "finished":
    


# ACME Corporation are hiring a new junior developer, as part of their hiring criteria they've created a "coding skill score" based on the specific competencies they require for this role; the more important the skill is for ACME corp, the more points it contributes to the "coding skill score" The skills are weighted as follows:
# - Python (1)
# - Ruby (2)
# - Bash (4)
# - Git (8)
# - HTML (16)
# - TDD (32)
# - CSS (64)
# - JavaScript (128)

# Write a program that allows a user to input their skills and then tells them 
# a) Their overall "coding skill score" 
# b) Skills they may want to learn, and how much each one would improve their score