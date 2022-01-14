#!/usr/bin/env python3

import smtplib, ssl, sys


import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText



import credentials

################################################################################
def sendalert(message, subject="alert", tolist=credentials.easynotify_RECEIVER):
    context = ssl.create_default_context()
    messagetosend = "Subject: {}\n\n{}".format(subject, message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(credentials.easynotify_SENDER, credentials.easynotify_SENDER_psk)
        senterrors = server.sendmail(credentials.easynotify_SENDER, tolist, messagetosend)
        server.quit()
        return senterrors

################################################################################
def sendfile_inline(filename, subject="file", tolist=credentials.easynotify_RECEIVER):
    with open(filename, 'r') as msgfile:
        message = msgfile.read()
        context = ssl.create_default_context()
        messagetosend = "Subject: {}\n\n{}".format(subject, message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(credentials.easynotify_SENDER, credentials.easynotify_SENDER_psk)
            senterrors = server.sendmail(credentials.easynotify_SENDER, tolist, messagetosend)
            server.quit()
            return senterrors

#######################################################################################
def sendcsv(filename, subject="file attached", tolist=credentials.easynotify_RECEIVER):
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


# ###########################
# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print()
#         print("give only 2 arguments")
#         print(f"eg: {str(sys.argv[0])} 'subject' 'message'")
#         print("easy_notify.py 'PRICE ALERT: upper limit' 'hey, bro, the price is WAY up!'")
#         exit()

#     print(f"sending message:\nSubj:{str(sys.argv[1])}\nMesg:{str(sys.argv[2])}")
#     sendalert(str(sys.argv[2]), str(sys.argv[1]))


###########################
if __name__ == "__main__":
    sendcsv('good_units.csv')
