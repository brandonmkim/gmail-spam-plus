from tkinter import *
import time
from emailClass import email

#tkinter setup
#TODO Make this stuff into a thread
#TODO use bubble sort to sort email stuff
#TODO pass in main class instance of tkinter
#TODO put this wholeeee thing into a class 

root = Tk()
content = Frame(root, width=600, height=200, bg='white')
frame = Frame(content, borderwidth=0, relief="flat", width=600, height=300, bg='white')
banner = Label(content, text="WOOOOOO BANNER")

emails = []

#Bubble Sort Algo
for i in range(len(emails)):
    for x in range(1,i):
        if(emails[i].getAccuracy()>emails[x].getAccuracy()):
            emails[i],emails[x] = emails[x],emails[i]

test = email(content, "subject",'b1', "body body body")
emails.append(test)
test2 = email(content, "again",'b1', "bsaniudashj")
emails.append(test2)

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=4)

banner.grid(column=0, row=0, columnspan=5, rowspan=1) #max width
row = 1
for e in emails:
    e.addEmail(row)
    row = row + 1

root.mainloop()