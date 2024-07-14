

from django.core.mail import EmailMessage

def send_email_with_attachment(email_subject, to_email, cc_email, attachment_path):
    email = EmailMessage(subject=email_subject, body='https://github.com/sakshisata/Selenium-webdriver Please find attached the file In this above github i had uploaded the rerquired source code and all the documentation ', to=[to_email], cc=[cc_email])
    email.attach_file(attachment_path)
    email.send()
