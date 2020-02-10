#! python3

import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()

conn.starttls()

conn.login('sender@gmail.com', 'password')

conn.sendmail('sender@gmail.com', 'receiver@gmail.com', 'Subject: python with email\n\n Dear Cuong,\n This is the email send by python. \n\n -CNV')

conn.quit()