"""
    EmailSender module:
        Sending Confirmation Emails with SMTP 
        
        Emails Contains :
            -A Hello User text.
            -Dataverse icon and info
            -A verification Code that need to type during registration in order
            to register.
        
        Type of supported emails :
            - "hotmail.com" , "live.com" , "gmail.com" , "yahoo.com"
"""

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
import base64

port = 465
host = "smtp.gmail.com"



def get_random_string(length):
    """
        Verification Code Maker
        -Input : Number
        -Output : Random string with length equal to Number
        
    """
    
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    
    return result_str



def Configuration(Receiver_Email):
    
    if (Receiver_Email[-11:]== "hotmail.com" or 
        Receiver_Email[-8:]=="live.com" or 
        Receiver_Email[-10:]== "hotmail.gr" or 
        Receiver_Email[-7:]=="live.gr" ):
        
        host = "smtp-mail.outlook.com"
        port = 587
        
    elif (Receiver_Email[-9:]== "yahoo.com" or 
          Receiver_Email[-8:]== "yahoo.gr"):
        
        host = "smtp.mail.yahoo.com"
        port = 465
        
    elif(Receiver_Email[-9:]== "gmail.com" or 
         Receiver_Email[-8:]== "gmail.gr"):
        
        port = 465
        host = "smtp.gmail.com"
        
    else:
        print("Sorry we dont support this type of email")
        
        

def ConfirmationEmail(Receiver):
    """
        -Input : Receiver Email
        -Output : A verify var 
                    - 0 ===> Wrong Code Entry
                    - 1 ===> Verification completed Successfully
    """
    
    sender_email = "mikasitesowner@gmail.com"
    receiver_email = Receiver
    password = base64.b64decode("aWNhbnRyZW1lbWJlcm15cGFzc3dvcmQxMjM=").decode("utf-8")
    
    Configuration(Receiver)
    
    confirmationCode = get_random_string(8)
    message = MIMEMultipart("alternative")
    message["Subject"] = "Verification Code"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # Create the plain-text and HTML version of your message
    text = """\
    Hi User,
    Your Confirmation Code is {}""".format(confirmationCode)
    html = """\
    <html>
      <body>
        <p>Hi User,<br>
           Your Confirmation Code is :<br>
           {}
        </p>
      </body>
    </html>
    """.format(confirmationCode)
    
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        
        server.login(sender_email, password)
        server.sendmail(sender_email, 
                        receiver_email, 
                        message.as_string()
        )
    #Get Verification Code
    Verification = input("We have sent an email on adress : {} \n \
                         Please Enter the code \
                         you will find in this email: ".format(Receiver))
    
    if Verification == confirmationCode:
        Verify = 1
    else:
        Verify = 0
    return Verify