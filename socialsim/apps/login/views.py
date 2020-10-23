from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.

def error_report(request, errors):
    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request, v)
        return True
    else:
        return False

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def create_user(request):
    if request.method == 'POST':
        errors= User.objects.user_validator(request.POST)
        if error_report(request, errors):
            return redirect('/')
        else:
            password= request.POST['password']
            passhash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], bdate=request.POST['bdate'], password=passhash)
            request.session['current_user'] = new_user.id
            return redirect('/main/title')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['username'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['pword'].encode(), logged_user.password.encode()):
                request.session['current_user'] = logged_user.id
                return redirect('/main/title')
            else:
                messages.error(request, "Your username or password is incorrect")
        else:
            messages.error(request, "Your username or password is incorrect")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')
