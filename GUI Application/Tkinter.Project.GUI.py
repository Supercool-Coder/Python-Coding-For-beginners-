# tee-kinter , Tk-inter , kinter

# Starter code
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
window = tk.Tk()
window.title('GUI Application')

# Create labels
name_label = ttk.Label(window, text='Enter the name :- ')
name_label.grid(row=0 , column=0 , sticky =tk.W)

age_label = ttk.Label(window, text='Age :- ')
age_label.grid(row=1,column=0,sticky=tk.W)

email_label = ttk.Label(window, text='Enter your email id:- ')
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label = ttk.Label(window, text='Select your gender:- ')
gender_label.grid(row=3,column=0,sticky=tk.W)

# Creating entry box for each label
name_variable = tk.StringVar()
name_entrybox = ttk.Entry(window,width=16,textvariable=name_variable)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

age_variable = tk.StringVar()
age_entrybox = ttk.Entry(window,width=16,textvariable=age_variable)
age_entrybox.grid(row=1,column=1)

email_variable = tk.StringVar()
email_entrybox = ttk.Entry(window,width=16,textvariable=email_variable)
email_entrybox.grid(row=2,column=1)

# gender_variable = tk.StringVar()
# gender_entrybox = ttk.Entry(window,width=16,textvariable=gender_variable)
# gender_entrybox.grid(row=3,column=1)

# Create combobox
gender_variable = tk.StringVar()
gender_combobox = ttk.Combobox(window, width=14, textvariable=gender_variable, state='readonly')
gender_combobox['values'] = ('Male','Female','Transgender like Dinesh')
gender_combobox.current(0)
gender_combobox.grid(row=3 , column=1)

# Creating radio button
usertype = tk.StringVar()
radio_button1 = ttk.Radiobutton(window, text='Student' , value='Student' , variable=usertype)
radio_button1.grid(row=4,column=0)

radio_button2 = ttk.Radiobutton(window, text='Teacher' , value='Teacher' , variable=usertype)
radio_button2.grid(row=4,column=1)

# Create check button

checkbutton = tk.IntVar()
check_button = ttk.Checkbutton(window,text='Check if you want to subscribe our channel',variable=checkbutton)
check_button.grid(row=5,columnspan=3)

# Create Button

# If we wanna write csv files
def action():
    username = name_variable.get()
    userage = age_variable.get()
    user_email = email_variable.get()
    user_gender = gender_variable.get()
    user_type = usertype.get()
    if checkbutton.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'

    with open('file.csv','a') as f:
        dict_writer = DictWriter(f,fieldnames=['UserName','User Email Address','User Age','User Gender','User Type','Suscribed'])

        if os.stat('file.csv').st_size==0:
           dict_writer.writeheader()

        dict_writer.writerow({
            'UserName' : username,
            'User Email Address' : user_email,
            'User Age' : userage,
            'User Gender' : user_gender,
            'User Type' : user_type,
            'Suscribed' : subscribed
        })

    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)

    name_label.configure(foreground='#b388ff')




submit_button = tk.Button(window,text='Submit' , command=action)
submit_button.grid(row=6,column=0)





'''Aagar hum mainloop() nhi likhenge toh hamara window turant chalu ho k bnd ho jayega iss liye hum mainloop k use kr
 rahe hai ki hamara window user bnd kre tb hi bnd ho......'''

window.mainloop()