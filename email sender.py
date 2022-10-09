import smtplib as sil
ob=sil.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('pshah9360@gmail.com','wwwaopubapdatfmh')
subject="skdck"
body="i love python"
massage="subject:{}\n\n{}".format(subject,body)
list1=['aaryanshah615@gmail.com',
        'pshah9360@gmail.com']
ob.sendmail('pshah9360@gmail.com',list1,massage)
print("mail send")
ob.quit()