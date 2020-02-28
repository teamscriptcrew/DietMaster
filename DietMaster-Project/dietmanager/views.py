from sklearn.linear_model import LinearRegression
import joblib
from random import randint
from pandas import DataFrame, read_csv
lr = joblib.load("caloriemeter.pkl")
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

def getDiet(calories):

    # Make this better
    morning=["idli","dosa","puttu","oats","noodles","salad","bread","sandwich","idiyappam","appam","ada","vada"]
    afternoon=["fish","porotta","pork","salad","rice"]
    night=["fish","porotta","pork","noodles","salad","rice"]
    snacks=["pastry","biscuit","fries","chocolate","pasta","vada pav"]
    Drinks=["coffee","tea","milk","shake"]
    others=["curd","yogurt","burger","peanuts"]
    fruits=["banana","apple","grapes","carrots"]
    curry=["sambar","avial","stew"]
    permeal = round(calories)//3
    df = DataFrame(read_csv("foodData.csv"))
    l2 = []
    f1 = []
    f2 = []
    f3 = []
    for j in range(3):
        c = 0
        l = []
        #i = randint(0,100)
        while(permeal>c):
            i = randint(0,100)

            # After editing the csv file, replace the mornings with afternoon and night respectievely at j=1 and j=2
            if(j==0):
                datas = []
                datas.append(df.loc[df['name'].isin(morning)])
                x = randint(0,len(datas[0])-1)
                calories = datas[0].iloc[x]["calories"]
                c += calories
                f1.append(datas[0].iloc[x]["name"])
            elif(j==1):
                datas = []
                datas.append(df.loc[df["name"].isin(morning)])
                x = randint(0,len(datas[0])-1)
                c += datas[0].iloc[x]["calories"]
                f2.append(datas[0].iloc[x]["name"])
            elif(j==2):
                datas = []
                datas.append(df.loc[df["name"].isin(morning)])
                x = randint(0, len(datas[0])-1)
                c += datas[0].iloc[x]["calories"]
                f3.append(datas[0].iloc[x]["name"])
    l2.append(f1)
    l2.append(f2)
    l2.append(f3)
    return l2


@login_required(login_url='/login/')
def health(request):
    current_user = request.user
    try:
        HealthModel.objects.get(username=current_user)
        return render(request, "dietmanager/main.html")
    except:
        pass
    if request.POST:
        forms = HealthModel()
        current_user = request.user
        forms.username = current_user
        forms.age = request.POST["age"]
        forms.weight = request.POST['weight']
        forms.height = request.POST['height']
        active = request.POST['is_active']
        diseases = request.POST['diseases']
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
            v=HealthModel.objects.get(username=current_user)
        except:
            forms.save()
            v = HealthModel.objects.get(username=current_user)
        username=v.username
        age=int(v.age)
        ismale=int(v.isMale==True)
        isfemale=int(v.isFemale==True)
        weight=int(v.weight)
        height=int(v.height)
        isactive=int(v.isActive==True)
        isnotactive=int(v.isnotActive==True)
        ismoderate=int(v.isModeratelyActive==True)
        lib=[age,ismale,isfemale,height, weight, isactive, isnotactive, ismoderate,0,0,0]
        calories = lr.predict([lib])
        l2 = joblib.load("calories_to_nutrients.pkl")
        values = l2.predict(calories)
        c = calories[0][0]
        diet = getDiet(c)
        return render(request, "dietmanager/home.html",{"calories":calories[0][0],"carbs":values[0][0],"proteins":values[0][1],"fats":values[0][2],"diet":diet})
    else:
        return render(request, "dietmanager/health1.html")
345.40499046046205
def store(request,user="new"):
    pass


@login_required(login_url='/login/')
def main(request):
    current_user = request.user
    obj = HealthModel.objects.all()
    return render(request, "dietmanager/home.html", {"user":current_user})
