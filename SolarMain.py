from tkinter import *
from PIL import Image , ImageTk

window = Tk()
window.geometry("1000x1000")
window.title("Solar")
window.config(background= "Black")
title = Label(window,text="Welcome to solar")
title.pack()
img = Image.open( "C:\\Users\\piahp\\Downloads\\solarsystem.png")
respic = img.resize((500,500))
tkimage = ImageTk.PhotoImage(respic)
intro = Label(window,text=" Welcome aboard the Starbound Explorer, Captain !Your adventure is about to begin. What shall we call you, Captain?")
intro.pack()
imglab = Label(window, image = tkimage )
startlab = Label(window,text="Are you ready to GO?")
planetmasslab = Label(window,text = "")
planetdiameterlab = Label(window,text="")
planetcollab = Label(window,text="")
planettemplab = Label(window,text="")
planetmoonslab = Label(window,text="")
planetlab = Label(window,text="")
planetmass = 0
planetdiameter = 0
planetcol = 0
planettemp = 0
planetmoons = 0
planet = 0

def submit():
    username = entry.get()
    name  = Label(window,text = "Hello Captian "+username+ "!")
    name.place(x=0, y=0)
    print(username)
    submit1.destroy()
    entry.destroy()
    startlab.place(x=450, y=600)
    subYes.place(x=475, y=700)
    subNo.place(x=525, y=700)


def submitYes():
    intro.destroy()
    title.destroy()
    imglab.destroy()
    startlab.destroy()
    subYes.destroy()
    subNo.destroy()
    nextbut.place()
    earth()
def submitNo():
    intro.destroy()

subYes = Button(window, text="yes", command=submitYes)
subNo = Button(window, text="no", command=submitNo)

submit1 = Button(window,text="submit",command=submit)
submit1.place(x=600,y=600)

imglab.image = tkimage
imglab.config(background= "Black")
imglab.pack()
img.save("solarsystem.png")

entry = Entry()
entry.config(width = 10)
entry.place(x=475,y=600)
entry.pack()


def earth():
    planetmasslab.config(text="196.9 Million mi^2")
    planetdiameterlab.config(text="7926.2 Mi")
    planetcollab.config(text = "100%")
    planettemplab.config(text = " 59F")
    planetmoonslab.config(text = "1")
    planetlab.config(text = "")
    planetmasslab.place(x=10, y=10)
    planetdiameterlab.place(x=10, y=30)
    planetcollab.place(x=10, y=50)
    planettemplab.place(x=10, y=70)
    planetmoonslab.place(x=10, y=90)
    planetlab.place(x=10, y=110)

def mercury():
    planetmasslab.config(text="28.8 Million mi^2")
    planetdiameterlab.config(text="3031.9")
    planetcollab.config(text = "0%")
    planettemplab.config(text = "333F")
    planetmoonslab.config(text = "0")
    planetlab.config(text = "59 Earth days")
    planetmasslab.place(x=10, y=10)
    planetdiameterlab.place(x=10, y=30)
    planetcollab.place(x=10, y=50)
    planettemplab.place(x=10, y=70)
    planetmoonslab.place(x=10, y=90)
    planetlab.place(x=10, y=110)

def mars():
    planetmasslab.config(text="55.74 Million mi^2")
    planetdiameterlab.config(text= "4212.3 Mi")
    planetcollab.config(text = "1%")
    planettemplab.config(text = "-85F")
    planetmoonslab.config(text = "2")
    planetlab.config(text = "24.6 hr")
    planetmasslab.place(x=10, y=10)
    planetdiameterlab.place(x=10, y=30)
    planetcollab.place(x=10, y=50)
    planettemplab.place(x=10, y=70)
    planetmoonslab.place(x=10, y=90)
    planetlab.place(x=10, y=110)

def jupiter():
    planetmasslab.config(text="23.71 billion mi^2")
    planetdiameterlab.config(text = "86881")
    planetcollab.config(text = "0")
    planettemplab.config(text = "-166F")
    planetmoonslab.config(text = "95")
    planetlab.config(text = "9.9hr")
    planetmasslab.place(x=10, y=10)
    planetdiameterlab.place(x=10, y=30)
    planetcollab.place(x=10, y=50)
    planettemplab.place(x=10, y=70)
    planetmoonslab.place(x=10, y=90)
    planetlab.place(x=10, y=110)
def venus():
    planetmasslab.config(text="177.7 million mi^2")
    planetdiameterlab.config(text = "7520.8 mi")
    planetcollab.config(text = "0%")
    planettemplab.config(text = "867F")
    planetmoonslab.config(text = "0")
    planetlab.config(text = "243 earth days ")
    planetmasslab.place(x=10, y=10)
    planetdiameterlab.place(x=10, y=30)
    planetcollab.place(x=10, y=50)
    planettemplab.place(x=10, y=70)
    planetmoonslab.place(x=10, y=90)
    planetlab.place(x=10, y=110)
def saturn():
    planetmasslab.config(text = "16.49 Billion mi^2")
    planetdiameterlab.config(text = "72367")
    planetcollab.config(text = "0%")
    planettemplab.config(text = "-220F")
    planetmoonslab.config(text = "274")
    planetlab.config(text = "10.5 hr")
    planetmasslab.place(x=10, y=10)
    planetdiameterlab.place(x=10, y=30)
    planetcollab.place(x=10, y=50)
    planettemplab.place(x=10, y=70)
    planetmoonslab.place(x=10, y=90)
    planetlab.place(x=10, y=110)
def uranus():
    planetmasslab.config(text = "3.121 Billion mi^2")
    planetdiameterlab.config(text = "31518")
    planetcollab.config(text = "0%")
    planettemplab.config(text = "-320F")
    planetmoonslab.config(text = "28")
    planetlab.config(text = "17 hr")
    planetmasslab.place(x=10, y=10)
    planetdiameterlab.place(x=10, y=30)
    planetcollab.place(x=10, y=50)
    planettemplab.place(x=10, y=70)
    planetmoonslab.place(x=10, y=90)
    planetlab.place(x=10, y=110)
def neptune():
    planetmasslab.config(text = "2.941 Billion mi^2")
    planetdiameterlab.config(text = "30599")
    planetcollab.config(text = "0%")
    planettemplab.config(text = "-330F")
    planetmoonslab.config(text = "16")
    planetlab.config(text = "16 Hours")
    planetmasslab.place(x=10, y=10)
    planetdiameterlab.place(x=10, y=30)
    planetcollab.place(x=10, y=50)
    planettemplab.place(x=10, y=70)
    planetmoonslab.place(x=10, y=90)
    planetlab.place(x=10, y=110)
window.counter = 0
def next():
    funclist=[earth(),mars()]
    window.counter += 1
    return funclist[window.counter]
    print(window.counter)



nextbut = Button(window, text="next", command = next())





nextbut.place(x= 10 , y = 50)














window.mainloop()




window.mainloop()
