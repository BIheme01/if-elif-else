"""
Start

Use the if-elif-else statement
1. Ask for the user's age and store it as integer
2. If user is 40 or over, print "You're over the hill."
3. If user says they are over 100, print "Sorry, you're dead.".
4. If the user is 65 or older, print "Enjoy your retirement!"
5. If the user is under 13, print "You qualify for the kiddie discount."
6. If user is 21, print "Congrats on your 21st!"
7. For any other age, print "Age is but a number."

Stop
"""
age = int(input("What is your age?"))

if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.") 
elif age == 21:
    print("Congrats on your 21st!")     
elif age < 13:
    print("You qualify for the kiddie discount.")          
else:
    print("Age is but a number.")
    
