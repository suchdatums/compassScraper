#!/usr/bin/env python3

import smtplib, ssl
import sys

#from credentials import *
import credentials

def sendalert(message, subject="alert", tolist=credentials.easynotify_RECEIVER):
# returns {} if successful
# TODO - this is a maturing module.. I need mature comments, you bitch!
    context = ssl.create_default_context()
    messagetosend = "Subject: {}\n\n{}".format(subject, message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(credentials.easynotify_SENDER, credentials.easynotify_SENDER_psk)
        senterrors = server.sendmail(credentials.easynotify_SENDER, tolist, messagetosend)
        server.quit()

        ### TODO THIS IS A HUGE PROBLEM.. IF I HAVE MISSION CRITICAL FAILURES AND
        ### NO NOTIFICATION COMES OUT.. HOW DO I FAIL GRACEFULLY??
        #if {} == senterrors:
        #    print("success")
        #else:
        #    print(senterrors)

        return senterrors

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print()
        print("give only 2 arguments")
        print(f"eg: {str(sys.argv[0])} 'subject' 'message'")
        print("easy_notify.py 'PRICE ALERT: upper limit' 'hey, bro, the price is WAY up!'")
        exit()

    print(f"sending message:\nSubj:{str(sys.argv[1])}\nMesg:{str(sys.argv[2])}")
    sendalert(str(sys.argv[2]), str(sys.argv[1]))
