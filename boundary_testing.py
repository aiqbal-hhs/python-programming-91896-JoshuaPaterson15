import time
student_senior_discount = 10


def menu_call():
    menu_option = float(input("Please type 1 to view what consession you are entitled to or press 2 to purchase your tickets? "))

    if menu_option == 1:
        consession()
        
    elif menu_option == 2:
        print("You will be directed to the purchase page")
        time.sleep(4)
        tickets()

def consession():
    age = float(input("Please insert your age which will tell us which consession you are entitled to? "))
    if age >= 0 and age <= 4:
     print("You are not entitled to a consession making your ticket $20.")
    if age >= 5 and age <= 18:
     print("You are entitled to a ticket making your ticket $10.")
    if age >= 19 and age <= 59:
     print("You are not entitled to a consession making your ticket $20.")
    if age >= 60:
     print("You are entitled to a consession making your ticket $10.")
    
    
def tickets():
    print("""
The prices for tickets are as follows -

Children (aged between 0 and 4) = $20
Children (aged between 5 and 18) = $10 (A discount)
Adults (aged between 19 and 59) = $20
Seniors (anyone aged aboved 60) = $10 (A discount)
""")
    childe_tickets = float(input("Please insert how many Children (aged between 0 and 4) tickets you would like to buy? "))
    print("")
    child_tickets = float(input("Please insert how many Children (aged between 5 and 18) tickets you would like to buy? "))
    print("")
    adult_tickets = float(input("Please insert how many Adult (aged between 19 and 59) tickets you would like to buy? "))
    print("")
    senior_tickets = float(input("Please insert how many Senior (anyone aged aboved 60 tickets you would like to buy? "))
    print("")
    childe_tickets_total = 20* childe_tickets
    child_tickets_total = 10* child_tickets
    adult_tickets_total = 20* adult_tickets
    senior_tickets_total = 10* senior_tickets

    grand_total = childe_tickets_total + child_tickets_total + adult_tickets_total + senior_tickets_total

    print("""Here are your totals in each catagory -

    Children (aged between 0 and 4) - ${}
    Children (aged between 5 and 18) - ${}
    Adult (aged between 19 and 59) - ${}
    Senior (aged 60 and above) - ${}

    """.format(childe_tickets_total, child_tickets_total, adult_tickets_total, senior_tickets_total))
    print("Your total is ${} for all your tickets to Henderson High School's Production".format(grand_total))






name = input("Hello, what is your name? ")
print("Hello {}, welcome to Henderson High School's Production.".format(name))
menu_call()

