import time

pocket_money = []
item_name = []
item_price = []
item_1 = 10

pocket_money =+ 10000
discount_15_off =+ 10

name = input("What is your name? ")
menu = input("What action would you like todo, type 1 for shopping or type 2 for exit? ")
if menu == '1':
        item_wanting = input("What would you like to purchase {}? ".format(name))

        if item_wanting == 'item 1':
            item_name.append(item_wanting)
            item_cost = 5* item_1 +3
            confimation = input("Are you sure you would like to purchase {} for ${}? (To cancel type no or type yes to confirm) ".format(item_wanting, item_cost))
            if confimation == 'no':
                print('Ok, your item has been cancelled.')
                print(menu)
            if confimation == 'yes':
                discount_code = input("Is there any discounts you would like to add to your order? ")

                if discount_code == 'no':
                    pocket_money -= item_cost
                    print("Your purchase has been made.")

                if discount_code == 'yes':
                    item_cost -= discount_15_off
                    print("Your total amount is ${}.".format(item_cost))
                    pocket_money -= item_cost
                    print("Your purchase has been made.")
            
          else:
            item_name.append(item_wanting)
            item_cost = float(input("How much is your item {}? ").format(name))
            item_price.append(item_cost)
            confimation = input("Are you sure you would like to purchase {} for ${}? (To cancel type no or type yes to confirm) ".format(item_wanting, item_cost))
            if confimation == 'no':
                print('Ok, your item has been cancelled.')
                print(menu)
            if confimation == 'yes':
                discount_code = input("Is there any discounts you would like to add to your order? ")

                if discount_code == 'no':
                    pocket_money -= item_cost
                    print("Your purchase has been made.")

                if discount_code == 'yes':
                    item_cost -= discount_15_off
                    print("Your total amount is ${}.".format(item_cost))
                    pocket_money -= item_cost
                    print("Your purchase has been made.")

if menu == '2':
    print("Thanks for visiting us, have an awesome day!")
    time.sleep(2)

