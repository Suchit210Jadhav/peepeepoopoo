# import time
import smtplib
import getpass

def send_mail():

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()

    subject = input("Enter subject of the mail: ")
    body = input("Enter the body of the mail: ")

    message = f"Subject: {subject}\n\n{body}"

    n = int(input("Enter number of recipients :"))
    print("Enter",n,"email addresses: ")
    to=[]
    for i in range(0,n):
        to.append(input())
    if(n>0):
        email_add = input("Enter your email address: ")
        password = getpass.getpass("Enter password: ")

        while(True):
            try:
                mail.login(email_add, password)
                mail.sendmail(
                    email_add,
                    to,
                    message
                )
                break

            except:
                password = getpass.getpass("Enter correct password for " +email_add+": ")

send_mail()