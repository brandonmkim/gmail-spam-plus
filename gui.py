from tkinter import *
from emailClass import email
from gui_frame import *

# TODO make into thread
# TODO actually put this in a class

#renders frame
max_col = 6
max_row = 5
content.grid(column=0, row=0)
bannerFrame.grid(column=0, row=0, columnspan=max_col, rowspan=1)
banner.grid(column=0, row=0, columnspan=max_col, rowspan=1, sticky=N, pady=10)

test = email("scammer", 1, "subject", "give movcney", "scam@s.cam")
test2 = email("a", 1, "adsfsadf", "hehe scam", "scam@s.cam")
test3 = email("a", 1, "fjdpaosi", "fjdsaoiufj", "scam@s.cam")
test4 = email("a", 4, "subjec", "body", "email")

email.renderAllEmails()

root.mainloop()