
from tkinter import *
from datetime import date, datetime
import datetime

date = datetime.datetime.now().date()
date = str(date)

class Application(object):
     def __init__(self,master ):
         self.master=master

         #frame
         self.top = Frame(master,  height=150,bg='pink')
         self.top.pack(fill = X)

         self.bottom = Frame(master,  height=500,bg='#84DFFF')
         self.bottom.pack(fill = X)
         self.heading =Label(self.top,text ='my phoneBook App',font='arial 15 bold ',bg='white',fg='gold')
         self.heading.place(x=230,y=50)

         self.heading =Label(self.top,text ='today date'+date,font='arial 12 bold ',bg='white',fg='gold')
         self.heading.place(x=450,y=90)


         #BTN
         self.mypeople= Button(self.bottom,text ='my people',font='arial 12 bold ',bg='white',fg='gold')
         self.mypeople.place(x=250,y=70)

         self.addpeople= Button(self.bottom,text ='add people',font='arial 12 bold ',bg='white',fg='gold')
         self.addpeople.place(x=250,y=130)

         self.about= Button(self.bottom,text ='about us',font='arial 12 bold ',bg='white',fg='gold')
         self.about.place(x=250,y=190)








def main():
    root = Tk()
    app=Application(root)

    root.geometry("650x550+350+20")
    root.title("Phone Book Apps")
    root.resizable(False,False)

    root.mainloop()

if __name__ == '__main__':
    main()