def genEmails():

    import email
    import imaplib as imap


    address = "emailtestingmoco@gmail.com"
    password = open("pwd.txt","r").read()
    server = 'imap.gmail.com'

    mail  = imap.IMAP4_SSL(server)
    mail.login(address, password)

    mail.select('inbox')

    status, data = mail.search(None, 'ALL')

    ids = []

    for i in data:
        ids += i.split()
    emails = {}
    count = 0
    for id in ids:
        emailStatus, emailData = mail.fetch(id, '(RFC822)')
        for response_part in emailData:
            if isinstance(response_part, tuple):

                encodedEmail = email.message_from_bytes(response_part[1])
                headline = encodedEmail['subject']

                if encodedEmail.is_multipart():
                    content = ''

                    for i in encodedEmail.get_payload():
                        if i.get_content_type() == 'text/plain':
                            content = i.get_payload()

                else:

                    content = encodedEmail.get_payload()

                FinalOutput = ("Subject: " + headline +" "+ content).replace("\n", "").replace("\r", "")
                emails[ids[count]] = FinalOutput
        count += 1

    return emails

print(genEmails())