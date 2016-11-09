from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import django.contrib.auth as auth
from mainmodels.models import Profile, Course, Category, Transaction
from django.urls import reverse
from datetime import datetime
import json

# Create your views here.
def login(req):
    if req.user.is_authenticated:
        return redirect(reverse('index:index'))
    if req.method == 'POST':
        username = req.POST['_username']
        password = req.POST['_password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect(reverse('browse:browseIndex'))
        else:
            return render(req, 'account/login.html', {'pageTitle': 'Login', 'message': 'Wrong Username or Password.'})
    else:
        return render(req, 'account/login.html', {'pageTitle': 'Login'})

def register(req):
    if req.method == 'POST':
        try:
            username = req.POST['username']
            password = req.POST['password']
            firstname = req.POST.get('firstname')
            lastname = req.POST.get('lastname')
            email = req.POST.get('email')
            gender = req.POST.get('gender', 'M')
            profilePicture = req.FILES.get('profilepicture')
            birthDate_str = req.POST.get('birthday')
            birthDate = datetime.strptime(birthDate_str, '%Y-%m-%d').date()
            user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
            user.profile.gender = gender[0]
            user.profile.profilePicture = profilePicture
            user.profile.birthDate = birthDate
            user.save()
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(req, user)
                return redirect(reverse('account:profile'))
        except IntegrityError:
            return render(req, 'account/register.html', {'message': 'This username has  already taken.'})
    else:
        return render(req, 'account/register.html')

def profile(req):
    if not req.user.is_authenticated:
        return redirect(reverse('account:login'))
    teachingCourses = Course.objects.filter(owner=req.user)
    findTakingCourses = Transaction.objects.filter(takerID=req.user.id)
    takingCourses = []
    for course in findTakingCourses:
        joinCourse = Course.objects.filter(courseID=course.courseID)
        takingCourses.append(joinCourse)
    return render(req, 'account/profile.html', {'teachingCourses': teachingCourses, 'takingCourses': takingCourses})

def personalUpdate(req):
    user = User.objects.filter(username=req.user, email=req.user.email)
    profile = Profile.objects.filter(user=req.user)
    if user is not None and profile is not None:
        birthDate_str = req.POST.get('bday')
        birthDate = datetime.strptime(birthDate_str, '%Y-%m-%d').date()
        gender = req.POST.get('gender', 'M')
        user.update(first_name=req.POST.get('firstname', ''), last_name=req.POST.get('lastname', ''))
        profile.update(birthDate=birthDate, gender=gender[0], address=req.POST.get('address', ''), bio=req.POST.get('biography', ''))
        return redirect(reverse('account:profile'))
    else:
        return json.dumps({'message': '403 Forbidden'})

def profileUpdate(req):
    user = User.objects.get(username=req.user)
    if user is not None:
        user.email = req.POST.get('email', '')
        user.set_password(req.POST.get('password',''))
        user.save()
        return redirect(reverse('account:login'))
    else:
        return json.dumps({'message': '403 Forbidden'})

def updateProfilePicture(req):
    user = User.objects.get(username=req.user)
    if user is not None:
        profilePic = req.FILES.get('profilePicture','')
        if profilePic:
            user.profile.profilePicture = profilePic
            user.save()
        return redirect(reverse('account:profile'))
    else:
        return json.dumps({'message': '403 Forbidden'})

def logout(req):
    auth.logout(req)
    return redirect(reverse('index:index'))
