from tkinter import Tk,Label,Grid,Button,Entry,Frame,BOTH,LEFT,RIGHT,CENTER,TOP,BOTTOM,IntVar,W,Radiobutton
from Components.MainController import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        # place button at (0,0)
        # exitButton.place(x=0, y=0)

        self.frame1=Frame(master=root)
        self.frame2=Frame(master=root)
        self.frame3=Frame(master=root)

        lbl=Label(master=self.frame1,text="NxN Queen Puzzle",font=('Roboto','15'))
        lbl.pack()
        self.frame1.pack(fill=BOTH, side=TOP, expand=False)

        lbl=Label(master=self.frame2,text="Enter N Value")
        lbl.grid(row=0,column=0)
        self.ent = Entry(master=self.frame2,bg="white", width=20)
        self.ent.grid(row=1,column=0)

        
        btnN = Button(master=self.frame2,
            text="Submit",
            command=self.clickedSubmit
        )
        btnN.grid(row=2,column=0)
        self.frame2.pack( side=TOP, expand=False)

        self.valueN = IntVar()

        Label(master=self.frame3, text="""Choose Method:""",justify = LEFT,padx = 20).grid(row=2,column=0)
        Radiobutton(master=self.frame3, text="Custom",padx = 20, variable=self.valueN, value=1).grid(row=3,column=0)
        Radiobutton(master=self.frame3, text="Random",padx = 20, variable=self.valueN, value=2).grid(row=4,column=0)
        btnStart = Button(master=self.frame3,text="Start",command=self.clickedStart)
        btnStart.grid(row=5,column=0)
        self.frame3.pack(side=BOTTOM, expand=False)

    def clickedSubmit(self):
        lblN=Label(master=self.frame3,text=f'You created a {int(self.ent.get())} Queen Puzzle !')
        lblN.grid(row=1,column=0)
        
    def clickedStart(self):
        # print(self.valueN.get())
        self._frame = None
        self.switch_frame()

    
                    
if __name__ == "__main__":

    root=Tk()
    app=Window(root)
    root.columnconfigure(0, minsize=250)
    root.rowconfigure([0, 1], minsize=100)
    root.title("Hello")
    root.geometry("200x220")
    root.mainloop()
