from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_check = request.POST['password_check']

        if password == password_check:
            if User.objects.filter(username=username).exists():
                messages.info(request, "帳戶已存在！")
            #elif User.objects.filter(email=email).exists():
            #    messages.info(request, "電子郵件已存在！")
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                print('User Created!')
                return redirect('login')
        else:
            messages.info(request, "密碼不相符！")
        return redirect('register')
    else:
        return render(request, 'accounts/accounts_base.html', {'login_page':False})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "帳號或密碼有誤！")
            return redirect('login')
    else:
        return render(request, 'accounts/accounts_base.html', {'login_page':True})


def logout(request):
    auth.logout(request)
    return redirect('/')
