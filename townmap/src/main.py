from tkinter import *
import itertools as it

class App:

    def __init__(self, master):

        rowCnt = it.count(0,1)
        frame = Frame(master)
        frame.pack()

        #header
        Label(frame,text="options").grid(row=next(rowCnt),columnspan=2,sticky=N)
        
        
        #number of hauses
        currRow = next(rowCnt)
        Label(frame, text="Houses").grid(row=currRow,sticky=NW)
        e_houses = Entry(frame)
        e_houses.grid(row=currRow,column=1,sticky=N)
        
        
        #canvas
        plot = Canvas(frame,width=200, height=100)
        plot.grid(row=0,column=2,rowspan=next(rowCnt))
        plot.create_rectangle(0, 0, 200, 100, fill="blue")
        plot.create_line(0, 0, 200, 100, fill="red", dash=(4, 4))


root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below