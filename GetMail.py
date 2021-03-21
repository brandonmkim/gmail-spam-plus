import email
import imaplib as imap
import time
from emailClass import emails
import nlp.SpamClassifier as sc
import threading

class EmailHook:
    def __init__(self, email, pwrd, server):
        self.address = email
        self.p = pwrd
        self.mail = imap.IMAP4_SSL(server)
        self.texts=[]
        #self.deleted=[]

    def connect(self):
        self.mail.login(self.address,self.p)
        self.mail.select('inbox')

###############################################
    def moveToTrash(self, id):
        self.mail.select('inbox')
        self.mail.store(id, '+X-GM-LABELS', '\Trash')

    def restore(self, id):
        self.mail.select('[Gmail]/Trash')
        self.mail.store(id, '-X-GM-LABELS', '\Trash')

        status, search_data = self.mail.search(None, 'ALL')
        ids = []
        for i in search_data:
            ids += i.split()
        print(ids)
        temp = str(id).split("'")
        print(temp)
        pos = int(temp[1])-1
        print(pos)
        for i in range(pos+1,len(self.texts)):
            self.texts[i].setID(ids[i-1])


    def permDelete(self, id):
        self.mail.select('[Gmail]/Trash')
        status, search_data = self.mail.search(None, 'ALL')

        ids = []

        for i in search_data:
            ids += i.split()
            
        temp = str(id).split("'")
        pos = int(temp[1])-1

        for i in self.texts:
            if i.getID() == id:
                self.texts.remove(i)
                break
        
        self.mail.store(id, '+FLAGS', '\Deleted')
        self.mail.expunge()
        
        for i in range(pos,len(self.texts)):
            self.texts[i].setID(ids[i-1])
####################################################

    def loop(self,tk):
        self.mail.select('inbox')
        status, data = self.mail.search(None, 'ALL')
        ids = []
        deleted=0
        for i in data:
            ids += i.split()
        for id in ids:
            emailStatus, emailData = self.mail.fetch(id, '(RFC822)')
            for response_part in emailData:
                if isinstance(response_part, tuple):
                    encodedEmail = email.message_from_bytes(response_part[1])
                    person = encodedEmail['from']
                    headline = encodedEmail['subject']

                    date = encodedEmail['date']
                    monthToNum = {'Jan' : "01",'Feb' : "02",'Mar' : "03",'Apr' : "04",'May' : "05",'Jun' : "06",'Jul' : "07",'Aug' : "08",'Sep' : "09",'Oct' : "10",'Nov' :"11",'Dec' : "12"}
                    date = date.split(" ")
                    t = date[4].split(":")
                    date = int(date[3] + monthToNum[date[2]]+ date[1] + t[0] + t[1]+ t[2])
                    
                    if encodedEmail.is_multipart():
                        content = ''
                        for i in encodedEmail.get_payload():
                            if i.get_content_type() == 'text/plain':
                                content = i.get_payload()
                    else:
                        content = encodedEmail.get_payload()

                    newstr = ("Subject: " + headline +" "+ content).replace("\n", "").replace("\r", "")
                
                    #Predict if email is spam.
                    #print("hellloooo")
                    pred,typ = sc.spamDetect(newstr)
                    #print(typ)
                    #print(pred)
                    print(pred, " a ", typ[0], "b ", newstr)
                    if(pred>0.6 and typ[0]=='spam'):
                        temp = str(id).split("'")
                        temp[1]= str(len(self.texts)+deleted+1)
                        deleted += 1

                        e = emails(self,person,(temp[1]).encode('utf8'),date,headline,content,pred)
                        self.texts.insert(0,e)
                        self.moveToTrash(id)
                        for i in range(len(self.texts)):
                            for x in range(i+1,len(self.texts)):
                                if int(self.texts[i].getTime())<int(self.texts[x].getTime()):
                                    if self.texts[i].stripID() > self.texts[x].stripID():
                                        temp = self.texts[i].getID()
                                        self.texts[i].setID(self.texts[x].getID())
                                        self.texts[x].setID(temp)
                                    
                                    self.texts[x],self.texts[i]=self.texts[i],self.texts[x]
        
        for i in range(len(self.texts)):
            for x in range(i+1,len(self.texts)):
                if self.texts[i].stripID() > self.texts[x].stripID():
                    temp = self.texts[i].getID()
                    self.texts[i].setID(self.texts[x].getID())
                    self.texts[x].setID(temp)

        for i in self.texts:
            print(i.getTime(), " ", i.getID())
        
        print(self.texts)

        for i in self.texts:
            print(i.getTime(), " ", i.getID())

    def getEmails(self):
        return self.texts