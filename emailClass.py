from gui_frame import *
from tkinter import *
from renderAllEmails import *
from PIL import ImageTk, Image
   
class emails:
    emailList = []
    def __init__(self, emailhook, person, emailID, time, st, subj, body, acc):
        #TODO can u move this into the GUI and access the emailhook stuff when u remove a line and get the emaillist
        #TODO Also put the restore function from the EmailHook w/ the gui.
        self.hook = emailhook
        self.emailFrame = Frame(content, background="bisque")

        self.person = person
        self.emailID = emailID
        self.acc = acc
        self.time = time
        self.st = st

        self.id = emailID
        self.subj = subj
        if self.subj == "":
            self.subj = "[no header]"
        self.subj_elem = Label(self.emailFrame, text=subj, wraplength=450, justify=LEFT, font=gui_frame.font_bold, background="pink")
        self.body = body
        if body == "":
            self.subj = "[no body]"
        self.body_elem = Label(self.emailFrame, text=body, wraplength=450, font=gui_frame.font_normal, justify=LEFT)

        trash = ImageTk.PhotoImage( Image.open("assets/trash.png").resize((36, 36), Image.ANTIALIAS) )
        self.trashButton = Button(content, image=trash, command=lambda: self.remove())
        self.trashButton.image = trash

        restore = ImageTk.PhotoImage( Image.open("assets/restore.png").resize((36, 36), Image.ANTIALIAS) )
        self.restoreButton = Button(content, image=restore, command=lambda: self.restore())
        self.restoreButton.image = restore

        self.expanded = IntVar()
        collapsed = ImageTk.PhotoImage( Image.open("assets/closed.png").resize((20, 20), Image.ANTIALIAS) )
        expanded = ImageTk.PhotoImage( Image.open("assets/open.png").resize((20, 20), Image.ANTIALIAS) )
        self.expandedButton = Checkbutton(content, variable=self.expanded, command=lambda: self.expandBody(), image=collapsed, selectimage=expanded, indicatoron=False)
        self.expandedButton.image = collapsed
        self.expandedButton.selectimage = expanded
        
        self.row = 0
        
    def getAccuracy(self):
        return self.acc

    # creates label and button on gui at newRow
    def renderEmail(self, newRow):
        # renders email
        self.expandedButton.grid(   column=0,           columnspan=1,           row=newRow, rowspan=1, padx=8, pady=8, sticky=NW)
        
        self.emailFrame.grid(       column=1,                                   row=newRow,            padx=8, pady=8, sticky=W)
        self.subj_elem.grid(        column=0,           columnspan=1,           row=0,      rowspan=1, padx=8, pady=8, sticky=W)

        self.restoreButton.grid(    column=maxCol-1,    columnspan=1,           row=newRow, rowspan=1, padx=8, pady=8, sticky=NE)
        self.trashButton.grid(      column=maxCol,      columnspan=1,           row=newRow, rowspan=1, padx=8, pady=8, sticky=NW)
        self.row = newRow
    
    def setID(self, i):
        self.id = i

    def remove(self):
        self.expanded = 0
        self.expandedButton.destroy()
        self.emailFrame.destroy()
        self.subj_elem.destroy()
        self.body_elem.destroy()
        self.restoreButton.destroy()
        self.trashButton.destroy()

        self.hook.permDelete(self.st)
        renderAllEmails(self.hook.getEmails())

    def restore(self):
        self.expanded = 0
        self.expandedButton.destroy()
        self.emailFrame.destroy()
        self.subj_elem.destroy()
        self.body_elem.destroy()
        self.restoreButton.destroy()
        self.trashButton.destroy()

        self.hook.restore(self.getID(),self.st)
        renderAllEmails(self.hook.getEmails())
    
    def getST(self):
        return self.st

    def getID(self):
        return self.emailID

    def stripID(self):
        return int(str(self.getID()).split("'")[1])

    def getTime(self):
        return self.time

    def expandBody(self):
        state = self.expanded.get()
        if state == 1:
            self.body_elem.grid(column=0, row=1, padx=8, pady=8, sticky=W)
        elif state == 0:
            self.body_elem.grid_forget()
