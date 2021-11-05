# Imports-----------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk # Importing tkrinter GUI platform and reffering the name as tk for short.
from tkinter import ttk# Importing ttk from tkrinter.
from tkinter import Entry, Label, Menu, StringVar # Importing Entry, Label from tkrinter.
from tkinter.constants import ALL, END # Importing constants from trkrinter.
global time # Global time variable to allow the time variable to be accross all functions.
import time # Importing the time functionality for the use of time and sleep.
from time import strftime # Importing strftime from the time import.
import datetime # Importing the time function to use the date and time functionality.
import os # Importing OS for window functionality e.g.Shut Down, restart.
import sys # Importing SYS for resrating python scripts.

# Global-----------------------------------------------------------------------------------------------------------------------------------------------------------
global window # Making the window variable global to apply to all functions in this script.
global menu # Making the menu vairable variable global to apply to all functions in this script.
global button_background # Making the button background vairable global to apply to all functions in this script.
global button_text # Making the button text vairable variable global to apply to all functions in this script.
global credential # Making the credential dictonary variable global to apply to all functions in this script.
global count # Making the count vairable variable global to apply to all functions in this script.
global pizza_options # Making the pizza options dictonary variable global to apply to all functions in this script.
global payment_options # Making the payment options dictonary variable global to apply to all functions in this script.

# Dictonaries---------------------------------------------------------------------------------------------------------------------------------------------------------------
credential = {'HHS':{'password':'Henderson', }, 'ADMIN':{'password':'., @admin', }, 'Tech':{'password':'123Tech', }} # Dictonary for all the usernames and passwords to login.
pizza_options = {"Pizza 1":'Australia', "Pizza 2":'France', "Pizza 3":'Korea', "Pizza 4":'India', "Pizza 5":'Fiji', "Pizza 6":'Germany', "Pizza 7":'Wellington', "Pizza 8":'Southern Italy', "Pizza 9":'New York', "Pizza 10":'London', "Pizza 11":'Rome', "Pizza 12":'Chicago', } # Dictonary for all the pizza options in the new order function. 
payment_options = {"Cash":'Cash Payment (UNPAID)', "Card":'Card Payment (UNPAID)', "Other":'Other'} # Dictonary for all payment options which are avalible for the business.

# Lists------------------------------------------------------------------------------------------------------------------------------------------------------------------
topping_options = ["Pepperoni", "Cheese", "BBQ Sauce", "Capsicum"]

# Fonts------------------------------------------------------------------------------------------------------------------------------------------------------------
global font_global # Making the font_global font option variable global to apply to all functions in this script.
global font_global_15 # Making the font_global font option in size 15 variable global to apply to all functions in this script.
global font_global_20 # Making the menu vairable global to apply to all functions in this script.
font_global = ("Comic Sans MS", 10, "bold") # Having font_global equal to differnt font style specifications.
font_global_15 = ("Comic Sans MS", 15, "bold") # Having font_global equal to differnt font style specifications with a size of 15.
font_global_20 = ("Comic Sans MS", 20, "bold") # Having font_global equal to differnt font style specifications with a size of 20.
font_global_15_underlined = ("Comic Sans MS", 15, "underline") # Having font_global equal to differnt font style specifications with a size of 15 underlined.
button_background = ('green') # Changing the button background to green by making it a variable.
button_text = ('white') # Changing the button text colour to white by making it a variable.

# Define Functions----------------------------------------------------------------------------------------------------------------------------------------------------

def pizza_palace(): # Defining the funtion of pizza_Palace when called.
    window.destroy() # Asking the python window to be destroyed.
    os.system("python joshua_paterson_as91896_henderson_pizza_palace.py") # Asking the operating system (os) to open the pizza palace python script on the computer.
    sys.exit() # Asking the python system to exit this python programe.

def open_evening(): # Defining the funtion of open_evening when called.
    window.destroy() # Asking the python window to be destroyed.
    os.system("python open_evening_script.py") # Asking the operating system (os) to open the open evening python script on the computer.
    sys.exit() # Asking the python system to exit this python programe.
    
def login(): # Defining the funtion of login when called.
    global input_login_user # Making the input_login_user variable global to apply to all functions in this script.
    global input_login_pass # Making the input_login_pass variable global to apply to all functions in this script.
    global label_1 # Making the label_1 variable global to apply to all functions in this script.
    global label_2 # Making the label_2 variable global to apply to all functions in this script.
    global b1 # Making the b1 variable global to apply to all functions in this script.
    global menu_view # Making the menu_view variable global to apply to all functions in this script.
    global new_order_login # Making the new_order_login variable global to apply to all functions in this script.
    global label_password # Making the label_password variable global to apply to all functions in this script.
    global label_username # Making the label_username variable global to apply to all functions in this script.
    global canva # Making the canva variable global to apply to all functions in this script.

    window.title("Henderson Pizza Palace | Login") # Changing the title of the window according to the function.

    canva = tk.Canvas(window, width = 1000, height = 750) # Setting the image for the canva canvas.    
    canva.pack() # Putting the canvas button onto the GUI platform.       
    img = tk.PhotoImage(file="images/henderson_pizza_palace/henderson_pizza_palace_logo_w_word_1.png") # Setting the image for the canva canvas.   
    canva.create_image(500, 250, image=img) # Positioning the canva image to a designated x and y positions according to the size of the window.

    label_username = tk.Label(window, font=font_global, text="Please insert your username?") # Creating a label asking the user for their username.
    label_username.pack() # Putting the label_username label onto the GUI platform.
    label_username.place(relx=0.33, rely=0.70) # Positioning the label_username label to a designated x and y positions according to the size of the window.

    label_password = tk.Label(window, font=font_global, text="Please insert your password?") # Creating a label asking the user for their password.
    label_password.pack() # Putting the label_password label onto the GUI platform.
    label_password.place(relx=0.33, rely=0.75) # Positioning the label_password label to a designated x and y positions according to the size of the window.
        
    input_login_user = tk.Text(window, font=font_global, height = 1, width = 10) # Create input box allowing the user to provide an input.
    input_login_user.pack() # Putting the input_login_user input box onto the GUI platform.
    input_login_user.place(relx=0.53, rely=0.70) # Positioning the input_login_user input box to a designated x and y positions according to the size of the window.

    input_login_pass = tk.Text(window, font=font_global, height = 1, width = 10) # Create input box allowing the user to provide an input.
    input_login_pass.pack() # Putting the new_order_menu input box onto the GUI platform.
    input_login_pass.place(relx=0.53, rely=0.75) # Positioning the input_login_pass input box to a designated x and y positions according to the size of the window.
                                                     
    menu_view = tk.Button(window, text ="View menu", bg=button_background, fg=button_text, font=font_global, width=20, command=view_menu) # Creating a button for users to view the menu.
    menu_view.pack() # Putting the menu_view button onto the GUI platform.
    menu_view.place(relx=0.50, rely=0.8) # Positioning the menu_view button to a designated x and y positions according to the size of the window.
    
    new_order_login = tk.Button(window, text ="Place a new order", bg=button_background, fg=button_text, font=font_global, width=20, command=verify) # Creating a button for users to login and verify their credentials.
    new_order_login.pack() # Putting the new_order_login button onto the GUI platform.
    new_order_login.place(relx=0.30, rely=0.8) # Positioning the new_order_login button to a designated x and y positions according to the size of the window.
    
    window.mainloop() # Running the window loop.

def verify(): # Defining the funtion of verify when called.

    username = input_login_user.get(1.0, "end-1c").strip() # Getting the user input from input_login_user and making it equal to username.
    password = input_login_pass.get(1.0, "end-1c").strip() # Getting the user input from input_login_pass and making it equal to password.

    if username in credential: # If the username is correct/matches in the credential dictonary, execute the following actions.
        if password == credential[username]['password']: # If the username matches the correct password set in the credential dictonary, execute the following actions.
            service_needed() # Call the services_needed function.
        else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
            from tkinter import messagebox # Importing a message box from tkrinter for the message below.
            tk.messagebox.showerror('Incorret Username/Password', 'Sorry, you have entered an incorrect username/password.') # Inform the user that the user has entered incorrect details.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        from tkinter import messagebox # Importing a message box from tkrinter for the message below.
        tk.messagebox.showerror('Incorret Username/Password', 'Sorry, you have entered an incorrect username/password.') # Inform the user that the user has entered incorrect details.

