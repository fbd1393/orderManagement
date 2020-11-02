from django.contrib.auth.models import auth, User
from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.


def register(request):

    if request.method == 'POST':
        # print('method is post')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username is taken!')
                messages.info(request, 'username is taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('this email is exist already')
                messages.info(request, 'this email is exist already')
                return redirect('register')
            elif username == '' or first_name == '' or last_name == '' or password1 == '' or password2 == '' or email == '':
                print('You have to complete all the fields')
                messages.info(request, 'You have to complete all the fields')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password1,
                    email=email)
                user.save()
                print('User is created successfully')
        else:
            print('passwords are not match')
            messages.info(request, 'passwords are not match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        # print('this a login page. with post method.')
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            print('The user is exist!')
            auth.login(request, user)
            return redirect('/')
        else:
            print('username or password is wrong!')
            messages.info(request, 'username or password is wrong!')
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
