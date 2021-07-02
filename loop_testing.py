import time
ticket_catagories = ['CH', 'CH' ,'AD' ,'SN' ]
ticket_prices = [20,10,20,10]
print("There are")
print(ticket_catagories.count('CH'))
print("Child catagories.")
time.sleep(1)

payment_preference = [' ', 'cash']
payment_position = payment_preference.index('cash')
print("Cash is our number {} payment option! ".format(payment_position))
print("We accept")
payment_options = ['C' , 'a' , 's' , 'h']
print("".join(payment_options))

