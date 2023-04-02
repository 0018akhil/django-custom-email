from django.shortcuts import render, redirect
from django.core.mail import send_mail


def emailSend(request):

    if request.method == 'POST':

        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            '0018akhil@gmail.com',
            ['akhil.achary18@gmail.com'],
            fail_silently=False,
        )

    return redirect('home')


def homeView(request):
    return render(request, 'home.html')
