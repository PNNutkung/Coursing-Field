from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'login/login.html')

def login(req):
    """username = req.POST['username']
    password = req.POST['password']"""

    """if username == "admin":
        return render(req, 'login.html')
    else:
        return render(req, 'login/index.html', {
            'error_message': 'Invalid username or password'
        })"""
    return render(req, 'login/login.html', {'error_message': 'Invalid username or password'})
