from django.shortcuts import render
from django.http import *
from .forms import RegisterForm
from .models import HealthModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
import joblib
from sklearn.linear_model import LinearRegression
def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'dietmanager/register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': forformsm,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/login/')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})


def login_user(request, message=""):
	logout(request)
	username = ''
	password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/health/')
			else:
				print("Not active user")
		else:request, "dietmanager/health.html"
	return render(request, 'dietmanager/login.html', {message:"No such user found"})

@login_required(login_url='/login/')
def health(request):
    try:
        HealthModel.objects.get(username=current_user)
    except:
        return render(request, "dietmanager/home.html")
    if request.POST:
        forms = HealthModel()
        current_user = request.user
        forms.username = current_user
        forms.age = request.POST["age"]
        forms.weight = request.POST['weight']
        forms.height = request.POST['height']
        active = request.POST['is_active']
        if(active=="Very_Active"):
            forms.isActive = True
            forms.isnotActive = False
            forms.isModeratelyActive = False
        elif(active=="Moderately_Active"):
            forms.isActive = False
            forms.isnotActive = False
            forms.isModeratelyActive = True
        else:
            forms.isActive = False
            forms.isnotActive = True
            forms.isModeratelyActive = False
        gender = request.POST["gender"]
        if(gender=="Male"):
            forms.isMale = True
            forms.isFemale = False
        else:
            forms.isMale = False
            forms.isFemale = True
        try:
            HealthModel.objects.get(username=current_user)
        except:
            forms.save()
        else:
            pass
        print(forms)
        return render(request, "dietmanager/home.html")
    else:
        return render(request, "dietmanager/health1.html")

def store(request,user="new"):
    print("HI")
    
    

@login_required(login_url='/login/')
def main(request):
    current_user = request.user
    obj = HealthModel.objects.all()
    print(obj.username)
    return render(request, "dietmanager/home.html", {"user":current_user})