def view_menu(): # Defining the funtion of view_menu when called.

    global canvas # Making the canvas variable global to apply to all functions in this script.
    global new_order_menu # Making the new_order_menu variable global to apply to all functions in this script.

    input_login_user.place_forget() # Forget the object/Delete the object from the window.
    input_login_pass.place_forget() # Forget the object/Delete the object from the window.
    menu_view.place_forget() # Forget the object/Delete the object from the window.
    new_order_login.place_forget() # Forget the object/Delete the object from the window.
    label_username.place_forget() # Forget the object/Delete the object from the window.
    label_password.place_forget() # Forget the object/Delete the object from the window.

    window.title("Henderson Pizza Palace | View Menu") # Changing the title of the window according to the function.

    canva.config(width=0, height=0) # Configuring the canva's size to (0X0).

    canvas = tk.Canvas(window, width = 725, height = 700) # Launching the Canvas to the designated width and height.      
    canvas.pack() # Putting the canvas button onto the GUI platform. 
    img1 = tk.PhotoImage(file="images/henderson_pizza_palace/menu.png") # Setting the image for the canvas.
    canvas.create_image(375, 350, image=img1) # Positioning the canvas image to a designated x and y positions according to the size of the window.

    new_order_menu = tk.Button(window, text =("Place a new order"), bg=button_background, fg=button_text, font=font_global, width=20, command=menu_hide) # Creating a button for users to place a new order.
    new_order_menu.pack() # Putting the new_order_menu button onto the GUI platform.
    new_order_menu.place(relx=.02, rely=.95) # Positioning the new_order_menu button to a designated x and y positions according to the size of the window.

    login_page_menu = tk.Button(window, text =("Login/HomePage"), bg=button_background, fg=button_text, font=font_global, width=20, command=menu_hide) # Creating a button for users to go back to the home page.
    login_page_menu.pack() # Putting the login_page_menu button onto the GUI platform.
    login_page_menu.place(relx=.800, rely=.95) # Positioning the login_page_menu button to a designated x and y positions according to the size of the window.

    window.mainloop() # Running the window loop.

def menu_hide(): # Defining the funtion of menu_hide when called.
    new_order_menu.place_forget() # Forget the object/Delete the object from the window.
    canvas.config(width=0, height=0) # Set the canvas size to (0X0).
    login() # Call the login function.

def service_needed(): # Defining the funtion of services_needed when called.
    global pickup_button # Making the pickup_button variable global to apply to all functions in this script.
    global delivery_button # Making the delivery_button variable global to apply to all functions in this script.
    global services_display # Making the services_display variable global to apply to all functions in this script.
    
    input_login_user.place_forget() # Forget the object/Delete the object from the window.
    input_login_pass.place_forget() # Forget the object/Delete the object from the window.
    menu_view.place_forget() # Forget the object/Delete the object from the window.
    new_order_login.place_forget() # Forget the object/Delete the object from the window.
    label_username.place_forget() # Forget the object/Delete the object from the window.
    label_password.place_forget() # Forget the object/Delete the object from the window.
    
    window.title("Henderson Pizza Palace | Service Required") # Changing the title of the window according to the function.

    canvas = tk.Canvas(window, width = 725, height = 700) # Launching the Canvas to the designated width and height.      
    canvas.pack() # Putting the canvas button onto the GUI platform. 
    img1 = tk.PhotoImage(file="images/henderson_pizza_palace/menu.png") # Setting the image for the canvas.
    canvas.create_image(375, 350, image=img1) # Positioning the canvas image to a designated x and y positions according to the size of the window.

    services_display = tk.Label(window, text="Is this order for pick-up or delivery?", font=font_global) # Creating a label asking the user what delivery option they would like to use.
    services_display.pack() # Putting the services_display label onto the GUI platform.
    services_display.place(relx=0.4, rely=0.75) # Positioning the services_display label to a designated x and y positions according to the size of the window.

    delivery_button = tk.Button(window, text =("Delivery"), bg=button_background, fg=button_text, font=font_global, width=20, command=delivery) # Creating a button which will take the user to the delivery function/new order function.
    delivery_button.pack() # Putting the delivery_button button onto the GUI platform.
    delivery_button.place(relx=0.53, rely=0.8) # Positioning the delivery_button button to a designated x and y positions according to the size of the window.

    pickup_button = tk.Button(window, text =("Pick-Up"), bg=button_background, fg=button_text, font=font_global, width=20, command=pick_up) # Creating a button which will take the user to the pick-up function/new order function.
    pickup_button.pack() # Putting the pickup_button button onto the GUI platform.
    pickup_button.place(relx=0.33, rely=0.8) # Positioning the pickup_button button to a designated x and y positions according to the size of the window.

    dtime() # Directing the function to the dtime def/function.

def pick_up(): # Defining the funtion of pizza_Palace when called.

    global service_chosen # Making the service_chosen variable global to apply to all functions in this script.

    services_display.place_forget() # Forget the object/Delete the object from the window.
    pickup_button.place_forget() # Forget the object/Delete the object from the window.
    delivery_button.place_forget() # Forget the object/Delete the object from the window. 

    from tkinter import messagebox # Importing a message box from tkrinter for the message below.
    pick_up_confirmation = tk.messagebox.askquestion ('Pick-Up Confirmation', 'Please confirm this order is for Pick Up at Henderson High School?', icon = 'warning') # Confirming with the user that they have selected the correct delivery option.
    if pick_up_confirmation == 'yes': # If the user selects yes, it redirects the programe to the actions below.
        service_chosen = 'Pick-Up' # Change the service_chosen variable to equal to Pick Up.
        services_display.place_forget() # Forget the object/Delete the object from the window.
        new_order() # Call the new_order function.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        service_needed() # Return to the services_needed function.

def delivery(): # Defining the funtion of delivery when called.

    global service_chosen # Making the service_chosen variable global to apply to all functions in this script.

    services_display.place_forget() # Forget the object/Delete the object from the window.
    pickup_button.place_forget() # Forget the object/Delete the object from the window.
    delivery_button.place_forget() # Forget the object/Delete the object from the window. 
    
    from tkinter import messagebox # Importing a message box from tkrinter for the message below.
    delivery_confirmation = tk.messagebox.askquestion ('Delivery Confirmation', 'Please confirm this order is for delivery for an extra $3?', icon = 'warning') # Confirming with the user that they have selected the correct delivery option. 
    if delivery_confirmation == 'yes': # If the user selects yes, it redirects the programe to the actions below.
        service_chosen = 'Delivery' # Change the service_chosen variable to equal to Delivery.
        new_order() # Call the new_order function.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        service_needed() # Return to the services_needed function.

