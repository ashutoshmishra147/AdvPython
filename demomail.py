# This Python file uses the following encoding: utf-8


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    #Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
     #server_ssl=smtplib.SMTP_SSL("smtp.gmail.com",465)
     server_ssl.ehlo()
     server_ssl.login(gmail_user, gmail_pwd)
     #ssl server doesn't support or need tls, so don't call server_ssl.starttls()
     server_ssl.sendmail(FROM, TO, message)
     #server_ssl.quit()
     server_ssl.close()
     print ('successfully sent the mail')
    except:
     print ("failed to send mail")
	
send_email('ashutosh147@gmail.com',"mer1sh0nul1",'mishrashutosh147@gmail.com',"HI","testing")	