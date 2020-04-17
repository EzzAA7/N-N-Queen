from tkinter import Tk,Label,Grid,Button,Entry,Frame,BOTH,LEFT,RIGHT,CENTER,TOP,BOTTOM,IntVar,W,Radiobutton
from Components.MainController import *

root=Tk()
root.columnconfigure(0, minsize=250)
root.rowconfigure([0, 1], minsize=100)
root.title("Start")
root.geometry("200x220")

frame1=Frame(master=root)
frame2=Frame(master=root)
frame3=Frame(master=root)

lbl=Label(master=frame1,text="NxN Queen Puzzle",font=('Roboto','15'))
lbl.pack()
frame1.pack(fill=BOTH, side=TOP, expand=False)

lbl=Label(master=frame2,text="Enter N Value")
lbl.grid(row=0,column=0)
ent = Entry(master=frame2,bg="white", width=20)
ent.grid(row=1,column=0)

def clickedSubmit():
    lblN=Label(master=frame3,text=f'You created a {int(ent.get())} Queen Puzzle !')
    lblN.grid(row=1,column=0)

btnN = Button(master=frame2,
    text="Submit",
    command=clickedSubmit
)
btnN.grid(row=2,column=0)
frame2.pack( side=TOP, expand=False)

valueN = IntVar()
rb=valueN.get()
    
def clickedStart():
    # print(valueN.get())
    N = int(ent.get())
    rb=valueN.get()
    frame1.destroy()
    frame2.destroy()
    frame3.destroy()
    puzzle_window(root,N,rb)
    
Label(master=frame3, text="""Choose Method:""",justify = LEFT,padx = 20).grid(row=2,column=0)
Radiobutton(master=frame3, text="Custom",padx = 20, variable=valueN, value=1).grid(row=3,column=0)
Radiobutton(master=frame3, text="Random",padx = 20, variable=valueN, value=2).grid(row=4,column=0)
btnStart = Button(master=frame3,text="Start",command=clickedStart)
btnStart.grid(row=5,column=0)
frame3.pack(side=BOTTOM, expand=False)

