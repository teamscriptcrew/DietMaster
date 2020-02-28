from django.shortcuts import render
from django.http import *
from .forms import RegisterForm, HealthForm
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
                    'form': form,
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
	return render(request, "dietmanager/health.html")

def store(request,user="new"):
    if request.POST:
        forms = HealthForm()

        forms.username = user.name
        forms.age = request.POST["age"]
        forms.weight = request.POST['weight']
        forms.height = request.POST['height']
        forms.is_active = request.POST['is_active']
        forms.is_not_active = request.POST['is_not_active']
        forms.is_modetately_active = request.POST['is_moderately_active']
        forms.is_male = request.POST['is_male']
        forms.is_female = request.POST['is_female']
        forms.save()
        print(forms)
    else:
        return render(request, "dietmanager/health.html")
    return render(request, "dietmanager/main.html")


@login_required(login_url='/login/')
def main(request):
	return render(request, "dietmanager/main.html")