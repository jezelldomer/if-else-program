
your_age = int(input("Enter your age: "))
if your_age >= 0 and your_age <= 12: 
    print ("Kid")
elif your_age >= 13 and your_age <= 17:
    print ("Teen")
elif your_age == 18:
    print ("Debut")
elif your_age >= 19:
    print ("Adult")
else:
    print("Invalid input for your age. Please provide and enter a valid input. ")

print ("--Done--")