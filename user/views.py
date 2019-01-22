from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from user.form import UserRegisterForm
from user.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'back/register.html')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['password'])
            User.objects.create(username=username, password=password)
            return HttpResponseRedirect(reverse('user:login'))
        else:
            errors = form.errors
            return render(request, 'back/register.html', {'errors': errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'back/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = User.objects.filter(username=username).first()
        if check_password(password, user.password):
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('back:index'))
        else:
            msg = '账号或密码错误'
            return render(request, 'back/login.html', {'msg': msg})
