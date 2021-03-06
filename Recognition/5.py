from Tkinter import *
import tkMessageBox
import tkFont
import pyttsx
import PyMongo
import cv2

global engine
global PyMongo

global gender
global city
global purpose

global t1
global t3
global t6

global cv2

main = Tk() # creates root window
# all components of thw window will come here

main.title(" Naagarik Seva ")
root = Frame(main)
width=600
height=400
#background_image=Tk.PhotoImage(file="C:\Python27\imgres.jpg")
#background_label = Tk.Label(root, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
engine = pyttsx.init('sapi5');
engine.say("Namaskaar !")
cv2.waitKey(2);
engine.say("Welcome,  Please Fill your details! ");
engine.runAndWait()

label_head=Label(root,text="Collector Office,Sangli.",font=("Lucida Fax",23),fg="cyan",bg="black");
f = tkFont.Font(label_head, label_head.cget("font"))
f.configure(underline = True)
label_head.grid(row=1,column=2)
#label_head.configure(font=f)
#label_head.pack()

l= Label(root,text="                                                         ")
l1 = Label(root,text="Name: ")
l2 = Label(root,text="Purpose: ")
l3 = Label(root,text="Age: ")
l4 = Label(root,text="Gender: ")
l5 = Label(root,text="City: ")
l6 = Label(root,text="Mobile: ")

d1= Label(root,text=" ----------------------------------------------------------")
d2= Label(root,text=" ----------------------------------------------------------")
d3= Label(root,text=" ----------------------------------------------------------")
d4= Label(root,text=" ----------------------------------------------------------")
d5= Label(root,text=" ----------------------------------------------------------")
d6= Label(root,text=" ----------------------------------------------------------")



#dropdown for gender
gender=StringVar(main)
choices={'Male','Female','Other'}
gender.set('Male')
popupmenu = OptionMenu(root,gender,*choices)


#dropdown for city
city=StringVar(main)
choices1={'Sangli','Miraj','Pune','Mumbai'}
city.set('Sangli')
popupmenu1 = OptionMenu(root,city,*choices1)

#dropdown for Purpose
purpose=StringVar(main)
choices2={'Personal','Meeting','Urgent','Invitation','Other'}
purpose.set('Meeting')
popupmenu2 =OptionMenu(root,purpose,*choices2)


t1=Entry(root)
#global t2=Entry(root)
t3=Entry(root)
#global t5=Entry(root)
t6 = Entry(root)

l.grid(row=2,column=1)
l1.grid(row=4,column=1)
t1.grid(row=4,column=3)
d1.grid(row=4,column=2)

l2.grid(row=5,column=1)
popupmenu2.grid(row=5,column=3)
d2.grid(row=5,column=2)

l3.grid(row=6,column=1)
t3.grid(row=6,column=3)
d3.grid(row=6,column=2)

l4.grid(row=7,column=1)
popupmenu.grid(row=7,column=3)
d4.grid(row=7,column=2)

l5.grid(row=8,column=1)
popupmenu1.grid(row=8,column=3)
d5.grid(row=8,column=2)

l6.grid(row=9,column=1)
t6.grid(row=9,column=3)
d6.grid(row=9,column=2)

def gen_dropdown(*args):
    tgender=gender.get()

def city_dropdown(*args):
    tcity=city.get()

def purpose_dropdown(*args):
	tpurpose=purpose.get()
    
def page():
    Name=t1.get()
    Purpose=purpose.get()
    Age=t3.get()
    Gender=gender.get()
    City=city.get()
    Mobile = t6.get()
    
    PyMongo.insertNew(Name,Gender,City,Age,Purpose,Mobile);
    engine.say("Thank you for response")
    cv2.waitKey(2)
    
    execfile("dataSetCreator.py")


    
gender.trace('w',gen_dropdown)
city.trace('w',city_dropdown)
purpose.trace('w',purpose_dropdown)

#button click event
b = Button(root,text="Continue",fg="red",bg="grey",command=page)

screen_w =root.winfo_screenwidth()
screen_h =root.winfo_screenheight()

b.grid(row=10,column=2)
x = (screen_w/2)-(width/2)
y = (screen_h/2)-(height/2)
root.pack()
main.geometry('%dx%d+%d+%d' %(800,250,x,y))
# To keep GUI window running
main.mainloop() 
