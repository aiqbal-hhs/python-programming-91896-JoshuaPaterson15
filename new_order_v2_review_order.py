import tkinter as tk
from tkinter import Entry, Label, Menu, StringVar
global time
import time
import datetime
from time import strftime
global window
global menu
global button_background
global button_text
global credential
global count
global pizza_options
import os
import sys
 
#Dictonaries-----------------------------------------------------------
credential = {'HHS':{'password':'2021',},'ADMIN':{'password':'2021',},'Tech':{'password':'2021',},'':{'password':'',}}
pizza_options = {"Pizza 1":'Australlia', "Pizza 2":'France', "Pizza 3":'Korea', "Pizza 4":'India', "Pizza 5":'Fiji', "Pizza 6":'Germany', "Pizza 7":'Wellington', "Pizza 8":'Southern Italy', "Pizza 9":'New York', "Pizza 10":'London', "Pizza 11":'Rome', "Pizza 12":'Chicago', }
#Fonts------------------------------------------------------------------------------------------------------------------------------------------------------------
global font_global
global font_global_15
global font_global_20
font_global = ("Comic Sans MS", 10, "bold")
font_global_15 = ("Comic Sans MS", 15, "bold")
font_global_20 = ("Comic Sans MS", 20, "bold")
font_global_15_underlined = ("Comic Sans MS",15,"underline")
button_background = ('green')
button_text = ('white')

#Define Functions----------------------------------------------------------------------------------------------------------------------------------------------------
def pizza_palace():
    window.destroy()
    os.system("python joshua_paterson_as91896_henderson_pizza_palace.py")
    sys.exit()

def open_evening():
    window.destroy()
    os.system("python open_evening_script.py")
    sys.exit()
    
def login():
    from tkinter import messagebox
    tk.messagebox.showinfo('Login/HomePage','You have made it to the Login/HomePage!')    

def service_needed():
    global user_option_1
    global user_option_2
    global services_display
    services_display = tk.Label(window,font=font_global,text="Is this order for pick-up or delivery?")
    user_option_1 = tk.Button(window, text =("Pick-Up"),bg=button_background, fg=button_text, font=font_global, width=20, command=pick_up)
    user_option_2 = tk.Button(window, text =("Delivery"),bg=button_background, fg=button_text, font=font_global, width=20, command=delivery)
    services_display.pack()
    user_option_1.pack()
    user_option_2.pack()
    services_display.place(relx=0.4,rely=0.6)
    user_option_1.place(relx=0.30,rely=0.7)
    user_option_2.place(relx=0.55,rely=0.7)

def pick_up():
    global service_chosen

    from tkinter import messagebox
    user_selection = tk.messagebox.askquestion ('Pick-Up Confirmation','Please confirm this order is for Pick Up at Henderson High School?',icon = 'warning')
    if user_selection == 'yes':
        service_chosen = 'Pick-Up'
        services_display.place_forget()
        new_order()
    else:
        return

def delivery():
    global service_chosen
    global order_total

    order_total = 0
    
    from tkinter import messagebox
    user_selection = tk.messagebox.askquestion ('Delivery Confirmation','Please confirm this order is for delivery for an extra $3?',icon = 'warning')
    if user_selection == 'yes':
        service_chosen = 'Delivery'
        new_order()
    else:
        return

