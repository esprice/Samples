print("Welcome to For Cup Coffee!")
name = input("What is your name? ")

if name == "Ben" or name == "Patricia" or name == "Loki" or name == "Mark" or name == "Richard":
    evil_status = input('Are you evil? ')
    good_deeds = int(input('How many good deeds have you done today?\n '))
    if evil_status == "Yes" and good_deeds < 4:
        print("You're not welcome here, evil, " + name + " ! Get out!")
        exit()
elif name == "Michael" or name == "Elizabeth" or name == "Beth":
    duck_love = input('Do you love ducks? ')
    if duck_love == "Yes":
        print("Quack! Quack! \n Ducks love you too!")
elif name == "Steve" or name == "James" or name == "Bill" or name == "William" or name == "Tim" or name == "Jim" or name == "Diana" or name == "Jacky" or name == "Susan" or name == "Mike":
    coffee_love = input('Do you enjoy coding? ')
    if coffee_love == 'Yes':
        print('Just to let you know, ' + name + ', we make all our Java fresh from script.')
    
    else:
        print("Great to see you today, " + name + "!")
else:
    print("Hello " + name + ", thanks a latte for coming in today.")

drink_menu = ("coffee", 'iced coffee', 'java', "cappuccino", "latte", "espresso", "frappuccino", "tea")

print('What would you like to order today, ' + name + '? Here is what we are serving:\n ')
print(drink_menu)
order = input()
if order == "frappuccino":
    whipped_cream = input('Do you want whipped cream with that? ').upper()  
    if whipped_cream == "YES":
        price = 14
    else:
        price = 13
elif order == "coffee" or order == "java" or order == 'iced coffee':
    cream = input('Do you want cream and sugar with that? ').upper()
    if cream == "YES":
        price = 3
    else:
        price = 2
elif order == 'espresso':
    price = 5
elif order == 'latte':
    whipped_cream1 = input('Do you want whipped cream with that? ').upper()  
    if whipped_cream1 == "YES":
        price = 7
    else:
        price = 6
elif order == 'cappuccino':
    whipped_cream1 = input('Do you want whipped cream with that? ').upper()
    if whipped_cream1 == "YES":
        price = 7
    else:
        price = 6
elif order == 'tea':
    lemon = input('Do you want lemon and sugar with that? ').upper()
    if lemon == "YES":
        price = 3
    else:
        price = 2
else:
    print("We don't have that here.")
    price = 0

quantity = int(input("How many " + order + "s would you like? "))

total = price * quantity 
print("Sounds good, " + name + ". We'll have your " + str(quantity) + " " + order + "s ready for you in a moment.")
print("Thank you. Your total is: $" + str(total))
if name == "Michael" or name == "Elizabeth" or name == "Beth":
    print('Make sure to save some to take to the park')
elif name == "Steve" or name == "James" or name == "Bill" or name == "William" or name == "Tim" or name == "Jim" or name == "Diana" or name == "Jacky" or name == "Susan" or name == "Mike":
    print("And be sure to grab a current edition of Spiders and Snakes located on the condiments counter. \n This weeks top article is:\n Eve's Guide to Working with Pythons\n A cautionary tale. \n There's also another good article about working for Apple by Adam Figleaf. \n Apparently, they're super strict with meal times.")
elif order == latte:
    print('Watch yourself, now.\n When coffee spills, it causes a latte problems.')
elif order == 'coffee' or order == 'iced coffee' or order == 'java':
    print('Coffee is a brew-tiful thing.')

