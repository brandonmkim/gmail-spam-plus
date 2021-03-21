from emailClass import emails
from GetMail import EmailHook
from gui_frame import *
from PIL import ImageTk, Image
from emailClass import email

# TODO figure out what to do w/ sorting

class gui:
    def __init__(self,root,eh):
        self.root = root
        self.emailhook = eh
    
    def sort(self):
        for i in range(len(self.emailhook.getEmails())):
            for x in range(i,len(self.emailhook.getEmails())):
                if(self.emailhook.getEmails()[i].getAccuracy() > self.emailhook.getEmails()[x].getAccuracy()):
                    self.emailhook.getEmails()[i],self.emailhook.getEmails()[x] = self.emailhook.getEmails()[x],self.emailhook.getEmails()[i]

    def renderAllEmails(self):
        if len(self.emailhook.getEmails()) > 0:
            row = 1
            for e in self.emailhook.getEmails():
                e.renderEmail(row)
                row += 1
        else:
            Label(content, text="No more emails! Maybe ask a Nigerian prince for more?").grid(column=0, columnspan=maxCol, row=1, pady=8)

    def createGUI(self):
        content.grid(column=0, row=0)
        
        bannerFrame = Frame(content, borderwidth=0, relief="flat", width=600)

        bannerimg = ImageTk.PhotoImage( Image.open("assets/wtf.png").resize((600,200), Image.ANTIALIAS) )
        banner = Label(content, image=bannerimg)
        bannerFrame.image = bannerimg

        bannerFrame.grid(column=0, row=0, columnspan=maxCol, rowspan=1)
        banner.grid(column=0, row=0, columnspan=maxCol, rowspan=1, sticky=N, pady=10)

        content.grid_columnconfigure(1, weight=1)

        self.renderAllEmails()
        
        self.root.mainloop()