import sys 
yes_no = input("Do you want to use the bus ? (y/n) :-  ")

rupees = 0

yes_no = yes_no.lower()

if yes_no == "y":
    print("Okay")
elif yes_no == "n":
    sys.exit(0)
else:
    print("Invalid input")

print("Valid :-\nBanglore to hydrabad          (b-g)\nChennai To kochi          (c-k)\nChennai to banglore          (c-b)\nPune to mumbai          (p-m)\nMumbai to delhi          (m-d)")
location = input("Enter the place you want to travell from and to (enter an option such as b-g )          ")

if location == "b-g":
    print("That is a valid location")
    rupees = 500
elif location == "c-k":
    print("That is a valid location")
    rupees = 700
elif location == "c-b":
    print("That is a valid location")
    rupees = 450
elif location == "p-m":
    print("That is a valid location")
    rupees = 600
elif location == "m-d":
    print("That is a valid location")
    rupees = 900
else:
    print("That is not a valid input")
    sys.exit(0)
age = int(input("Enter your age:-   "))

if age >= 11:
    print("The amount would be",rupees,"Per passenger")
if age <= 10:
    print("You can enjoy our servises they are free")
    rupees = 0 

num_ppl = int(input("Please enter the number of people :-  "))
 
total_rupees = num_ppl*rupees

if total_rupees >= 5 :
    total_rupees1 = total_rupees/100 * 30 
    total_rupees = total_rupees - total_rupees1
else:
    print()
print(total_rupees)