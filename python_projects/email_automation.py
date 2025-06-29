import smtplib

to =input("Enter the Email:- ")

message = input("Enter the message:- ")

def sendEmail(to,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('krishanpaltu1998@gmail.com','ccrsyyhuaqhhwkmd') 
    server.sendmail('krishanpaltu1998@gmail.com', to , message)
    server.close()

sendEmail(to,message)