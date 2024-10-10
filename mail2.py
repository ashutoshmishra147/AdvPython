import smtplib

fromadd='ashutosh147@gmail.com'
toadd='arti147@gmail.com'

msg='''hi,how r u'''
username='ashutosh147@gmail'
passwd='mer1sh0nul1'
try:
 server = smtplib.SMTP('smtp.gmail.com:587')
 server.ehlo()
 server.starttls()
 server.login(username,passwd)
 server.sendmail(fromadd,toadd,msg)
 print("Mail Send Successfully")
 server.quit()

except:
 print("Error:unable to send mail")
 
 #NOTE:https://www.google.com/settings/security/lesssecureapps that 