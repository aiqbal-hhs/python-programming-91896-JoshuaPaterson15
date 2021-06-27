import time #Importing time to use the pause/sleep function.












def menu_call(): #Definition created as the menu.
    menu_option = float(input("Please type 1 to view what consession you are entitled to or press 2 to purchase your tickets? ")) #This numeric input is so users have the option to call the nessasary code which is relevant to them.

    if menu_option == 1: #If a users types in 1 as their answer, the menu would call the concession definition.
        consession()
        
    if menu_option == 2: #If a users types in 2 as their answer, the menu would call the tickets definition.
        print("You will be directed to the purchase page")
        time.sleep(4) #Using the import time function, I could pause the programe for 4 seconds.
        tickets() #This calls the tickets definition.

    else:
        print("Your input was wrong, please try again")

def consession(): #Definition created for verifing someones eligbility for a consession ticket.
    age = float(input("Please insert your age which will tell us which consession you are entitled to? ")) #This numeric variable which has been named accordingly, is to identify how old the user is. 
    if age >= 0 and age <= 4: #If the user inputs an answer between 0 and 4, this if satement would be used.
     print("You are not entitled to a consession making your ticket $20.")
     menu_call() #The user will then be redirected to the menu.
    if age >= 5 and age <= 18: #If the user inputs an answer between 5 and 18, this if satement would be used.
     print("You are entitled to a ticket making your ticket $10.")
     menu_call() #The user will then be redirected to the menu.
    if age >= 19 and age <= 59: #If the user inputs an answer between 19 and 59, this if satement would be used.
     print("You are not entitled to a consession making your ticket $20.")
     menu_call() #The user will then be redirected to the menu.
    if age >= 60: #If the user inputs an answer above 60, this if satement would be used.
     print("You are entitled to a consession making your ticket $10.")
     menu_call() #The user will then be redirected to the menu.
    
    
def tickets(): #Definition created for purchasing tickets.
    print("""
The prices for tickets are as follows -

Children (aged between 0 and 4) = $20
Children (aged between 5 and 18) = $10 (A discount)
Adults (aged between 19 and 59) = $20
Seniors (anyone aged aboved 60) = $10 (A discount)
""") #This is the total price for the overall ticket price in line with the usability convention.
    childe_tickets = float(input("Please insert how many Children (aged between 0 and 4) tickets you would like to buy? ")) #This is asking the amount of tickets the user wishes to purchase for this catagory.
    print("") #This is a gap for visual hieracy reasons.
    child_tickets = float(input("Please insert how many Children (aged between 5 and 18) tickets you would like to buy? ")) #This is asking the amount of tickets the user wishes to purchase for this catagory.
    print("") #This is a gap for visual hieracy reasons.
    adult_tickets = float(input("Please insert how many Adult (aged between 19 and 59) tickets you would like to buy? ")) #This is asking the amount of tickets the user wishes to purchase for this catagory.
    print("") #This is a gap for visual hieracy reasons.
    senior_tickets = float(input("Please insert how many Senior (anyone aged aboved 60 tickets you would like to buy? ")) #This is asking the amount of tickets the user wishes to purchase for this catagory.
    print("") #This is a gap for visual hieracy reasons.
    childe_tickets_total = 20* childe_tickets #This calculates the total amount for each catagory based on the amount of tickets the user wishes to purchase.
    child_tickets_total = 10* child_tickets #This calculates the total amount for each catagory based on the amount of tickets the user wishes to purchase.
    adult_tickets_total = 20* adult_tickets #This calculates the total amount for each catagory based on the amount of tickets the user wishes to purchase.
    senior_tickets_total = 10* senior_tickets #This calculates the total amount for each catagory based on the amount of tickets the user wishes to purchase.

    grand_total = childe_tickets_total + child_tickets_total + adult_tickets_total + senior_tickets_total #This would be the total price of the users requests after calculating the total for each catagory.

    print("""Here are your totals in each catagory -

    Children (aged between 0 and 4) - ${}
    Children (aged between 5 and 18) - ${}
    Adult (aged between 19 and 59) - ${}
    Senior (aged 60 and above) - ${}

    """.format(childe_tickets_total, child_tickets_total, adult_tickets_total, senior_tickets_total)) #This is the total prices based on the users request and is printed per catagory to outline the users request.
    print("Your total is ${} for all your tickets to Henderson High School's Production".format(grand_total)) #This is the overall total price when all the totals are calculated together.
    return()


#MAIN SCRIPT BELOW -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

name = input("Hello, what is your name? ") #This is an imput so the script can be personalized according to their name.
print("Hello {}, welcome to Henderson High School's Production.".format(name)) #An input to greet them on to the python system.
menu_call() #Calling the menu definition as its the users first time.
purchase_request("If you would like to purchase these tickets please type 'purchase' or 'no'")

