__author__ = 'ayost'

import sys
import smtplib
from email.mime.text import MIMEText


def main():
    me = "You@gmail.com"
    to = ["toaddresses@gmail.com","other_recipients@sample.com"]
    if len(sys.argv) < 3:
        print("INCORRECT USAGE!")
        print("Correct Usage:")
        print("\t python emailSender messageContents.txt \"Subject\"")
        exit(-1)
    fp = open(sys.argv[1])
    contents = fp.read()
    fp.close()
    contents += '<h2>Signature Block</h2><p style="font-family: Courier, Courier New;">-<i>Fill in your stylized signature here</i></p>'
    msg = MIMEText(contents, 'html', 'utf8')
    msg['To'] = ",".join(to)
    msg['Subject'] = sys.argv[2]
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login('google user name', 'google pass word')
    server.sendmail(me, to, msg.as_string())
    server.close()

if __name__ == '__main__':
    main()
