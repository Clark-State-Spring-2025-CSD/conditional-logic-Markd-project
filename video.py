#Updated 1 Feb 2025
#Watch the video here: https://www.youtube.com/watch?v=YKxvDL3JxEA or follow the instructor led demo
#Implement all the code shown in the video.
#Modify the code so the checks from 12 and under for the $8 price tag
#and 62 and older for the $12 price tag.

print("welcome to the Menu Ordering System")

customerAge = int(input("What is the age of the customer? "))

price = 9

if customerAge < 12:
    price = 8
elif customerAge >= 62:
    price = 12
#else:
#    price = 12

print(f"The cost for this customer is ${price}")

drinkYesNo = input("Add a drink? Y/N")

if drinkYesNo == "Y":
    smallLarge = input("small or Large? S/L")
    if smallLarge == "L":
          price += 1
    else:
          price += 2

print(f"Total is: ${price}")