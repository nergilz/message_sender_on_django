from django.shortcuts import render
from django.contrib import auth
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from mainapp.models import Message_db


def main_views(request):
    return render(request, 'index.html')

def message_views(request):
    return render(request, 'message.html')

def reg_views(request):
    return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/message')
        else:
            return render(request, 'index.html', {'username': username, 'errors': True})
    raise Http404

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def send_email(request):
    to_email = request.POST.get('email', '')
    message = request.POST.get('message', '')
    from_email = '' # make your email adress
    mail = Message_db()
    mail.msg_message = message
    mail.msg_email = to_email
    if message == '':
        message = ' '
    if message and to_email:
        try:
            send_mail("Fogstream_test_message", message, from_email, [to_email], fail_silently=False)
            mail.msg_status = True
            mail.save()
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return render(request, 'message.html', {'messages':True})

def registration(request):
    if request.method == 'POST':
        errors = {}
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        if password != password2:
            errors['password'] = 'несовпадение паролей'
        user = User(username=username, email=email)
        user.set_password(password)
        try:
            user.validate_unique()
        except ValidationError:
            errors['username'] = 'пользователь с таким логином уже существует'
        if errors:
            return render(request, 'registration.html', {'reg_errors': errors})
        user.save()
        return HttpResponseRedirect('/')
    return render(request, 'registration.html')