def new_order():
        window.title("Hederson Pizza Palace | New Order")
        global regular_price
        global gourmet_price
        global pizza_1_var
        global pizza_2_var
        global pizza_3_var
        global pizza_4_var
        global pizza_5_var
        global pizza_6_var
        global pizza_7_var
        global pizza_8_var
        global pizza_9_var
        global pizza_10_var
        global pizza_11_var
        global pizza_12_var
        global pizza_1_option
        global pizza_2_option
        global pizza_3_option
        global pizza_4_option
        global pizza_5_option
        global pizza_6_option
        global pizza_7_option
        global pizza_8_option
        global pizza_9_option
        global pizza_10_option
        global pizza_11_option
        global pizza_12_option

        pizza_1_var = StringVar()
        pizza_2_var = StringVar()
        pizza_3_var = StringVar()
        pizza_4_var = StringVar()
        pizza_5_var = StringVar()
        pizza_6_var = StringVar()
        pizza_7_var = StringVar()
        pizza_8_var = StringVar()
        pizza_9_var = StringVar()
        pizza_10_var = StringVar()
        pizza_11_var = StringVar()
        pizza_12_var = StringVar()

        pizza_count = 0
        regular_price = 8.5
        gourmet_price = 13.5

        services_display.place_forget()
        user_option_1.place_forget()
        user_option_2.place_forget()

        pizza_1 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 1"], regular_price), font=font_global_15_underlined)
        pizza_1.pack()
        pizza_1.place(relx=0.1,rely=0.1)

        pizza_2 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 2"], regular_price), font=font_global_15_underlined)
        pizza_2.pack()
        pizza_2.place(relx=0.1,rely=0.2)

        pizza_3 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 3"], regular_price), font=font_global_15_underlined)
        pizza_3.pack()
        pizza_3.place(relx=0.1,rely=0.3)

        pizza_4 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 4"], regular_price), font=font_global_15_underlined)
        pizza_4.pack()
        pizza_4.place(relx=0.1,rely=0.4)

        pizza_5 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 5"], regular_price), font=font_global_15_underlined)
        pizza_5.pack()
        pizza_5.place(relx=0.1,rely=0.5)

        pizza_6 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 6"], regular_price), font=font_global_15_underlined)
        pizza_6.pack()
        pizza_6.place(relx=0.1,rely=0.6)

        pizza_7 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 7"], gourmet_price), font=font_global_15_underlined)
        pizza_7.pack()
        pizza_7.place(relx=0.6,rely=0.1)

        pizza_8 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 8"],gourmet_price), font=font_global_15_underlined)
        pizza_8.pack()
        pizza_8.place(relx=0.6,rely=0.2)

        pizza_9 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 9"],gourmet_price), font=font_global_15_underlined)
        pizza_9.pack()
        pizza_9.place(relx=0.6,rely=0.3)

        pizza_10 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 10"],gourmet_price), font=font_global_15_underlined)
        pizza_10.pack()
        pizza_10.place(relx=0.6,rely=0.4)

        pizza_11 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 11"],gourmet_price), font=font_global_15_underlined)
        pizza_11.pack()
        pizza_11.place(relx=0.6,rely=0.5)

        pizza_12 = tk.Label(window, text="{} - ${}".format(pizza_options["Pizza 12"],gourmet_price), font=font_global_15_underlined)
        pizza_12.pack()
        pizza_12.place(relx=0.6,rely=0.6)

        b1 = tk.Button(window, text =("Review Order"),bg=button_background, fg=button_text, font=font_global, width=20, command=review_order)
        b1.pack()
        b1.place(relx=.800, rely=.95)
        b2 = tk.Button(window, text =("Login/HomePage"),bg=button_background, fg=button_text, font=font_global, width=20, command=login)
        b2.pack()
        b2.place(relx=.02, rely=.95)

        pizza_1_option = Entry(window,font=font_global,width = 10, textvariable = pizza_1_var).pack()

        pizza_2_option = Entry(window,font=font_global,width = 10, textvariable = pizza_2_var).pack()
     

        pizza_3_option = Entry(window,font=font_global,width = 10, textvariable = pizza_3_var).pack()
 

        pizza_4_option = Entry(window,font=font_global,width = 10, textvariable = pizza_4_var).pack()
 

        pizza_5_option = Entry(window,font=font_global,width = 10, textvariable = pizza_5_var).pack()


        pizza_6_option = Entry(window,font=font_global,width = 10, textvariable = pizza_6_var).pack()


        pizza_7_option = Entry(window,font=font_global,width = 10, textvariable = pizza_7_var).pack()
    

        pizza_8_option = Entry(window,font=font_global,width = 10, textvariable = pizza_8_var).pack()


        pizza_9_option = Entry(window,font=font_global,width = 10, textvariable = pizza_9_var).pack()


        pizza_10_option = Entry(window,font=font_global,width = 10, textvariable = pizza_10_var).pack()


        pizza_11_option = Entry(window,font=font_global,width = 10, textvariable = pizza_11_var).pack()


        pizza_12_option = Entry(window,font=font_global,width = 10, textvariable = pizza_12_var).pack()
   

        window.mainloop()

