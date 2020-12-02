import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def ConfirmationEmail(Receiver):
    sender_email = "mikasitesowner@gmail.com"
    receiver_email = Receiver
    password = "icantremembermypassword123"
    port = 465
    
    confirmationCode = get_random_string(8)
    message = MIMEMultipart("alternative")
    message["Subject"] = "Verification Code"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
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
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    Verification = input("We have sent an email on adress : {} \nPlease Enter the code you will find in this email: ".format(Receiver))
    if Verification == confirmationCode:
        Verify = 1
    else:
        Verify = 0
    return Verify