def new_order(): # Defining the funtion of new_order when called.
        global ordertotal # Making the info varable global to use in all functions in this script.
        global regular_price # Making the info varable global to use in all functions in this script.
        global gourmet_price # Making the info varable global to use in all functions in this script.
        global pizza_1_option # Making the pizza_1_option varable global to use in all functions in this script.
        global pizza_2_option # Making the pizza_2_option varable global to use in all functions in this script.
        global pizza_3_option # Making the pizza_3_option varable global to use in all functions in this script.
        global pizza_4_option # Making the pizza_4_option varable global to use in all functions in this script.
        global pizza_5_option # Making the pizza_5_option varable global to use in all functions in this script.
        global pizza_6_option # Making the pizza_6_option varable global to use in all functions in this script.
        global pizza_7_option # Making the pizza_7_option varable global to use in all functions in this script.
        global pizza_8_option # Making the pizza_8_option varable global to use in all functions in this script.
        global pizza_9_option # Making the pizza_9_option varable global to use in all functions in this script.
        global pizza_10_option # Making the pizza_10_option varable global to use in all functions in this script.
        global pizza_11_option # Making the pizza_11_option varable global to use in all functions in this script.
        global pizza_12_option # Making the pizza_12_option varable global to use in all functions in this script.
        global pizza_1_display # Making the pizza_1_display varable global to use in all functions in this script.
        global pizza_2_display # Making the pizza_2_display varable global to use in all functions in this script.
        global pizza_3_display # Making the pizza_3_display varable global to use in all functions in this script.
        global pizza_4_display # Making the pizza_4_display varable global to use in all functions in this script.
        global pizza_5_display # Making the pizza_5_display varable global to use in all functions in this script.
        global pizza_6_display # Making the pizza_6_display varable global to use in all functions in this script.
        global pizza_7_display # Making the pizza_7_display varable global to use in all functions in this script.
        global pizza_8_display # Making the pizza_8_display varable global to use in all functions in this script.
        global pizza_9_display # Making the pizza_9_display varable global to use in all functions in this script.
        global pizza_10_display # Making the pizza_10_display varable global to use in all functions in this script.
        global pizza_11_display # Making the pizza_11_display varable global to use in all functions in this script.
        global pizza_12_display # Making the pizza_12_display varable global to use in all functions in this script.
        global toppings_button # Making the toppings_button varable global to use in all functions in this script.

        window.title("Henderson Pizza Palace | New Order") # Changing the title of the window pop-up accordng to the function.
        window.geometry("1200x700") # Changing the window pop-up size to the set amount stated.

        ordertotal = 0 # Setting the order total as 0 at the beginning of the function.

        canva.config(width=0, height=0) # Set the canvas size to (0X0).D
        
        regular_price = 8.5 # Setting the current price of the regular pizza's.
        gourmet_price = 13.5 # Setting the current price of the gourment pizza's.

        pizza_1_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 1"], regular_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 1 option.
        pizza_2_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 2"], regular_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 2 option.
        pizza_3_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 3"], regular_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 3 option.
        pizza_4_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 4"], regular_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 4 option.
        pizza_5_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 5"], regular_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 5 option.
        pizza_6_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 6"], regular_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 6 option.
        pizza_7_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 7"], regular_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 7 option.
        pizza_8_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 8"], gourmet_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 8 option.
        pizza_9_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 9"], gourmet_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 9 option.
        pizza_10_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 10"], gourmet_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 10 option.
        pizza_11_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 11"], gourmet_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 11 option.
        pizza_12_display = tk.Label(window, text="{} - ${} = ".format(pizza_options["Pizza 12"], gourmet_price), font=font_global_20) # Creating a label asking the user how many pizza's they want from the Pizza 12 option.
        
        pizza_1_display.pack() # Putting the pizza_1_display label onto the GUI platform.
        pizza_2_display.pack() # Putting the pizza_2_display label onto the GUI platform.
        pizza_3_display.pack() # Putting the pizza_3_display label onto the GUI platform.
        pizza_4_display.pack() # Putting the pizza_4_display label onto the GUI platform.
        pizza_5_display.pack() # Putting the pizza_5_display label onto the GUI platform.
        pizza_6_display.pack() # Putting the pizza_6_display label onto the GUI platform.
        pizza_7_display.pack() # Putting the pizza_7_display label onto the GUI platform.
        pizza_8_display.pack() # Putting the pizza_8_display label onto the GUI platform.
        pizza_9_display.pack() # Putting the pizza_9_display label onto the GUI platform.
        pizza_10_display.pack() # Putting the pizza_10_display label onto the GUI platform.
        pizza_11_display.pack() # Putting the pizza_11_display label onto the GUI platform.
        pizza_12_display.pack() # Putting the pizza_12_display label onto the GUI platform.

        pizza_1_display.place(relx=0.1, rely=0.3) # Positioning the pizza_1_display label to a designated x and y positions according to the size of the window.
        pizza_2_display.place(relx=0.1, rely=0.4) # Positioning the pizza_2_display label to a designated x and y positions according to the size of the window.
        pizza_3_display.place(relx=0.1, rely=0.5) # Positioning the pizza_3_display label to a designated x and y positions according to the size of the window.
        pizza_4_display.place(relx=0.1, rely=0.6) # Positioning the pizza_4_display label to a designated x and y positions according to the size of the window.
        pizza_5_display.place(relx=0.1, rely=0.7) # Positioning the pizza_5_display label to a designated x and y positions according to the size of the window.
        pizza_6_display.place(relx=0.1, rely=0.8) # Positioning the pizza_6_display label to a designated x and y positions according to the size of the window.
        pizza_7_display.place(relx=0.6, rely=0.3) # Positioning the pizza_7_display label to a designated x and y positions according to the size of the window.
        pizza_8_display.place(relx=0.6, rely=0.4) # Positioning the pizza_8_display label to a designated x and y positions according to the size of the window.
        pizza_9_display.place(relx=0.6, rely=0.5) # Positioning the pizza_9_display label to a designated x and y positions according to the size of the window.
        pizza_10_display.place(relx=0.6, rely=0.6) # Positioning the pizza_10_display label to a designated x and y positions according to the size of the window.
        pizza_11_display.place(relx=0.6, rely=0.7) # Positioning the pizza_11_display label to a designated x and y positions according to the size of the window.
        pizza_12_display.place(relx=0.6, rely=0.8) # Positioning the pizza_12_display label to a designated x and y positions according to the size of the window.
        
        pizza_1_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_1_option.place(relx=0.35, rely=0.3) # Positioning the pizza_1_option combobox to a designated x and y positions according to the size of the window.
        pizza_1_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_2_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_2_option.place(relx=0.35, rely=0.4) # Positioning the pizza_2_option combobox to a designated x and y positions according to the size of the window.
        pizza_2_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_3_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_3_option.place(relx=0.35, rely=0.5) # Positioning the pizza_3_option combobox to a designated x and y positions according to the size of the window.
        pizza_3_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_4_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_4_option.place(relx=0.35, rely=0.6) # Positioning the pizza_4_option combobox to a designated x and y positions according to the size of the window.
        pizza_4_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_5_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_5_option.place(relx=0.35, rely=0.7) # Positioning the pizza_5_option combobox to a designated x and y positions according to the size of the window.
        pizza_5_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_6_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_6_option.place(relx=0.35, rely=0.8) # Positioning the pizza_6_option combobox to a designated x and y positions according to the size of the window.
        pizza_6_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_7_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_7_option.place(relx=0.915, rely=0.3) # Positioning the pizza_7_option combobox to a designated x and y positions according to the size of the window.
        pizza_7_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_8_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_8_option.place(relx=0.915, rely=0.4) # Positioning the pizza_8_option combobox to a designated x and y positions according to the size of the window.
        pizza_8_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_9_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_9_option.place(relx=0.915, rely=0.5) # Positioning the pizza_9_option combobox to a designated x and y positions according to the size of the window.
        pizza_9_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_10_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_10_option.place(relx=0.915, rely=0.6) # Positioning the pizza_10_option combobox to a designated x and y positions according to the size of the window.
        pizza_10_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_11_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_11_option.place(relx=0.915, rely=0.7) # Positioning the pizza_11_option combobox to a designated x and y positions according to the size of the window.
        pizza_11_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        pizza_12_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_20, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        pizza_12_option.place(relx=0.915, rely=0.8) # Positioning the pizza_12_option combobox to a designated x and y positions according to the size of the window.
        pizza_12_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.
           
        toppings_button = tk.Button(window, text =("Toppings"), bg=button_background, fg=button_text, font=font_global, width=20, command=toppings) # Created a button directing the user to the toppings function.
        toppings_button.pack() # Putting the toppings_button button onto the GUI platform.
        toppings_button.place(relx=.8, rely=.95) # Positioning the toppings_button button to a designated x and y positions according to the size of the window.

