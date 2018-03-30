import smtplib

content='sending email through python'
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('gurunadh4b2@gmail.com','udaychanti')
mail.sendmail('gurunadh4b2@gmail.com','gurunadh.4b@gmail.com',content)
print('Ok sent successfully') 
mail.close()

