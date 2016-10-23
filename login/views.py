from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'login/login.html')

def login(req):
    username = req.POST['username']
    password = req.POST['password']

    """if username == "admin":
        return render(req, 'login.html')
    else:
        return render(req, 'login/login.html', { 'error_message': 'Invalid username or password'})"""

def register(req):
    return render(req, 'login/register.html')

def create_new_user(req):
    firstname = req.POST['firstname']
    lastname = req.POST['lastname']
    username = req.POST['username']
    password = req.POST['password']
    confirm_password = req.POST['confirm_password']
    bday = req.POST['bday']
    gender = req.POST['gender']
    user = None
    return render(req, 'login/login.html', {
        'error_message': 'Register successfully.'
    })
    """
    try:
        user = User.objects.get(username=username)
    except(User.DoesNotExist):
        if user is not None:
            return render(req, 'login/register.html', {
                'error_message': 'This username has already taken.'
            })
        elif password != confirm_password:
            return render(req, 'login/register.html', {
                'error_message': 'Your password is not match.'
            })
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return render(req, 'login/register.html', {
                'error_message': 'Your email is not valid.'
            })
        else:
            user = User.objects.create_user(username, email=email, password=password, first_name=firstname, last_name=lastname)
            return render(req, 'login/index.html', {
                'error_message': 'Register successfully.'
            })"""