def toppings(): # Defining the funtion of restart when called.

    global cart_buton_order_page # Making the cart_buton_order_page varable global to use in all functions in this script.
    global pizza_1_total # Making the pizza_1_total variable global to apply to all functions in this script.
    global pizza_2_total # Making the pizza_2_total variable global to apply to all functions in this script.
    global pizza_3_total # Making the pizza_3_total variable global to apply to all functions in this script.
    global pizza_4_total # Making the pizza_4_total variable global to apply to all functions in this script.
    global pizza_5_total # Making the pizza_5_total variable global to apply to all functions in this script.
    global pizza_6_total # Making the pizza_6_total variable global to apply to all functions in this script.
    global pizza_7_total # Making the pizza_7_total variable global to apply to all functions in this script.
    global pizza_8_total # Making the pizza_8_total variable global to apply to all functions in this script.
    global pizza_9_total # Making the pizza_9_total variable global to apply to all functions in this script.
    global pizza_10_total # Making the pizza_10_total variable global to apply to all functions in this script.
    global pizza_11_total # Making the pizza_11_total variable global to apply to all functions in this script.
    global pizza_12_total # Making the pizza_12_total variable global to apply to all functions in this script.
    global ordertotal_display # Making the ordertotal_display variable global to apply to all functions in this script.
    global ordertotal # Making the ordertotal variable global to apply to all functions in this script.t # Making the ordertotal_cost variable global to apply to all functions in this script. 
    global ordertotal_cost # Making the ordertotal_cost variable global to apply to all functions in this script. 
    global topping_1_display # Making the topping_1_display variable global to apply to all functions in this script.
    global topping_2_display # Making the topping_2_display variable global to apply to all functions in this script.
    global topping_3_display # Making the topping_3_display variable global to apply to all functions in this script.
    global topping_4_display # Making the topping_4_display variable global to apply to all functions in this script.
    global topping_1_option # Making the topping_1_option variable global to apply to all functions in this script.
    global topping_2_option # Making the topping_2_option variable global to apply to all functions in this script.
    global topping_3_option # Making the topping_3_option variable global to apply to all functions in this script.
    global topping_4_option # Making the topping_4_option variable global to apply to all functions in this script.
    global topping_notes # Making the topping_notes variable global to apply to all functions in this script.
    global customer_topping_notes # Making the customer_topping_notes variable global to apply to all functions in this script.

    toppings_button.place_forget() # Forget the object/Delete the object from the window.
    pizza_1_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_2_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_3_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_4_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_5_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_6_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_7_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_8_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_9_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_10_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_11_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_12_option.place_forget() # Forget the object/Delete the object from the window.
    pizza_1_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_2_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_3_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_4_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_5_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_6_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_7_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_8_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_9_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_10_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_11_display.place_forget() # Forget the object/Delete the object from the window.
    pizza_12_display.place_forget() # Forget the object/Delete the object from the window.

    window.title("Henderson Pizza Palace | Pizza Toppings") # Changing the title of the window pop-up accordng to the function.
    window.geometry("1400x800") # Changing the window pop-up size to the set amount stated.

    ordertotal += int(pizza_1_option.get()) # Retreive the input from pizza_1_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_2_option.get()) # Retreive the input from pizza_2_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_3_option.get()) # Retreive the input from pizza_3_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_4_option.get()) # Retreive the input from pizza_4_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_5_option.get()) # Retreive the input from pizza_5_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_6_option.get()) # Retreive the input from pizza_6_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_7_option.get()) # Retreive the input from pizza_7_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_8_option.get()) # Retreive the input from pizza_8_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_9_option.get()) # Retreive the input from pizza_9_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_10_option.get()) # Retreive the input from pizza_10_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_11_option.get()) # Retreive the input from pizza_11_option and add the quanity of the pizzas to the ordertotal count.
    ordertotal += int(pizza_12_option.get()) # Retreive the input from pizza_12_option and add the quanity of the pizzas to the ordertotal count.

    if 1 <= ordertotal <= 5: # Only execute the following commands if the user has ordered between 1 and 5 pizzas.

        pizza_1_total = int(pizza_1_option.get())*regular_price # Multiplying the pizza_1_option quanitity with the price of the pizza to equal the variable name pizza_1_total.
        pizza_2_total = int(pizza_2_option.get())*regular_price # Multiplying the pizza_2_option quanitity with the price of the pizza to equal the variable name pizza_2_total.
        pizza_3_total = int(pizza_3_option.get())*regular_price # Multiplying the pizza_3_option quanitity with the price of the pizza to equal the variable name pizza_3_total.
        pizza_4_total = int(pizza_4_option.get())*regular_price # Multiplying the pizza_4_option quanitity with the price of the pizza to equal the variable name pizza_4_total.
        pizza_5_total = int(pizza_5_option.get())*regular_price # Multiplying the pizza_5_option quanitity with the price of the pizza to equal the variable name pizza_5_total.
        pizza_6_total = int(pizza_6_option.get())*regular_price # Multiplying the pizza_6_option quanitity with the price of the pizza to equal the variable name pizza_6_total.
        pizza_7_total = int(pizza_7_option.get())*regular_price # Multiplying the pizza_7_option quanitity with the price of the pizza to equal the variable name pizza_7_total.
        pizza_8_total = int(pizza_8_option.get())*gourmet_price # Multiplying the pizza_8_option quanitity with the price of the pizza to equal the variable name pizza_8_total.
        pizza_9_total = int(pizza_9_option.get())*gourmet_price # Multiplying the pizza_9_option quanitity with the price of the pizza to equal the variable name pizza_9_total.
        pizza_10_total = int(pizza_10_option.get())*gourmet_price # Multiplying the pizza_10_option quanitity with the price of the pizza to equal the variable name pizza_10_total.
        pizza_11_total = int(pizza_11_option.get())*gourmet_price # Multiplying the pizza_11_option quanitity with the price of the pizza to equal the variable name pizza_11_total.
        pizza_12_total = int(pizza_12_option.get())*gourmet_price # Multiplying the pizza_12_option quanitity with the price of the pizza to equal the variable name pizza_12_total.

        ordertotal_display = tk.Label(window, text=("Total Amount of Pizza's - {}".format(ordertotal)), font=font_global_20) # Created a label to inform the user if the total amount of pizzas being ordered from the ordertotal.
        ordertotal_display.pack() # Putting the ordertotal_display label onto the GUI platform.
        ordertotal_display.place(relx=0.3, rely=0.05) # Positioning the ordertotal_display label to a designated x and y positions according to the size of the window.

        topping_1_display = tk.Label(window, text="Topping 1 - {}".format(topping_options[0]), font=font_global_15) # Creating a label asking the user how many toppings's they want.
        topping_2_display = tk.Label(window, text="Topping 2 - {}".format(topping_options[1]), font=font_global_15) # Creating a label asking the user how many toppings's they want.
        topping_3_display = tk.Label(window, text="Topping 3 - {}".format(topping_options[2]), font=font_global_15) # Creating a label asking the user how many toppings's they want.
        topping_4_display = tk.Label(window, text="Topping 4 - {}".format(topping_options[3]), font=font_global_15) # Creating a label asking the user how many toppings's they want.

        topping_1_display.pack() # Putting the topping_1_display label onto the GUI platform.
        topping_2_display.pack() # Putting the topping_2_display label onto the GUI platform.
        topping_3_display.pack() # Putting the topping_3_display label onto the GUI platform.
        topping_4_display.pack() # Putting the topping_4_display label onto the GUI platform.

        topping_1_display.place(relx=0.54, rely=0.25) # Positioning the topping_1_display label to a designated x and y positions according to the size of the window.
        topping_2_display.place(relx=0.575, rely=0.3) # Positioning the topping_2_display label to a designated x and y positions according to the size of the window.
        topping_3_display.place(relx=0.775, rely=0.25) # Positioning the topping_3_display label to a designated x and y positions according to the size of the window.
        topping_4_display.place(relx=0.775, rely=0.3) # Positioning the topping_4_display label to a designated x and y positions according to the size of the window.

        topping_1_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_15, width=2) # Created a combobox asking the user for how many toppings they would like on topping_1_option.
        topping_1_option.place(relx=0.7, rely=0.25) # Positioning the topping_1_option combobox to a designated x and y positions according to the size of the window.
        topping_1_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        topping_2_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_15, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        topping_2_option.place(relx=0.72, rely=0.3) # Positioning the pizza_2_option combobox to a designated x and y positions according to the size of the window.
        topping_2_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        topping_3_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_15, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        topping_3_option.place(relx=0.95, rely=0.25) # Positioning the pizza_3_option combobox to a designated x and y positions according to the size of the window.
        topping_3_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        topping_4_option = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5], state="readonly", font=font_global_15, width=2) # Created a combobox asking the user for how many pizzas they would like of pizza_1_option.
        topping_4_option.place(relx=0.95, rely=0.3) # Positioning the pizza_4_option combobox to a designated x and y positions according to the size of the window.
        topping_4_option.current(0) # Setting the defult responce to 0 should the operator not need this pizza.

        customer_topping_notes = tk.Text(window, font=font_global, height = 4, width = 50) # Create input box allowing the user to provide an input.
        customer_topping_notes.pack() # Putting the customer_topping_notes input box onto the GUI platform.
        customer_topping_notes.place(relx=.6, rely=.41) # Positioning the customer_topping_notes input box to a designated x and y positions according to the size of the window.

        topping_notes = tk.Label(window, text=("Topping Notes"), font=font_global) # Created a label asking the user to insert notes about toppings below.
        topping_notes.pack() # Putting the topping_notes label onto the GUI platform.
        topping_notes.place(relx=0.6, rely=0.3725) # Positioning the topping_notes label to a designated x and y positions according to the size of the window.

        cart_buton_order_page = tk.Button(window, text =("Order Review"), bg=button_background, fg=button_text, font=font_global, width=20, command=order_review) # Created a button directing the user to the toppings function.
        cart_buton_order_page.pack() # Putting the cart_buton_order_page button onto the GUI platform.
        cart_buton_order_page.place(relx=.8, rely=.95) # Positioning the cart_buton_order_page button to a designated x and y positions according to the size of the window.

    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        from tkinter import messagebox # Importing a message box from tkrinter for the message below.
        answer = messagebox.askretrycancel("Too Many Items In The Cart", "There are more than 5 items in the cart or there are no item in the cart, please try again.") # Informing the user that there is an error and they need to recomplete the order.
        if answer == 'retry': # Only if the user click the retry button will the command below will be executed. 
            new_order() # Send thre user back to new_order page as the user ordered no pizzas or the user ordered too many pizzas.
        else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed. 
            new_order() # Send the user back to new_order page as the user ordered no pizzas or the user ordered too many pizzas.

            window.mainloop()

