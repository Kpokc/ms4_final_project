from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import os
import smtplib
from email.message import EmailMessage


EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASS = os.environ.get('EMAIL_HOST_PASS')

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
        msg.set_content('''
        <!DOCTYPE html>
        <html>
            <body>
                <div style="background-color:#eee;padding:10px 20px;text-align:center;">
                    <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">Edible Bouquets</h2>
                </div>
                <div style="padding:20px 0px">
                    <div style="height:500px;width:400px;margin: 0 auto;">
                        <div style="text-align:center;">
                            <h3>Your Query Received.</h3>
                            <p>We appreciate you contacting us {name}.
                            <br> One of our colleagues will get back in touch with you soon! <br> Have a great day!</p>
                            <hr>
                            <h3>{name} Subject:</h3>
                            <p>{subject}</p>
                            <h3>{name} Query:</h3>
                            <p>{message}</p>
                            <h3>Contact details:</h3>
                            <p></p>
                            <a href="https://final-ms4-app.herokuapp.com/">Edible Bouquets</a>
                        </div>
                    </div>
                </div>
            </body>
        </html>
        '''.format(name=name, message=message, subject=subject, email=email), subtype='html')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASS)
            smtp.send_message(msg)

        return redirect(reverse('sent'))

    return render(request, 'contact/contact.html')

def sent(request):
    """ Render Message sent page"""
    return render(request, 'contact/message_sent.html')
