#!/usr/bin/env python3

import sys
import smtplib, ssl, mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

import credentials

################################################################################
def sendalert(tolist, subject, message):
    context = ssl.create_default_context()
    messagetosend = "Subject: {}\n\n{}".format(subject, message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(credentials.easynotify_SENDER, credentials.easynotify_SENDER_psk)
        senterrors = server.sendmail(credentials.easynotify_SENDER, tolist, messagetosend)
        server.quit()
        return senterrors



# TODO - this isn't done yet.. and it should only be used for text files... right?
################################################################################
def sendfile_inline(tolist, subject, filename):
    with open(filename, 'r') as msgfile:
        message = msgfile.read()
        context = ssl.create_default_context()
        messagetosend = "Subject: {}\n\n{}".format(subject, message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(credentials.easynotify_SENDER, credentials.easynotify_SENDER_psk)
            senterrors = server.sendmail(credentials.easynotify_SENDER, tolist, messagetosend)
            server.quit()
            return senterrors




# https://stackoverflow.com/questions/23171140/how-do-i-send-an-email-with-a-csv-attachment-using-python
# https://docs.python.org/3.4/library/email-examples.html
#######################################################################################
def sendcsv(tolist, subject, filename):
    username = credentials.easynotify_SENDER
    password = credentials.easynotify_SENDER_psk

    msg = MIMEMultipart()
    msg["From"] = credentials.easynotify_SENDER
    msg["To"] = tolist
    msg["Subject"] = subject
    msg.preamble = "see attached"

    ctype, encoding = mimetypes.guess_type(filename)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(filename)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(filename, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(filename, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(filename, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=filename)
    msg.attach(attachment)

    server = smtplib.SMTP("smtp.gmail.com:587") # 465
    server.starttls()
    server.login(username,password)
    server.sendmail(credentials.easynotify_SENDER, tolist, msg.as_string())
    server.quit()





###########################
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print()
        print("give only 3 arguments")
        print(f"eg: {str(sys.argv[0])} 'to' 'subject' 'message'")
        exit()

    print(f"sending message:\nSubj:{str(sys.argv[1])}\nMesg:{str(sys.argv[2])}")
    sendalert(credentials.easynotify_RECEIVER, str(sys.argv[1]), str(sys.argv[2]))
