# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 10:20:43 2021

@author: diren
"""

from tkinter import*

from tkcalendar import DateEntry 

#go to cmd and install  'pip install tkcalendar' 

master = Tk() # when we define an interface it works like a parent object
master.title("Diren")

canvas = Canvas(master, height=450, width=850)# under master identifid the scales
canvas.pack() #pack, place ve grid commands provide to object on a frame. Grid contains a column and row

frame_top = Frame(master,bg='#add8e6')
frame_top.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1) # relx ve rely working like padding


frame_bottom_left = Frame(master,bg='#add8e6')
frame_bottom_left.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5) 

frame_bottom_right = Frame(master,bg='#add8e6')
frame_bottom_right.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

reminder_label = Label(frame_top,bg='#add8e6', text="Reminder Type:", font="Verdana 12 bold" )# we define style here
reminder_label.pack(padx=10, pady=10, side=LEFT)

reminder_option = StringVar(frame_top)
reminder_option.set("\t") #default value

reminder_option_open = OptionMenu(frame_top, reminder_option, "Birthday", "Shopping", "Paying") 
reminder_option_open.pack(padx=10, pady=10, side=LEFT)

reminder_date_choosing = DateEntry(frame_top, width=12, background = 'orange', foreground='black', boderwidth=1, locale="de_DE")
reminder_date_choosing._top_cal.overrideredirect(False) #DateEntry does not work pack directly. This formula makes it to work
reminder_date_choosing.pack(padx=10, pady=10, side=RIGHT)


reminder_date_label = Label(frame_top,bg='#add8e6', text="Reminder date:", font="Verdana 12 bold" )
reminder_date_label.pack(padx=10, pady=10, side=RIGHT)

#Part2

Label(frame_bottom_left, text="Reminder Options", font="Verdana 10 bold").pack(padx=10, pady=10, anchor=NW) #without defining a variable atamadan, label work like that
var = IntVar()

R1 = Radiobutton(frame_bottom_left, text="Save", variable = var, value = 1,bg='#add8e6', font="Verdana 10 bold")
R1.pack(anchor=NW, pady=5, padx=15)

R2 = Radiobutton(frame_bottom_left, text="Send an email", variable = var, value = 2,bg='#add8e6', font="Verdana 10 bold")
R2.pack(anchor=NW, pady=5, padx=15)

var1 = IntVar()
C1 = Checkbutton(frame_bottom_left, text="One week before", variable=var1, onvalue=1 , offvalue=0,bg='#add8e6', font="Verdana 10 bold")
C1.pack(anchor=NW, pady=5, padx=25)

var2 = IntVar()
C2 = Checkbutton(frame_bottom_left, text="One day before", variable=var2, onvalue=2 , offvalue=0,bg='#add8e6', font="Verdana 10 bold")
C2.pack(anchor=NW, pady=5, padx=25)

var3 = IntVar()
C3 = Checkbutton(frame_bottom_left, text="Today", variable=var3, onvalue=3 , offvalue=0,bg='#add8e6', font="Verdana 10 bold")
C3.pack(anchor=NW, pady=5, padx=25)

#part3
from tkinter import messagebox

def submit():
    last_message = ""
    try:
        if var.get():
            if var.get() == 1:
                last_message += "Data saved successfully"
                kind = reminder_option.get() if hatirlatma_tipi_opsiyon.get() == '' else "Genel"
                date = reminder_date_choosing
                message = text_area.get("1.0", "end")
                
                with open("reminders.txt", "w") as file:
                    file.write(
                        '{} in category','{} at date and "{}" with that note'.format(
                            kind,
                            date,
                            message
                            ))
                    file.close()
                    
            elif var.get() == 2:
                last_message += "Reminder will reach you through email"
                messagebox.showinfo("Successful ",last_message)
        else:
            last_message += "Fill all the gaps, please"
            messagebox.showwarning("Invalid Information", last_message)
        return
    except:
         last_message += "Operation failed"
         messagebox.showerror("Unsuccessful Operation", last_message)
    finally:
        master.destroy()

Label(frame_bottom_right, text="Reminder message", font="Verdana 10 bold").pack(padx=10, pady=10, anchor=NW)


text_area = Text(frame_bottom_right, height = 9, width = 50)
text_area.tag_configure('styele', foreground= '#bfbfbf', font=('Verdana',7, 'bold'))
text_area.pack()

first_text = 'Write your message here...'
text_area.insert(END,first_text, ' style')

submit_buton = Button(frame_bottom_right, text="Submit", command=submit)

submit_buton.pack(anchor=S)



master.mainloop()
