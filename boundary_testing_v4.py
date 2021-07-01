import time #Importing time to use the pause/sleep function.


def age_check():

    age_request = float(input("Please insert your age to verify if you are eligable to purchase tickets on this script? "))
    b = age_request

    if b > 15:
      print("Your eligable for purchasing ticket using this script.")
      menu_call()
    else:
      print("We are sorry, your not eligable, good bye! ")
      quit()

def menu_call(): #Definition created as the menu.
    menu_option = float(input("Please type 1 to view what consession you are entitled to or press 2 to purchase your tickets? ")) #This numeric input is so users have the option to call the nessasary code which is relevant to them.

    if menu_option == 1: #If a users types in 1 as their answer, the menu would call the concession definition.
        consession()
        
    if menu_option == 2: #If a users types in 2 as their answer, the menu would call the tickets definition.
        print("You will be directed to the purchase page")
        time.sleep(4) #Using the import time function, I could pause the programe for 4 seconds.
        tickets() #This calls the tickets definition.

    if menu_option == 3: #If a users types in 3 as their answer, the menu would call the ticket_win definition.
        print("You will be directed to the oppitunity to win a free ticket.")
        time.sleep(1) #Using the import time function, I could pause the programe for 4 seconds.
        ticket_win() #This calls the tickets definition.
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
    ticket_cost = [10, 20]
    print("The minimum cost of a ticket is ${} and the highest cost of a ticket is ${}".format((min(ticket_cost)),(max(ticket_cost))))
    ticket_prices = ["Children (aged between 0 and 4) = $20",  "Children (aged between 5 and 18) = $10 (A discount)", "Adults (aged between 19 and 59) = $20", "Seniors (anyone aged aboved 60) = $10 (A discount)"]
    print("There are", len(ticket_prices), "catagories avaliable for purchase.")
    childe_tickets = float(input("Please insert how many Children (aged between 0 and 4) tickets you would like to buy? ")) #This is asking the amount of tickets the user wishes to purchase for this catagory.
    print("") #This is a gap for visual hieracy reasons.
    child_tickets = float(input("Please insert how many Children (aged between 5 and 18) tickets you would like to buy? ")) #This is asking the amount of tickets the user wishes to purchase for this catagory.
    print("") #This is a gap for visual hieracy reasons.
    adult_tickets = float(input("Please insert how many Adult (aged between 19 and 59) tickets you would like to buy? ")) #This is asking the amount of tickets the user wishes to purchase for this catagory.
    print("") #This is a gap for visual hieracy reasons.
    senior_tickets = float(input("Please insert how many Senior (anyone aged aboved 60 tickets you would like to buy? ")) #This is asking the amount of tickets the user wishes to purchase for this catagory.
    print("") #This is a gap for visual hieracy reasons.
    childe_tickets_total =  ticket_cost[1] *childe_tickets #This calculates the total amount for each catagory based on the amount of tickets the user wishes to purchase.
    child_tickets_total =  ticket_cost[0] * child_tickets #This calculates the total amount for each catagory based on the amount of tickets the user wishes to purchase.
    adult_tickets_total =  ticket_cost[1] * adult_tickets #This calculates the total amount for each catagory based on the amount of tickets the user wishes to purchase.
    senior_tickets_total =  ticket_cost[0] * senior_tickets #This calculates the total amount for each catagory based on the amount of tickets the user wishes to purchase.

    
    grand_total = childe_tickets_total + child_tickets_total + adult_tickets_total + senior_tickets_total #This would be the total price of the users requests after calculating the total for each catagory.

    print("""Here are your totals in each catagory -

    Children (aged between 0 and 4) - ${}
    Children (aged between 5 and 18) - ${}
    Adult (aged between 19 and 59) - ${}
    Senior (aged 60 and above) - ${}

    """.format(childe_tickets_total, child_tickets_total, adult_tickets_total, senior_tickets_total)) #This is the total prices based on the users request and is printed per catagory to outline the users request.
    print("Your total is ${} for all your tickets to Henderson High School's Production".format(grand_total)) #This is the overall total price when all the totals are calculated together.
    payment_method()

def payment_method():
   payment_types = ["cash", "bank transfer", "debit card"]
   payment_input = str(input("To verifiy your payment option, please type the option now? ")).strip().lower()
   if payment_input in payment_types:
        print("We accept your payment method of {}.".format(payment_input.capitalize()))
        payment()
   else:
        print("We don't accept your payment method.")
        payment_methods = "Cash#Bank Transfer# Debit Card"
        pay_methods = payment_methods.split("#", 2)
        print("We accept {}".format(pay_methods))
        payment()

def payment():
    payment_option = str(input("How you would like to pay? ")).lower()
    if payment_option ==  "cash":
       print("Please pay when you arrive at the production.")
       print("When you arrive, please indicate your order number.")
       option1 = str(input("Is there anything else you would like todo today? ")).strip().lower()
    if option1 == "yes":
            menu_call()
    else:
            print("Thank you, Good Bye!")
            quit() 
       
    if payment_option == "bank transfer":
        print("Option 1")
        
    if payment_option == "debit card":
        print("Option 2")
        
    else:
        print("Sorry")
        menu_call()
        
def ticket_win():
    guess = 3
    while guess >= 1:
            num_guess = float(input("How many students approximitly are at Henderson High School? "))
            if num_guess == 1000:
                print("You correct, add code 'I won' to the checkout.")
                print("Thanks for playing.")
                menu_call()
            else:
                print("Sorry wrong, please try again")
                guess -= 1
                print("You have {} tries remaining".format(guess))
                print({} <  9)
                continue
    else:
            print("Sorry, you failed")
            menu_call()


#MAIN SCRIPT BELOW -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

payment_method()
name = input("Hello, what is your name? ") #This is an imput so the script can be personalized according to their name.
print("Hello {}, welcome to Henderson High School's Production.".format(name)) #An input to greet them on to the python system.
age_check()

