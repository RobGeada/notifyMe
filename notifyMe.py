import smtplib
import datetime
import random
from email.mime.text import MIMEText

#I know I know it's plaintext what do you want from me
emailPass = raw_input("Email password: ")

#========Generate string with current time======================
def timeStr():
    currTime = datetime.datetime.now().time()
    if currTime.hour > 12:
        am = "PM"
        hour = currTime.hour - 12
    elif currTime.hour < 12:
        am = "AM"
        hour = currTime
    else:
        am = "PM"
        hour = 12
    currTime = "{}:{}:{} {}".format(hour,currTime.minute,currTime.second,am)
    return "\n\nAt {}, you asked me to notify you of the following: \n".format(currTime)

#========Generate random greeting===============================
def randGreeting():
    seed = random.randint(0,5)
    greetings = ["Hi!","Hello friend!","'What's up dude!","Hear thee, hear thee!","Hey there!","Psst!"]
    return greetings[seed]

#=======Print out spacer line=================================
def spacer():
    return "\n=======================================================\n\n"

#========Generate random sign off===============================
def randSignOff():
    seed = random.randint(0,5)
    signoffs = ["Love,","Hope it was everything you wanted and more,","Warmest regards from my cold, metal heart,","Catch you on the flip side,","Sent from my iPhone,","May your code forever compile on the first try,"]
    return "\n" + spacer() + signoffs[seed] + "\n\nnotifyMe"

#========Send email to self=====================================
def notifyMe(me,msg):
    server =smtplib.SMTP('smtp.gmail.com',587)
    
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(me,emailPass)

    msgToSend = randGreeting() + timeStr() + spacer() + "\t" + msg + randSignOff()
    mimeMsg = MIMEText(msgToSend)

    mimeMsg['Subject'] = "Automated Reminder from notifyMe!"
    mimeMsg['From'] = me
    mimeMsg['To']   = me

    server.sendmail(me, me, mimeMsg.as_string())
    server.quit

