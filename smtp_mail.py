import smtplib

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('Sender mail','Mail Password')
    subject = "Test Mail From Raspberry Pi"
    body = "Hey! If you recieve this mail your code works fine."
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'Sender mail',
        'reciever Mail',
        msg
        )
    print("The Email has sent!!")
    server.quit
send_mail()    

