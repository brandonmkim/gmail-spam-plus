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
        
    def connect(self):
        self.mail.login(self.address,self.p)
        self.mail.select('inbox')

    def validate(self):
        self.mail.login(self.address,self.p)
        self.mail.logout()

###############################################
    def moveToTrash(self, string):
        self.mail.select('inbox')
        status, data = self.mail.search(None, 'ALL')
        ids=[]
        for i in data:
            ids += i.split()

        print("LIST OF IDS ", ids)

        for id in ids:
            emailStatus, emailData = self.mail.fetch(id, '(RFC822)')
            for response_part in emailData:
                if isinstance(response_part, tuple):
                    encodedEmail = email.message_from_bytes(response_part[1])
                    person = encodedEmail['from']
                    headline = encodedEmail['subject']
                    date = encodedEmail['date']
                    print(date," ",string)
                    if string==date:
                        print(headline, "TRUE")
                        self.mail.store(id, '+X-GM-LABELS', '\Trash')
                        break
        

    def restore(self,id,string):
        self.mail.select('[Gmail]/Trash')

        status, data = self.mail.search(None, 'ALL')
        ids=[]
        for i in data:
            ids += i.split()
        
        print("LIST OF IDS ", ids)
        for ide in ids:
            emailStatus, emailData = self.mail.fetch(ide, '(RFC822)')
            for response_part in emailData:
                if isinstance(response_part, tuple):
                    encodedEmail = email.message_from_bytes(response_part[1])
                    headline = encodedEmail['subject']
                    sender = encodedEmail['From']
                    date = encodedEmail['date']
                    if encodedEmail.is_multipart():
                        content = ''
                        for i in encodedEmail.get_payload():
                            if i.get_content_type() == 'text/plain':
                                content += i.get_payload()
                    else:
                        content = encodedEmail.get_payload()
                if string== date:
                    message = email.message.Message()
                    message['From'] = sender
                    message['subject'] = headline
                    message.set_payload(content)
                    self.mail.append('INBOX', '', imap.Time2Internaldate(time.time()), str(message).encode('utf-8'))
                    self.permDelete(string)

    def permDelete(self, time):
        self.mail.select('[Gmail]/Trash')
        status, search_data = self.mail.search(None, 'ALL')

        status, data = self.mail.search(None, 'ALL')
        ids=[]
        for i in data:
            ids += i.split()

        print("LIST OF IDS ", ids)

        for id in ids:
            emailStatus, emailData = self.mail.fetch(id, '(RFC822)')
            for response_part in emailData:
                if isinstance(response_part, tuple):
                    encodedEmail = email.message_from_bytes(response_part[1])
                    person = encodedEmail['from']
                    headline = encodedEmail['subject']
                    date = encodedEmail['date']
                    print(date," ",time)
                    if time==date:
                        print(headline, "TRUE")
                        print("before", self.texts)
                        for i in self.texts:
                            if i.getST() == time:
                                self.texts.pop( self.texts.index(i) )
                                break
                        print("AFTER:", self.texts)
                        self.mail.store(id, '+FLAGS', '\Deleted')
                        self.mail.expunge()
                        break

    def addDeleted(self,tk):
        self.mail.select('[Gmail]/Trash')
        status, data = self.mail.search(None, 'ALL')
        ids = []

        for i in data:
            ids += i.split()
        for id in ids:
            emailStatus, emailData = self.mail.fetch(id, '(RFC822)')
            for response_part in emailData:
                try:
                    if isinstance(response_part, tuple):
                        encodedEmail = email.message_from_bytes(response_part[1])
                        person = encodedEmail['from']
                        headline = encodedEmail['subject']
                        date1=encodedEmail['date']
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

                        e = emails(self,person,id,date,date1,headline,content,1)
                        self.texts.append(e)
                except:
                    continue

####################################################

    def loop(self,tk):
        self.mail.select('inbox')
        status, data = self.mail.search(None, 'ALL')
        ids = []

        for i in data:
            ids += i.split()

        print("LIST OF IDS ", ids)

        for id in ids:
            emailStatus, emailData = self.mail.fetch(id, '(RFC822)')
            for response_part in emailData:
                if isinstance(response_part, tuple):
                    encodedEmail = email.message_from_bytes(response_part[1])
                    person = encodedEmail['from']
                    headline = encodedEmail['subject']
                    date = encodedEmail['date']
                    print(person)
                    print(headline)

                    
                    monthToNum = {'Jan' : "01",'Feb' : "02",'Mar' : "03",'Apr' : "04",'May' : "05",'Jun' : "06",'Jul' : "07",'Aug' : "08",'Sep' : "09",'Oct' : "10",'Nov' :"11",'Dec' : "12"}
                    print(date)
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
                    
                    print("\n", id.decode(), "<id to content>", content,"\n")

                    newstr = ("Subject: " + headline +" "+ content).replace("\n", "").replace("\r", "")
                
                    #Predict if email is spam.
                    pred,typ = sc.spamDetect(newstr)
                    print(pred)
                    if(pred>0.6 and typ[0]=='spam'):
                        e = emails(self,person,id,date,encodedEmail['date'],headline,content,pred)
                        self.texts.insert(0,e)
                        self.moveToTrash(encodedEmail['date'])

    def getEmails(self):
        return self.texts