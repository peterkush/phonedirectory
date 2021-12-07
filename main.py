
from tkinter import *

class Application(object):
     def __init__(self,master ):
         self.master=master
         #frame
         self.top = Frame(master,  height=150,bg='pink')
         self.top.pack(fill='x')



def main():
    root = Tk()
    app=Application(root)

    root.geometry("650x550+350+20")
    root.title("Phone Book Apps")
    root.resizable(False,False)

    root.mainloop()

if __name__ == '__main__':
    main()