from GetMail import EmailHook
from gui_frame import *
from emailClass import emails
from renderAllEmails import *
from PIL import ImageTk, Image

# TODO figure out what to do w/ sorting

class gui:
    def __init__(self,root,eh):
        self.root = root
        self.emailhook = eh

        self.emailhook.connect()
    
    def sort(self):
        for i in range(len(self.emailhook.getEmails())):
            for x in range(i,len(self.emailhook.getEmails())):
                if(self.emailhook.getEmails()[i].getAccuracy() > self.emailhook.getEmails()[x].getAccuracy()):
                    self.emailhook.getEmails()[i],self.emailhook.getEmails()[x] = self.emailhook.getEmails()[x],self.emailhook.getEmails()[i]

    def createGUI(self):
        content.grid(column=0, row=0)
        
        bannerFrame = Frame(content, borderwidth=0, relief="flat", width=600)

        bannerimg = ImageTk.PhotoImage( Image.open("assets/wtf.png").resize((600,200), Image.ANTIALIAS) )
        banner = Label(content, image=bannerimg, background="white")
        bannerFrame.image = bannerimg

        bannerFrame.grid(column=0, row=0, columnspan=maxCol, rowspan=1)
        banner.grid(column=0, row=0, columnspan=maxCol, rowspan=1, sticky=N, pady=10)

        content.grid_columnconfigure(1, weight=1)
        
        counter = 0
        self.emailhook.loop(root)
        renderAllEmails(self.emailhook.getEmails())
        self.root.mainloop()
        # while True:
        #     if(counter == 1000 or counter == 0):
        #         print("entering hook loop ---------------------")
        #         self.emailhook.loop(root)
        #         counter = 1
        #     else:
        #         counter += 1
        #         self.renderAllEmails()
        #         self.root.update_idletasks()
        #         self.root.update()