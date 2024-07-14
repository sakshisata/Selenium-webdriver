

from django.core.mail import EmailMessage

def send_email_with_attachment(email_subject, to_email, cc_email, attachment_path):
    email = EmailMessage(subject=email_subject, body='Please find attached the file.', to=[to_email], cc=[cc_email])
    email.attach_file(attachment_path)
    email.send()
