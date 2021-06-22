import time
student_senior_discount = 10

name = input("Hello, what is your name? ")
print("Hello {}, welcome to Henderson High School's Production.".format(name))
print(""" The prices for tickets are as follows -
Children (aged between 0 and 4) = $20
Children (aged between 5 and 18) = $10 (A discount)
Adults (aged between 19 and 59) = $20
Seniors (anyone aged aboved 60) = $10 (A discount)
""")
childe_tickets = float(input("Please insert how many Children (aged between 0 and 4) tickets you would like to buy? "))
child_tickets = float(input("Please insert how many Children (aged between 5 and 18) tickets you would like to buy? "))
adult_tickets = float(input("Please insert how many Adult (aged between 19 and 59) tickets you would like to buy? "))
senior_tickets = float(input("Please insert how many Senior (anyone aged aboved 60 tickets you would like to buy? "))

childe_tickets_total = 20* childe_tickets
child_tickets_total = 10* child_tickets
adult_tickets_total = 20* adult_tickets
senior_tickets_total = 10* senior_tickets

grand_total = childe_tickets_total + child_tickets_total + adult_tickets_total + senior_tickets_total

print(""" Here are your totals in each catagory -
Children (aged between 0 and 4) - ${}
Children (aged between 5 and 18) - ${}
Adult (aged between 19 and 59) - ${}
Senior (aged 60 and above) - ${}
""".format(childe_tickets_total, child_tickets_total, adult_tickets_total, senior_tickets_total))
print("Your total is ${} for all your tickets to Henderson High School's Production".format(grand_total))


