from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import django.contrib.auth as auth
from mainmodels.models import Profile
from django.urls import reverse
from datetime import datetime

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user_information = "Welcome "+request.user.first_name+request.user.last_name
        isLogin = True
        return render(request, 'mockaccount/index.html', {'isLogin' : isLogin})
    else:
        return render(request, 'mockaccount/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        gender = request.POST.get('gender', 'M')
        profilePicture = request.FILES.get('profilepicture')
        address = request.POST.get('address','')
        birthDate_str = request.POST.get('birthday')
        birthDate = datetime.strptime(birthDate_str, '%Y-%m-%d').date()
        balance = 0.00
        isBan = False
        user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
        user.profile.gender = gender[0]
        user.profile.profilePicture = profilePicture
        user.profile.address = address
        user.profile.birthDate = birthDate
        user.profile.balance = balance
        user.profile.isBan = isBan
        print(user.profile.gender, user.profile.birthDate, user.profile.balance, user.profile.isBan)
        user.save()
        return redirect(reverse('mockaccount:index'))
    else:
        return HttpResponse('Failed to Register')

def login(request):
    if request.method == 'POST':
        username = request.POST['_username']
        password = request.POST['_password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(reverse('mockaccount:index'))
    else: 
        return HttpRespnose('Failed to login')

def profile(request):
    return HttpRespnose('This is a profile page.')

def logout(request):
    auth.logout(request)
    return redirect(reverse('mockaccount:index'))
