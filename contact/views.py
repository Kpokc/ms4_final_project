import os
import smtplib
from email.message import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, reverse


EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')


def contact(request):
    """ Send email to customer and to site owner """

    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        msg = EmailMessage()
        msg['Subject'] = 'Edible Bouquets query'
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = [request.POST['email'], EMAIL_HOST_USER]

        context = {
            'name': name,
            'subject': subject,
            'message': message,
            'email': email,
        }

        msg_html = render_to_string(
            'contact/contact_email.html', {'context': context})

        msg.set_content(msg_html, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            smtp.send_message(msg)

    return render(request, 'contact/contact.html')


def sent(request):
    """ Render Message sent page"""
    return render(request, 'contact/message_sent.html')
