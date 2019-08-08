import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import os.path
import getpass

def send_mail():

    message =MIMEMultipart()

    mail = smtplib.SMTP('smtp.gmail.com', '587')
    mail.ehlo()
    mail.starttls()
    mail.ehlo()

    subject = input("Enter subject of the mail: ")
    body = input("Enter the body of the mail: ")
    f = int(input("Enter number of files :"))
    print("Enter",f,"file locations: ")
    loc=[]
    for i in range(0,f):
        loc.append(input())

    n = int(input("Enter number of recipients :"))
    print("Enter",n,"email addresses: ")
    to=[]
    for i in range(0,n):
        to.append(input())

    if(n>0):
        email_add = input("Enter your email address: ")
        password = getpass.getpass("Enter password: ")

        message['From'] = email_add
        message['To'] = ", ".join(to)
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        for i in range(0,f):
            # file_name = os.path.basename(loc[i])
            files = open(loc[i], 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(files.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % files)
            message.attach(part)

            count = 0
            while(True):
                try:
                    mail.login(email_add, password)
                    mail.sendmail(
                        email_add,
                        to,
                        message.as_string()
                    )
                    # mail.close()
                    break
    
                except:
                    if(count==3):
                        print("Sorry! Unkown error!")
                        break
                    password = getpass.getpass("Enter correct password for " +email_add+": ")
                    count+=1
send_mail()