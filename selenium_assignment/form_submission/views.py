

from django.shortcuts import render
from .email_utils import send_email_with_attachment

def send_email_view(request):
    if request.method == 'POST':
       
        attachment_path = '/Users/apple/Downloads/selenium.pdf'

       
        email_subject = 'Assignment Submission'
        to_email = 'tech@themedius.ai'
        cc_email = 'hr@themedius.ai'

     
        send_email_with_attachment(email_subject, to_email, cc_email, attachment_path)

        
   




