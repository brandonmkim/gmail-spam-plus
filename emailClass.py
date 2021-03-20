from tkinter import *

class email:
    def __init__(self, person, id, subj, body, acc):
        self.id = id
        self.subj = subj
        self.body = body
        self.subj_elem = Label(person, text=self.subj)
        self.body_elem = Label(person, text=self.body)
        self.button = Button(person, text="delete", command=self.remove)
        self.acc = acc
        
    def addEmail(self, row):
        self.subj_elem.grid(column=0, row=row, columnspan=2, rowspan=1)
        self.button.grid(column=5, row=row, columnspan=1, rowspan=1)
    
    def remove(self):
        self.subj_elem.destroy()
        self.body_elem.destroy()
        self.button.destroy()