def order_review(): # Defining the funtion of order_review when called.

            global pizza_1 # Making the pizza_1 variable global to apply to all functions in this script.
            global pizza_2 # Making the pizza_2 variable global to apply to all functions in this script.
            global pizza_3 # Making the pizza_3 variable global to apply to all functions in this script.
            global pizza_4 # Making the pizza_4 variable global to apply to all functions in this script.
            global pizza_5 # Making the pizza_5 variable global to apply to all functions in this script.
            global pizza_6 # Making the pizza_6 variable global to apply to all functions in this script.
            global pizza_7 # Making the pizza_7 variable global to apply to all functions in this script.
            global pizza_8 # Making the pizza_8 variable global to apply to all functions in this script.
            global pizza_9 # Making the pizza_9 variable global to apply to all functions in this script.
            global pizza_10 # Making the pizza_10 variable global to apply to all functions in this script.
            global pizza_11 # Making the pizza_11 variable global to apply to all functions in this script.
            global pizza_12 # Making the pizza_12 variable global to apply to all functions in this script.
            global order_details # Making the order_details variable global to apply to all functions in this script.
            global recomplete_order # Making the recomplete_order variable global to apply to all functions in this script.
            global services_needed # Making the services_needed variable global to apply to all functions in this script.
            global topping_info # Making the topping_info variable global to apply to all functions in this script. 
            global topping_4_total_price # Making the topping_4_total_price variable global to apply to all functions in this script.      
            global topping_3_total_price # Making the topping_3_total_price variable global to apply to all functions in this script.      
            global topping_2_total_price # Making the topping_2_total_price variable global to apply to all functions in this script.      
            global topping_1_total_price # Making the topping_1_total_price variable global to apply to all functions in this script.                     

            toppings_button.place_forget() # Forget the object/Delete the object from the window.
            customer_topping_notes.place_forget() # Forget the object/Delete the object from the window.
            topping_notes.place_forget() # Forget the object/Delete the object from the window.
            topping_1_option.place_forget() # Forget the object/Delete the object from the window.
            topping_2_option.place_forget() # Forget the object/Delete the object from the window.
            topping_3_option.place_forget() # Forget the object/Delete the object from the window.
            topping_4_option.place_forget() # Forget the object/Delete the object from the window.
            topping_1_display.place_forget() # Forget the object/Delete the object from the window.
            topping_2_display.place_forget() # Forget the object/Delete the object from the window.
            topping_3_display.place_forget() # Forget the object/Delete the object from the window.
            topping_4_display.place_forget() # Forget the object/Delete the object from the window.

            topping_1_total_price = int(topping_1_option.get())*0.5 # Multiplying the topping_1_option quanitity with the price of the topping price (0.50c).
            topping_2_total_price = int(topping_2_option.get())*0.5 # Multiplying the topping_2_option quanitity with the price of the topping price (0.50c).
            topping_3_total_price = int(topping_3_option.get())*0.5 # Multiplying the topping_3_option quanitity with the price of the topping price (0.50c).
            topping_4_total_price = int(topping_4_option.get())*0.5 # Multiplying the topping_4_option quanitity with the price of the topping price (0.50c).
        
            global grandtotal # Making the grandtotal variable global to apply to all functions in this script.
            grandtotal = 0 # Set the grandtotal (total cost price) to 0.

            grandtotal += pizza_1_total # Adding the pizza_1_total to the final grandtotal cost.
            grandtotal += pizza_2_total # Adding the pizza_2_total to the final grandtotal cost.
            grandtotal += pizza_3_total # Adding the pizza_3_total to the final grandtotal cost.
            grandtotal += pizza_4_total # Adding the pizza_4_total to the final grandtotal cost.
            grandtotal += pizza_5_total # Adding the pizza_5_total to the final grandtotal cost.
            grandtotal += pizza_6_total # Adding the pizza_6_total to the final grandtotal cost.
            grandtotal += pizza_7_total # Adding the pizza_7_total to the final grandtotal cost.
            grandtotal += pizza_8_total # Adding the pizza_8_total to the final grandtotal cost.
            grandtotal += pizza_9_total # Adding the pizza_9_total to the final grandtotal cost.
            grandtotal += pizza_10_total # Adding the pizza_10_total to the final grandtotal cost.
            grandtotal += pizza_11_total # Adding the pizza_11_total to the final grandtotal cost.
            grandtotal += pizza_12_total # Adding the pizza_12_total to the final grandtotal cost.
            
            grandtotal += topping_1_total_price # Adding the topping_1_total_price to the final grandtotal cost.
            grandtotal += topping_2_total_price # Adding the topping_2_total_price to the final grandtotal cost.
            grandtotal += topping_3_total_price # Adding the topping_3_total_price to the final grandtotal cost.
            grandtotal += topping_4_total_price # Adding the topping_4_total_price to the final grandtotal cost.
              
            topping_info = tk.Label(window, text=("Topping Notes - {}".format(customer_topping_notes.get("1.0", END))), font=font_global) # Created a label informing the user of the topping notes.
            topping_info.pack() # Putting the topping_info label onto the GUI platform.
            topping_info.place(relx=0.6, rely=0.3725) # Positioning the topping_info label to a designated x and y positions according to the size of the window.

            if pizza_1_total >= 1: # Only execute the following action if pizza_1_total is above 1.
                pizza_1 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 1"], pizza_1_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_1.pack() # Putting the pizza_1 label onto the GUI platform.
                pizza_1.place(relx=0.05, rely=0.6) # Positioning the pizza_1 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_1 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_2_total >= 1: # Only execute the following action if pizza_2_total is above 1.
                pizza_2 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 2"], pizza_2_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_2.pack() # Putting the pizza_2 label onto the GUI platform.
                pizza_2.place(relx=0.05, rely=0.7) # Positioning the pizza_2 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_2 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_3_total >= 1: # Only execute the following action if pizza_3_total is above 1.
                pizza_3 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 3"], pizza_3_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_3.pack() # Putting the pizza_3 label onto the GUI platform.
                pizza_3.place(relx=0.05, rely=0.8) # Positioning the pizza_3 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_3 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_4_total >= 1: # Only execute the following action if pizza_4_total is above 1.
                pizza_4 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 4"], pizza_4_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_4.pack() # Putting the pizza_4 label onto the GUI platform.
                pizza_4.place(relx=0.05, rely=0.9) # Positioning the pizza_4 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_4 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_5_total >= 1: # Only execute the following action if pizza_5_total is above 1.
                pizza_5 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 5"], pizza_5_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_5.pack() # Putting the pizza_5 label onto the GUI platform.
                pizza_5.place(relx=0.4, rely=0.6) # Positioning the pizza_5 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_5 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_6_total >= 1: # Only execute the following action if pizza_6_total is above 1.
                pizza_6 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 6"], pizza_6_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_6.pack() # Putting the pizza_6 label onto the GUI platform.
                pizza_6.place(relx=0.4, rely=0.7) # Positioning the pizza_6 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_6 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_7_total >= 1: # Only execute the following action if pizza_7_total is above 1.
                pizza_7 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 7"], pizza_7_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_7.pack() # Putting the pizza_7 label onto the GUI platform.
                pizza_7.place(relx=0.4, rely=0.8) # Positioning the pizza_7 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_7 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_8_total >= 1: # Only execute the following action if pizza_8_total is above 1.
                pizza_8 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 8"], pizza_8_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_8.pack() # Putting the pizza_8 label onto the GUI platform.
                pizza_8.place(relx=0.4, rely=0.9) # Positioning the pizza_8 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_8 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_9_total >= 1: # Only execute the following action if pizza_9_total is above 1.
                pizza_9 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 9"], pizza_9_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_9.pack() # Putting the pizza_9 label onto the GUI platform.
                pizza_9.place(relx=0.8, rely=0.6) # Positioning the pizza_9 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_9 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_10_total >= 1: # Only execute the following action if pizza_10_total is above 1.
                pizza_10 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 10"], pizza_10_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_10.pack() # Putting the pizza_10 label onto the GUI platform.
                pizza_10.place(relx=0.8, rely=0.7) # Positioning the pizza_10 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_10 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_11_total >= 1: # Only execute the following action if pizza_11_total is above 1.
                pizza_11 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 11"], pizza_11_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_11.pack() # Putting the pizza_11 label onto the GUI platform.
                pizza_11.place(relx=0.8, rely=0.8) # Positioning the pizza_11 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_11 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if pizza_12_total >= 1: # Only execute the following action if pizza_12_total is above 1.
                pizza_12 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 12"], pizza_12_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
                pizza_12.pack() # Putting the pizza_12 label onto the GUI platform.
                pizza_12.place(relx=0.8, rely=0.9) # Positioning the pizza_12 label to a designated x and y positions according to the size of the window.
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                pizza_12 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

            if service_chosen == "Delivery":
                ordertotal_cost_final = tk.Label(window, text=("Total Cost of Pizza's - ${}".format(grandtotal+3)), font=font_global_20) # Created a label to inform the user if the total cost amount for the pizza's from the grandtotal but with an additional $3 as a flat delivery fee rate.
                ordertotal_cost_final.pack() # Putting the ordertotal_cost label onto the GUI platform.
                ordertotal_cost_final.place(relx=0.3, rely=0.15) # Positioning the ordertotal_cost label to a designated x and y positions according to the size of the window.
                
            else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
                ordertotal_cost = tk.Label(window, text=("Total Cost of Pizza's - ${}".format(grandtotal)), font=font_global_20) # Created a label to inform the user if the total amount for the pizza's from the grandtotal.
                ordertotal_cost.pack() # Putting the ordertotal_cost label onto the GUI platform.
                ordertotal_cost.place(relx=0.3, rely=0.15) # Positioning the ordertotal_cost label to a designated x and y positions according to the size of the window.
           
            order_details = tk.Button(window, text =("Order Details"), bg=button_background, fg=button_text, font=font_global, width=20, command=details) # Created a button allowing the user to then proceed to the details function once they are satisfied with their order.
            order_details.pack() # Putting the order_details button onto the GUI platform.
            order_details.place(relx=.800, rely=.95) # Positioning the order_details button to a designated x and y positions according to the size of the window.

            recomplete_order = tk.Button(window, text =("Re Complete Order/Restart"), bg=button_background, fg=button_text, font=font_global, width=25, command=restart) # Created a button allowing the user to recomplete the order should they not be satisfied with the order.
            recomplete_order.pack() # Putting the recomplete_order button onto the GUI platform.
            recomplete_order.place(relx=.400, rely=.95) # Positioning the recomplete_order button to a designated x and y positions according to the size of the window.

            window.mainloop() # Running the window loop.

