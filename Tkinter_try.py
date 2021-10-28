from tkinter import *

def saveInfo():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    age_info = str(age_info)
    print(firstname_info, lastname_info, age_info)

    file = open("user.txt", "a+")
    file.write('First Name: ' + firstname_info + '\n')
    file.write('Last Name: ' + lastname_info + '\n')
    file.write('Age: ' + age_info + '\n')
    print("User ", firstname_info, "has been registered successfully!")

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    age_entry.delete(0, END)

screen = Tk()
screen.title("Registration Form")
screen.geometry("500x500")
heading = Label(text = "Registration Form", fg="black", bg="grey", height = '3', width = '500')
heading.pack()
firstname_text = Label(text = "First Name")
lastname_text = Label(text = "Last Name")
age_text = Label(text = "Age")
firstname_text.place(x = 15, y = 70)
lastname_text.place(x = 15, y = 140)
age_text.place(x = 15, y = 210)

firstname = StringVar()
lastname = StringVar()
age = IntVar()
firstname_entry = Entry(textvariable = firstname, width = "30")
lastname_entry = Entry(textvariable = lastname, width = "30")
age_entry = Entry(textvariable = age, width = "30")
firstname_entry.place(x = 15, y = 100)
lastname_entry.place(x = 15, y = 180)
age_entry.place(x = 15, y = 240)
register = Button(screen, text = "Register", height = '2', width = '30', command = saveInfo, bg="grey")
register.place(x = 15, y = 290)

screen.mainloop()
