from tkinter import *
from emailClass import email
from gui_frame import *

# TODO make into thread

class gui:
    def __init__(self):
        content.grid(column=0, row=0)

        bannerFrame = Frame(content, borderwidth=0, relief="flat", width=600)
        banner = Label(content, text="WOOOOO BANNNANER")
        bannerFrame.grid(column=0, row=0, columnspan=maxCol, rowspan=1)
        banner.grid(column=0, row=0, columnspan=maxCol, rowspan=1, sticky=N, pady=10)
        print("banner placed")

        test = email("scammer@scammer.com", 1, "hehe this is a scam", 
            "give movcney give movcney give movcney give movcney give movcney give movcney give movcney give movcney give movcney give movcney give movcney give movcney give movcney", 50)
        test2 = email("a", 1, "adsfsadf", "hehe scam", "scam@s.cam")
        test3 = email("a", 1, "fjdpaosi", "fjdsaoiufj", "scam@s.cam")
        test4 = email("a", 4, "subjec", "body", "email")
        print(len(email.emailList))

        content.columnconfigure(1, weight=1)

        email.renderAllEmails()
        print("emails rendered")

        root.mainloop()