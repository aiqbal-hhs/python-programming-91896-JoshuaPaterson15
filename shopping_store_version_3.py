import time

pocket_money = []
item_name = []
item_price = []
item_1 = 10
jackpot = 123

pocket_money =+ 10000
discount_15_off =+ 10

name = input("What is your name? ").strip(" ,.;:1234567890")
menu = input("What action would you like todo, type 1 for shopping, type 2 for a balance check or type 3 for exit? ").strip(" ,.;:abcdefghijklmnopqrstuvwxyz")
if menu == '1':
        item_wanting = input("What would you like to purchase {}? ".format(name)).strip(" ,.;:1234567890")

        if item_wanting == 'item 1':
            item_name.append(item_wanting)
            item_cost = 5* item_1 +3
            confimation = input("Are you sure you would like to purchase {} for ${}? (To cancel type no or type yes to confirm) ".format(item_wanting, item_cost)).lower()
            if confimation == 'no':
                print('Ok, your item has been cancelled.')
                print(menu)
            if confimation == 'yes':
                discount_code = input("Is there any discounts you would like to add to your order? ").lower().strip(" ,.;:1234567890")

                if discount_code == 'no':
                    pocket_money -= item_cost
                    print("Your purchase has been made.")

                elif discount_code == 'yes':
                    item_cost -= discount_15_off
                    print("Your total amount is ${}.".format(item_cost))
                    pocket_money -= item_cost
                    print("Your purchase has been made.")

                else:
                        print("Sorry, this is an incorrect input message.")
            
        else:
            item_name.append(item_wanting)
            item_cost = float(input("How much is your item {}? ".format(name)))
            item_price.append(item_cost)
            confimation = input("Are you sure you would like to purchase {} for ${}? (To cancel type no or type yes to confirm) ".format(item_wanting, item_cost)).strip(" ,.;:1234567890").lower()
            if confimation == 'no':
                print('Ok, your item has been cancelled.')
                print(menu)
            if confimation == 'yes':
                discount_code = input("Is there any discounts you would like to add to your order? ").strip(" ,.;:1234567890").lower()

                if discount_code == 'no':
                    pocket_money -= item_cost
                    print("Your purchase has been made.")

                if discount_code == 'yes':
                    item_cost -= discount_15_off
                    print("Your total amount is ${}.".format(item_cost))
                    pocket_money -= item_cost
                    print("Your purchase has been made.")

if menu == '2':
        customer_budget = int(input("Please input your budget for today's shopping? ")).strip(" ,.;:abcdefghijklmnopqrstuvwxyz")
        if customer_budget <10:
                print("Your budget is too low.")

        elif customer_budget > 50 and customer_budget <= 100:
                print("You have a sufficant balance avaliable for any purchase on this store.")

        elif customer_budget == jackpot:
                print("You have won the jackpot, use the discount code yes next time you purchase anything from our store!")

if menu == '3':
    print("Thanks for visiting us, have an awesome day!")
    time.sleep(2)

