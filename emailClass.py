from tkinter import *

class email:
    def __init__(self, content, id, subj, body):
        self.id = id
        self.subj = subj
        self.body = body
        self.subj_elem = Label(content, text=self.subj)
        self.body_elem = Label(content, text=self.body)
        self.button = Button(content, text="delete", command=self.remove)
    
    def addEmail(self, row):
        self.subj_elem.grid(column=0, row=row, columnspan=2, rowspan=1)
        self.button.grid(column=5, row=row, columnspan=1, rowspan=1)
    
    def remove(self):
        self.subj_elem.destroy()
        self.body_elem.destroy()
        self.button.destroy()