def details(): # Defining the funtion of details when called.

    global input_customer_phone_number # Making the input_customer_phone_number variable global to apply to all functions in this script.
    global input_customer_name # Making the input_customer_name variable global to apply to all functions in this script.
    global customer_address # Making the customer_address variable global to apply to all functions in this script.
    global customer_name # Making the customer_name variable global to apply to all functions in this script.
    global customer_phone_number # Making the customer_phone_number variable global to apply to all functions in this script.
    global customer_pickup # Making the customer_pickup variable global to apply to all functions in this script.
    global user_input_phone_number # Making the user_input_phone_number variable global to apply to all functions in this script.
    global user_input_name # Making the user_input_name variable global to apply to all functions in this script.
    global user_input_address # Making the user_input_address variable global to apply to all functions in this script.
    global user_input_pick_up # Making the user_input_pick_up variable global to apply to all functions in this script.
    global payment_button # Making the input_customer_address variable global to apply to all functions in this script.

    pizza_1.place_forget() # Forget the object/Delete the object from the window.
    pizza_2.place_forget() # Forget the object/Delete the object from the window.
    pizza_3.place_forget() # Forget the object/Delete the object from the window.
    pizza_4.place_forget() # Forget the object/Delete the object from the window.
    pizza_5.place_forget() # Forget the object/Delete the object from the window.
    pizza_6.place_forget() # Forget the object/Delete the object from the window.
    pizza_7.place_forget() # Forget the object/Delete the object from the window.
    pizza_8.place_forget() # Forget the object/Delete the object from the window.
    pizza_9.place_forget() # Forget the object/Delete the object from the window.
    pizza_10.place_forget() # Forget the object/Delete the object from the window.
    pizza_11.place_forget() # Forget the object/Delete the object from the window.
    pizza_12.place_forget() # Forget the object/Delete the object from the window.
    recomplete_order.place_forget() # Forget the object/Delete the object from the window.
    order_details.place_forget() # Forget the object/Delete the object from the window.
    topping_info.place_forget() # Forget the object/Delete the object from the window.

    window.title("Henderson Pizza Palace | Customer Details") # Changed title of the window pop-up based on the function active.
    window.geometry("1000x700") # Changing the window pop-up size to the set amount stated.

    customer_name = tk.Label(window, text="Customer's Name:", font=font_global_15_underlined) # Created a label asking the user for the customers name.
    customer_phone_number = tk.Label(window, text="Customer's Phone Number:", font=font_global_15_underlined) # Created a label asking the user for the customers phone number.
    input_customer_name = tk.Text(window, font=font_global, height = 1, width = 26) # Created an input box allowing the user to insert the customers name.
    input_customer_phone_number = tk.Text(window, font=font_global, height = 1, width = 15) # Created an input box allowing the user to insert the customers phone number.

    customer_name.pack() # Putting the customer_name label onto the GUI platform.
    customer_phone_number.pack() # Putting the customer_phone_number label onto the GUI platform.
    input_customer_name.pack() # Putting the input_customer_name label onto the GUI platform.
    input_customer_phone_number.pack() # Putting the input_customer_phone_number label onto the GUI platform.  

    customer_name.place(relx=0.1, rely=0.3) # Positioning the customer_name label to a designated x and y positions according to the size of the window.
    input_customer_name.place(relx=0.29, rely=0.31) # Positioning the input_customer_name input box to a designated x and y positions according to the size of the window.
    customer_phone_number.place(relx=0.1, rely=0.4) # Positioning the customer_phone_number label to a designated x and y positions according to the size of the window.
    input_customer_phone_number.place(relx=0.375, rely=0.41) # Positioning the input_customer_phone_number input box to a designated x and y positions according to the size of the window.


    if service_chosen == "Delivery": # Only execute the following commands if the user selects delivery as their prefered delivery method.
        customer_address = tk.Label(window, text="Customer's Address:", font=font_global_15_underlined) # Created a label asking the user to insert their disired delivery address.
        customer_address.pack() # Putting the pizza_1_display label onto the GUI platform.
        customer_address.place(relx=0.1, rely=0.5) # Positioning the customer_address button to a designated x and y positions according to the size of the window.

        global input_customer_address # Making the input_customer_address variable global to apply to all functions in this script.
        input_customer_address = tk.Text(window, font=font_global, height = 1, width = 20) # Created an input box allowing the user to insert their address.
        input_customer_address.pack() # Putting the pizza_1_display label onto the GUI platform.
        input_customer_address.place(relx=0.31, rely=0.51) # Positioning the input_customer_address input box to a designated x and y positions according to the size of the window.

    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        customer_pickup = tk.Label(window, text="Customer's Pickup Time:", font=font_global_15_underlined) # Created a label asking the user to insert their disired pickup time.
        customer_pickup.pack() # Putting the pizza_1_display label onto the GUI platform.
        customer_pickup.place(relx=0.1, rely=0.5) # Positioning the customer_pickup label to a designated x and y positions according to the size of the window.

        global input_customer_pickup # Making the input_customer_pickup variable global to apply to all functions in this script.
        input_customer_pickup = tk.Text(window, font=font_global, height = 1, width = 18) # Created input box allowing the user to insert the customers pick up time.
        input_customer_pickup.pack() # Putting the pizza_1_display label onto the GUI platform.
        input_customer_pickup.place(relx=0.35, rely=0.51) # Positioning the input_customer_pickup input box to a designated x and y positions according to the size of the window.


    payment_button = tk.Button(window, text ="Payment", bg=button_background, fg=button_text, font=font_global, width=20, command=payment) # Created button allowing the user to go to the payment function when they have confirmed the customers details.
    payment_button.pack() # Putting the pizza_1_display label onto the GUI platform.
    payment_button.place(relx=.8, rely=.95) # Positioning the restart_python button to a designated x and y positions according to the size of the window.

