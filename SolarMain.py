from tkinter import *
from PIL import Image , ImageTk



window = Tk()
window.geometry("1000x1000")
window.title("Solar")
window.config(background= "Black")
title = Label(window,text="Welcome to solar")
title.pack()
img = Image.open( "C:\\users\\hetad\\Downloads\\solarsystem.png")
respic = img.resize((500,500))
tkimage = ImageTk.PhotoImage(respic)
intro = Label(window,text=" Welcome aboard the Starbound Explorer, Captain !Your adventure is about to begin. What shall we call you, Captain?")
intro.pack()
imglab = Label(window, image = tkimage )
startlab = Label(window,text="Are you ready to GO?")


def earth():
def
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
    intro.config(text="This is" + )






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
entry.pack

























window.mainloop()