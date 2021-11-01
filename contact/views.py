from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import os
import smtplib
from email.message import EmailMessage


EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def contact(request):
    """ Send email to customer and to site owner """

    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        msg = EmailMessage()
        msg['Subject'] = 'Edible Bouquets query'
        msg['From'] = 'EdibleBouquets@gmail.com' 
        msg['To'] = [request.POST['email'], EMAIL_ADDRESS]
        msg.set_content('''
        <!DOCTYPE html>
        <html>
            <body>
                <div style="background-color:#eee;padding:10px 20px;text-align: center;">
                    <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">Edible Bouquets</h2>
                </div>
                <div style="padding:20px 0px">
                    <div style="height:500px;width:400px;margin: 0 auto;">
                        <div style="text-align:center;">
                            <h3>Your Query Received.</h3>
                            <p>We appreciate you contacting us {name}. 
                            <br> One of our colleagues will get back in touch with you soon! <br> Have a great day!</p>
                            <h3>Your query:</h3>
                            <p>{message}</p>
                            <a href="#">Edible Bouquets</a>
                        </div>
                    </div>
                </div>
            </body>
        </html>
        '''.format(name=name, message=message), subtype='html')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
            smtp.send_message(msg)
        
        #return render(request, 'contact/message_sent.html')
        return redirect(reverse('sent'))

    return render(request, 'contact/contact.html')

def sent(request):
    """ Render Message sent page"""
    return render(request, 'contact/message_sent.html')