def review_order():
    from tkinter import messagebox
    tk.messagebox.showinfo('Review Order','You have made it to the Review Order Page!')   

def dtime():
    e = datetime.datetime.now()
    info.config(text = "%s/%s/%s" % (e.day, e.month, e.year)+ "\n"+ strftime('%H:%M:%S %p'))
    info.after(1, dtime)
    
def restart():
    window.destroy()
    os.system("python template.py")
    sys.exit()
    
def leave():
        from tkinter import messagebox
        leave_box = tk.messagebox.askquestion ('Quit Program','Are you sure you want to quit the application?',icon = 'warning')
        if leave_box == 'yes':
            window.destroy()
            os.system("python jp_software.py")
            sys.exit()
        else:
                tk.messagebox.showinfo('Return','Returning back to the application.')    

def system_logout():
        from tkinter import messagebox
        leave_box = tk.messagebox.askquestion ('System Log Off','Are you sure you want to log out of the computer?',icon = 'warning')
        if leave_box == 'yes':
                os.system("shutdown -l")
    
def system_restart():
        from tkinter import messagebox
        leave_box = tk.messagebox.askquestion ('System Restart','Are you sure you want to restart the computer?',icon = 'warning')
        if leave_box == 'yes':
                os.system("shutdown /r /t 0")
    
def system_shutdown():
        from tkinter import messagebox
        leave_box = tk.messagebox.askquestion ('System Shutdown','Are you sure you want to shutdown the application and the computer?',icon = 'warning')
        if leave_box == 'yes':
                os.system("shutdown /s /t 0")

#Window Function------------------------------------------------------------------------------------------------------------------------------------------------------
window=tk.Tk()
window.geometry('1000x700')
window.title("Henderson Pizza Palace Menu")
window.iconphoto(False, tk.PhotoImage(file="images/henderson_pizza_palace_logo.png"))

global info
info = tk.Label(window, text="""""", font=font_global,height =2,border=0 )
info.pack()
info.place(relx=0.05,rely=0.001)
dtime()

# JP Software Menu----------------------------------------------------------------------------------------------------------------------------------------------------------              
openevening_logo = tk.PhotoImage(file="images/open_evening/hhs-logo.png")
pizzapalace_logo = tk.PhotoImage(file="images/henderson_pizza_palace_logo.png")
jp_software_logo_img = tk.PhotoImage(file="images/jp_software-icon-2.png")
jp_software_control = tk.Menubutton(window, image=jp_software_logo_img ,height =35, width=45, border=0)      
jp_software_control.menu = Menu(jp_software_control)  
jp_software_control["menu"]= jp_software_control.menu  
jp_software_control.menu.add_command(label = "", image=openevening_logo, command=open_evening)
jp_software_control.menu.add_command(label = "", image=pizzapalace_logo, command=pizza_palace)
jp_software_control.menu.add_command(label = "Leave Application", command=leave)
jp_software_control.menu.add_command(label = "Restart Application", command=restart)
jp_software_control.menu.add_command(label = "Shut Down PC",command=system_shutdown)
jp_software_control.menu.add_command(label = "Restart PC",command=system_restart)
jp_software_control.menu.add_command(label = "Log Off PC",command=system_logout)
jp_software_control.pack() 
jp_software_control.place(relx=0.0,rely=0.003)
service_needed()
window.mainloop()
