from sklearn.linear_model import LinearRegression
import joblib
from django.shortcuts import render
from django.http import *
from .forms import RegisterForm
from .models import HealthModel, StorageModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
import joblib
from sklearn.linear_model import LinearRegression
from .diets import getDiet

lr = joblib.load("caloriemeter.pkl")
# To register the user
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


# Check whether the user is registered and logs him in
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


# To get the health related details and store it in a db 
@login_required(login_url='/login/')
def health(request):
    current_user = request.user

    if request.POST:
        forms = HealthModel()
        current_user = request.user
        forms.username = current_user
        forms.age = request.POST["age"]
        forms.weight = request.POST['weight']
        forms.height = request.POST['height']
        active = request.POST['is_active']
        forms.diseases = request.POST['diseases']
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
            v=HealthModel.objects.get(username=current_user)
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
        v.calories = c
        v.carbs = values[0][0]
        v.proteins = values[0][1]
        v.fats = values[0][2]
        # diet = getDiet(c,v.diseases)[:-1]
        # avoidables = getDiet(c,v.diseases)[-1]
        v.diet = "diet"
        v.save()
        return render(request, "dietmanager/home.html",{"calories":calories[0][0],"carbs":values[0][0],"proteins":values[0][1],"fats":values[0][2],"diet":"diet","avoidable":"avoidables"})
    else:
        try:
            v = HealthModel.objects.get(username=current_user)
            return render(request, "dietmanager/home.html")
        except:
            return render(request, "dietmanager/health1.html")

# To store the changed values of calories each day for a period of 7 days
def store(request):

    user = request.user
    v=HealthModel.objects.get(username=user)
    
    st = StorageModel(username=v)
    if(st is None):
        st = StorageModel()
        st.username = user
        st.save()
    print(st)
    if request.POST:
        if(st.daily_intake1==0):
            st = StorageModel(username=v)
            daily_intake1 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake1 = daily_intake1
            x = (v.calories-daily_intake1)
            v.calories += x
            v.save()
            st.save()
        elif(st.daily_intake2==0):
            daily_intake2 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake2 = daily_intake2
            x = (v.calories-daily_intake2)
            v.calories += x

            v.save()
            st.save()
        elif(st.daily_intake3==0):
            daily_intake3 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake3 = daily_intake3
            x = (v.calories-daily_intake3)
            v.calories += x
            st.save()
            v.save()
        elif(st.daily_intake4==0):
            daily_intake4 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake4 = daily_intake4
            x = (v.calories-daily_intake4)
            v.calories += x
            st.save()
            v.save()
        elif(st.daily_intake5==0):
            daily_intake5 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake5 = daily_intake5
            x = (v.calories-daily_intake5)
            v.calories += x
            st.save()
            v.save()
        elif(st.daily_intake6==0):
            daily_intake6 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake6 = daily_intake6
            x = (v.calories-daily_intake6)
            v.calories += x
            st.save()
            v.save()
        elif(st.daily_intake7==0):
            daily_intake7 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake7 = daily_intake7
            x = (v.calories-daily_intake7)
            v.calories += x
            st.save()
            v.save()
        diet = getDiet(v.calories, v.diseases)
        return render(request, "dietmanager/home.html",{"calories":v.calories,"proteins":v.proteins,"carbs":v.carbs,"fats":v.fats,"diet":diet})
    else:
        return render(request,"dietmanager/response.html")



# On Progress
@login_required(login_url='/login/')
def main(request):
    current_user = request.user
    obj = HealthModel.objects.all()
    return render(request, "dietmanager/home.html", {"user":current_user})