def payment(): # Defining the funtion of payment when called.

    global payment_button_1 # Making the payment_button_1 variable global to apply to all functions in this script.
    global payment_button_2 # Making the payment_button_2 variable global to apply to all functions in this script.
    global payment_button_3 # Making the payment_button_3 variable global to apply to all functions in this script.
    global display_customer_name # Making the display_customer_name variable global to apply to all functions in this script.
    global display_customer_phone_number # Making the display_customer_phone_number variable global to apply to all functions in this script.
    global display_customer_address # Making the display_customer_address variable global to apply to all functions in this script.
    global display_customer_pickup # Making the display_customer_pickup variable global to apply to all functions in this script.

    input_customer_name.place_forget() # Forget the object/Delete the object from the window.
    input_customer_phone_number.place_forget() # Forget the object/Delete the object from the window.
    payment_button.place_forget() # Forget the object/Delete the object from the window.

    window.title("Henderson Pizza Palace | Customer Payment") # Changing the title of the window according to the function.
    window.geometry("1400x800") # Changing the window pop-up size to the set amount stated.

    display_customer_name = tk.Label(window, text=(input_customer_name.get("1.0", END).strip()+'.').capitalize(), font=font_global, height = 2, width = 18) # Create label displaying the customers name using the customers name input, strip and captitalize with a full stop at the end of the label/name.
    display_customer_name.pack() # Putting the display_customer_name label onto the GUI platform.
    display_customer_name.place(relx=0.225, rely=0.3) # Positioning the display_customer_name label to a designated x and y positions according to the size of the window.

    display_customer_phone_number = tk.Label(window, text=input_customer_phone_number.get("1.0", END), font=font_global, height = 2, width = 18) # Create label displaying the customers phone number.
    display_customer_phone_number.pack() # Putting the display_customer_phone_number label onto the GUI platform.
    display_customer_phone_number.place(relx=0.29, rely=0.4059) # Positioning the display_customer_phone_number label to a designated x and y positions according to the size of the window.

    if topping_1_total_price >= 1: # Only execute the following action if pizza_1_total is above 1.
        topping_1_final = tk.Label(window, text="{} - ${}".format(topping_options[0], topping_1_total_price), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        topping_1_final.pack() # Putting the pizza_1 label onto the GUI platform.
        topping_1_final.place(relx=0.54, rely=0.20) # Positioning the pizza_1 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        topping_1_final = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if topping_2_total_price >= 1: # Only execute the following action if pizza_2_total is above 1.
        topping_2_final = tk.Label(window, text="{} - ${}".format(topping_options[1], topping_2_total_price), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        topping_2_final.pack() # Putting the pizza_2 label onto the GUI platform.
        topping_2_final.place(relx=0.775, rely=0.20) # Positioning the pizza_2 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        topping_2_final = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if topping_3_total_price >= 1: # Only execute the following action if pizza_3_total is above 1.
        topping_3_final = tk.Label(window, text="{} - ${}".format(topping_options[2], topping_3_total_price), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        topping_3_final.pack() # Putting the pizza_3 label onto the GUI platform.
        topping_3_final.place(relx=0.575, rely=0.25) # Positioning the pizza_3 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        topping_3_final = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if topping_4_total_price >= 1: # Only execute the following action if pizza_4_total is above 1.
        topping_4_final = tk.Label(window, text="{} - ${}".format(topping_options[3], topping_4_total_price), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        topping_4_final.pack() # Putting the pizza_4 label onto the GUI platform.
        topping_4_final.place(relx=0.775, rely=0.25) # Positioning the pizza_4 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        topping_4_final = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    topping_info_final = tk.Label(window, text=("Topping Notes - {}.".format(customer_topping_notes.get("1.0", END))), font=font_global) # Created a label informing the user of the topping notes.
    topping_info_final.pack() # Putting the topping_info_final label onto the GUI platform.
    topping_info_final.place(relx=0.6, rely=0.3725) # Positioning the topping_info_final label to a designated x and y positions according to the size of the window.

    if service_chosen == "Delivery": # Only execute the actions below if the user choose delivery as the selected delivery option.
        input_customer_address.place_forget() # Forget the object/Delete the object from the window.
        display_customer_address = tk.Label(window, text=input_customer_address.get("1.0", END), font=font_global, height = 2, width = 18) # Create label displaying the customers address.
        display_customer_address.pack() # Putting the display_customer_address label onto the GUI platform.
        display_customer_address.place(relx=0.28, rely=0.5) # Positioning the display_customer_address label to a designated x and y positions according to the size of the window.

    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        input_customer_pickup.place_forget() # Forget the object/Delete the object from the window.
        display_customer_pickup = tk.Label(window, font=font_global, height = 2, width = 18, text=input_customer_pickup.get("1.0", END)) # Create label displaying the customers pickup time.
        display_customer_pickup.pack() # Putting the display_customer_pickup label onto the GUI platform.
        display_customer_pickup.place(relx=0.28, rely=0.5) # Positioning the display_customer_pickup label to a designated x and y positions according to the size of the window.


    if pizza_1_total >= 1: # Only execute the following action if pizza_1_total is above 1.
        pizza_1 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 1"], pizza_1_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_1.pack() # Putting the pizza_1 label onto the GUI platform.
        pizza_1.place(relx=0.05, rely=0.6) # Positioning the pizza_1 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_1 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_2_total >= 1: # Only execute the following action if pizza_2_total is above 1.
        pizza_2 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 2"], pizza_2_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_2.pack() # Putting the pizza_2 label onto the GUI platform.
        pizza_2.place(relx=0.05, rely=0.7) # Positioning the pizza_2 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_2 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_3_total >= 1: # Only execute the following action if pizza_3_total is above 1.
        pizza_3 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 3"], pizza_3_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_3.pack() # Putting the pizza_3 label onto the GUI platform.
        pizza_3.place(relx=0.05, rely=0.8) # Positioning the pizza_3 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_3 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_4_total >= 1: # Only execute the following action if pizza_4_total is above 1.
        pizza_4 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 4"], pizza_4_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_4.pack() # Putting the pizza_4 label onto the GUI platform.
        pizza_4.place(relx=0.05, rely=0.9) # Positioning the pizza_4 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_4 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_5_total >= 1: # Only execute the following action if pizza_5_total is above 1.
        pizza_5 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 5"], pizza_5_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_5.pack() # Putting the pizza_5 label onto the GUI platform.
        pizza_5.place(relx=0.4, rely=0.6) # Positioning the pizza_5 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_5 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_6_total >= 1: # Only execute the following action if pizza_6_total is above 1.
        pizza_6 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 6"], pizza_6_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_6.pack() # Putting the pizza_6 label onto the GUI platform.
        pizza_6.place(relx=0.4, rely=0.7) # Positioning the pizza_6 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_6 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_7_total >= 1: # Only execute the following action if pizza_7_total is above 1.
        pizza_7 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 7"], pizza_7_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_7.pack() # Putting the pizza_7 label onto the GUI platform.
        pizza_7.place(relx=0.4, rely=0.8) # Positioning the pizza_7 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_7 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_8_total >= 1: # Only execute the following action if pizza_8_total is above 1.
        pizza_8 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 8"], pizza_8_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_8.pack() # Putting the pizza_8 label onto the GUI platform.
        pizza_8.place(relx=0.4, rely=0.9) # Positioning the pizza_8 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_8 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_9_total >= 1: # Only execute the following action if pizza_9_total is above 1.
        pizza_9 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 9"], pizza_9_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_9.pack() # Putting the pizza_9 label onto the GUI platform.
        pizza_9.place(relx=0.8, rely=0.6) # Positioning the pizza_9 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_9 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_10_total >= 1: # Only execute the following action if pizza_10_total is above 1.
        pizza_10 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 10"], pizza_10_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_10.pack() # Putting the pizza_10 label onto the GUI platform.
        pizza_10.place(relx=0.8, rely=0.7) # Positioning the pizza_10 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_10 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_11_total >= 1: # Only execute the following action if pizza_11_total is above 1.
        pizza_11 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 11"], pizza_11_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_11.pack() # Putting the pizza_11 label onto the GUI platform.
        pizza_11.place(relx=0.8, rely=0.8) # Positioning the pizza_11 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_11 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    if pizza_12_total >= 1: # Only execute the following action if pizza_12_total is above 1.
        pizza_12 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 12"], pizza_12_total), font=font_global_15) # Create a label showing the pizza option selected and the total for the pizza option.
        pizza_12.pack() # Putting the pizza_12 label onto the GUI platform.
        pizza_12.place(relx=0.8, rely=0.9) # Positioning the pizza_12 label to a designated x and y positions according to the size of the window.
    else: # If the user does not meet the requirement/condition for the if statement above, the action below is executed.
        pizza_12 = tk.Label(window, text="") # Leave a gap in the GUI programe as there are no pizzas being ordered for this type.

    payment_button_1 = tk.Button(window, text =("Cash Payment"), bg=button_background, fg=button_text, font=font_global, width=20, command=cash_payment) # Created a label directing the user to the cash_payment function.
    payment_button_1.pack() # Putting the payment_button_1 button onto the GUI platform.
    payment_button_1.place(relx=.4, rely=.95) # Positioning the payment_button_1 button to a designated x and y positions according to the size of the window.
    
    payment_button_2 = tk.Button(window, text =("Card Payment"), bg=button_background, fg=button_text, font=font_global, width=20, command=card_payment) # Created a label directing the user to the card_payment function.
    payment_button_2.pack() # Putting the payment_button_2 button onto the GUI platform.
    payment_button_2.place(relx=.6, rely=.95) # Positioning the payment_button_2 button to a designated x and y positions according to the size of the window.

    payment_button_3 = tk.Button(window, text =("Other Payment"), bg=button_background, fg=button_text, font=font_global, width=20, command=other_payment) # Created a button directing the user to the other_payment function.
    payment_button_3.pack() # Putting the payment_button_3 button onto the GUI platform.
    payment_button_3.place(relx=.8, rely=.95) # Positioning the payment_button_3 button to a designated x and y positions according to the size of the window.

    window.mainloop() # Running the window loop.

def other_payment(): # Defining the funtion of other_payment when called.
    global other_payment_input # Making the other_payment_input variable global to apply to all functions in this script.
    global confirmation_request # Making the confirmation_request variable global to apply to all functions in this script.
    global payment_chosen # Making the payment  variable global to apply to all functions in this script.

    payment_button_1.place_forget() # Forget the object/Delete the object from the window. # Forgetting payment_button_1.
    payment_button_2.place_forget() # Forget the object/Delete the object from the window. # Forgetting payment_button_2.
    payment_button_3.place_forget() # Forget the object/Delete the object from the window. # Forgetting payment_button_3.

    other_payment_input = tk.Text(window, font=font_global, height = 1, width = 26) # Create input box allowing the user to provide an input.
    other_payment_input.pack() # Putting the other_payment_input input box onto the GUI platform.
    other_payment_input.place(relx=.5, rely=.95) # Positioning the other_payment_input input box to a designated x and y positions according to the size of the window.

    payment_chosen = "Other" # Set the payment_chosen to other.
    confirmation_request = tk.Button(window, text =("Next Payment"), bg=button_background, fg=button_text, font=font_global, width=20, command=payment_selected_def) # Create button to identify if the uses needs the command set.
    confirmation_request.pack() # Putting the confirmation_request label onto the GUI platform.
    confirmation_request.place(relx=.8, rely=.95) # Positioning the confirmation_request label to a designated x and y positions according to the size of the window.

def cash_payment(): # Defining the funtion of restart when called.
    global payment_chosen # Making the payment_option variable global to apply to all functions in this script.

    payment_button_1.place_forget() # Forget the object/Delete the object from the window. # Forgetting payment_button_1.
    payment_button_2.place_forget() # Forget the object/Delete the object from the window. # Forgetting payment_button_2.
    payment_button_3.place_forget() # Forget the object/Delete the object from the window. # Forgetting payment_button_3.

    from tkinter import messagebox # Importing a message box from tkrinter for the message below.
    tk.messagebox.showinfo ('Confirm Payment Option', 'Please confirm this user will pay by {}.'.format(payment_options["Cash"])) # Informing the operator that they have selected the relevant payment option.

    payment_chosen = "Cash" # Set the users payment_chosen as Cash.

    payment_selected_def() # Call the payment_selcted_def function.

def card_payment(): # Defining the funtion of restart when called.
    global payment_chosen # Making payment_chosen global.

    payment_button_1.place_forget() # Forget the object/Delete the object from the window. # Forgetting payment_button_1.
    payment_button_2.place_forget() # Forget the object/Delete the object from the window. # Forgetting payment_button_2.
    payment_button_3.place_forget() # Forget the object/Delete the object from the window. # Forgetting payment_button_3.

    from tkinter import messagebox # Importing a message box from tkrinter for the message below.
    tk.messagebox.showinfo ('Confirm Payment Option', 'Please confirm this user will pay by {}.'.format(payment_options["Card"])) # Informing the operator that they have selected the relevant payment option.

    payment_chosen = "Card" # Set the users payment_chosen as Card.

    payment_selected_def() # Call the payment_selcted_def function.

def payment_selected_def(): # Defining the funtion of payment_selected_def when called.
    global payment_selected # Making the payment_selected variable global to apply to all functions in this script.
    
    if payment_chosen == "Cash": # If the user selected cash as their payment option, the actions below are executed.
        payment_selected = payment_options["Cash"] # Set payment_selected as Cash.

    if payment_chosen == "Card": # If the user selected card as their payment option, the actions below are executed.
        payment_selected = payment_options["Card"] # Set payment_selected as Card.

    if payment_chosen =="Other": # If the user selected other as their payment option, the actions below are executed.
        other_payment_input.place_forget() # Forget the object/Delete the object from the window.
        payment_options["Other"] = other_payment_input.get("1.0", END) # Collect the input from the user input as the explaination for the other payment option.
        payment_selected =  payment_options["Other"] # Set payment_selected as Other.

    confirmation() # Call the confirmation function.

def confirmation(): # Defining the funtion of confirmation when called.
    global payment_selected # Making the payment_selected variable global to apply to all functions in this script.

    window.title("Henderson Pizza Palace | Order Confirmation") # Changing the title of the window pop-up accordng to the function.
    
    ordertotal_display.place(relx=0.3, rely=0.05) # Positioning the ordertotal_display variable to a designated x and y positions according to the size of the window.

    payment_option_display = tk.Label(window, text="""Payment Confirmed, Payment By 
    {}""".format(payment_selected), background="light green", font=font_global_15) # Creating a label informing the user that their order has been confirmed.
    payment_option_display.pack() # Displaying the label above into the GUI platform.
    payment_option_display.place(relx=0.6, rely=0.05) # Positioning the payment_option_display variable to a designated x and y positions according to the size of the window.
    
    restart_python = tk.Button(window, text =("Restart Program"), bg=button_background, fg=button_text, font=font_global, width=20, command=restart) # Creating a button allowing the user to click restart on the programe.
    restart_python.pack() # Displaying the button above into the GUI platform.
    restart_python.place(relx=.8, rely=.95) # Positioning the restart_python button to a designated x and y positions according to the size of the window.

    payment_option_display.after(30000, restart) # After displaying payment_option_display label for 30 seconds, execute the restart function.
    window.mainloop()

def dtime(): # Defining the funtion of dtime when called.
    e = datetime.datetime.now() # Setting the vaiable named e as the current date and time.
    info.config(text = "%s/%s/%s" % (e.day, e.month, e.year)+ "\n"+ strftime('%H:%M:%S %p')) # Configuring the info label to the set time and date.
    info.after(1, dtime) # After 1 second, complete this cycle function again.

def restart(): # Defining the funtion of restart when called.
    window.destroy() # Asking the python window to be destroyed.
    os.system("python henderson_pizza_palace.py") # Asking the operating system (os) to reopen the henderson_pizza_palace python script on the computer.
    sys.exit() # Asking the python system to exit this python programe.
    
def leave(): # Defining the funtion of leave when called.
    from tkinter import messagebox # Importing a message box from tkrinter for the message below.
    leave_box = tk.messagebox.askquestion ('Quit Program', 'Are you sure you want to quit the application?', icon = 'warning') # Asking the user if they want to leave the programe and return # Return to the mainscript/current function called. to the JP_Software home page.
    if leave_box == 'yes': # If the user selects yes, it redirects the programe to the actions below.
        window.destroy() # Asking the python window to be destroyed.
        os.system("python jp_software.py") # Asking the operating system (os) to open the JP_Software python script on the computer.
        sys.exit() # Asking the python system to exit this python programe.

def system_logout(): # Defining the funtion of system logout when called.
    from tkinter import messagebox # Importing a message box from tkrinter for the message below.
    logout_box = tk.messagebox.askquestion ('System Log Off', 'Are you sure you want to log out of the computer?', icon = 'warning') # Asking the user if they are sure about logging out of the computer.
    if logout_box == 'yes': # If the user selects yes, it redirects the programe to the actions below.
        os.system("shutdown -l") # Asking the operating system (os) to logout the computer.
    
def system_restart(): # Defining the funtion of system restart when called.
    from tkinter import messagebox # Importing a message box from tkrinter for the message below.
    restart_box = tk.messagebox.askquestion ('System Restart', 'Are you sure you want to restart the computer?', icon = 'warning') # Asking the user if they are sure about restarting the computer.
    if restart_box == 'yes': # If the user selects yes, it redirects the programe to the actions below.
        os.system("shutdown /r /t 0") # Asking the operating system (os) to restart the computer.
    
def system_shutdown(): # Defining the funtion of system shutdown when called.
    from tkinter import messagebox # Importing a message box from tkrinter for the message below.
    shutdown_box = tk.messagebox.askquestion ('System Shutdown', 'Are you sure you want to shutdown the application and the computer?', icon = 'warning') # Asking the user if they are sure about shutting down the computer.
    if shutdown_box == 'yes': # If the user selects yes, it redirects the programe to the actions below.
        os.system("shutdown /s /t 0") # Asking the operating system (os) to shutdown the computer.

# Window Function------------------------------------------------------------------------------------------------------------------------------------------------------
window=tk.Tk() # Creating the window to open to use as a GUI platform.
window.geometry('1000x700') # Setting the window pop-up size to the set amount stated.
window.title("Henderson Pizza Palace Menu") # Setting the title of the window pop-up.
window.iconphoto(False, tk.PhotoImage(file="images/henderson_pizza_palace_logo.png")) # Setting the icon photo of the window pop-up.

# Date and Time Function-----------------------------------------------------------------------------------------------------------------------------------------------------------
global info # Making the info varable global to use in all functions in this script.
info = tk.Label(window, text="""""", font=font_global, height =2, border=0 ) # Creating a label for the space of time and date.
info.pack() # Putting the info label onto the GUI platform.
info.place(relx=0.05, rely=0.001) # Positioning the info label to a designated x and y positions according to the size of the window.

#  JP Software Menu/ Home Page----------------------------------------------------------------------------------------------------------------------------------------------------------              
openevening_logo = tk.PhotoImage(file="images/open_evening/hhs-logo.png") # Logo image for the open evening programe.
pizzapalace_logo = tk.PhotoImage(file="images/henderson_pizza_palace_logo.png") # Logo image for the pizza palace programe.
jp_software_logo_img = tk.PhotoImage(file="images/jp_software-icon-2.png") # Logo for the JP_Software programe.
jp_software_control = tk.Menubutton(window, image=jp_software_logo_img , height =35, width=45, border=0) # Menu Button created for the menu.
jp_software_control.menu = Menu(jp_software_control) # Menu button defined for tkrinter pruposes.
jp_software_control["menu"]= jp_software_control.menu  # Menu again defined for ["Menu"].
jp_software_control.menu.add_command(label = "", image=openevening_logo, command=open_evening) # Command added to open the open evening script in the menu bar.
jp_software_control.menu.add_command(label = "", image=pizzapalace_logo, command=pizza_palace) # Command added to open the pizza_palace script in the menu bar.
jp_software_control.menu.add_command(label = "Leave Application", command=leave) # Command added to leave the script in the menu bar.
jp_software_control.menu.add_command(label = "Restart Application", command=restart) # Command added to restart the script in the menu bar.
jp_software_control.menu.add_command(label = "Shut Down PC", command=system_shutdown) # Command added ot shut down the computer in the menu bar.
jp_software_control.menu.add_command(label = "Restart PC", command=system_restart) # Command added to restart the computer in the menu bar.
jp_software_control.menu.add_command(label = "Log Off PC", command=system_logout) # Command added to log out of the computer in the menu bar
jp_software_control.pack() # Putting the menu button onto the GUI platform.
jp_software_control.place(relx=0.0, rely=0.003) # This is for placing the menu bar on the GUI programe.

login() # Directing the script to login def.
window.mainloop() # Running the window loop. # Running the window loop.

