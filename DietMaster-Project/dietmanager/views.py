from sklearn.linear_model import LinearRegression
import joblib
from random import randint
from pandas import DataFrame, read_csv
lr = joblib.load("caloriemeter.pkl")
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

def getDiet(calories,diseases):
    snacks=["Kuzhalappam","pastry","biscuit","fries","chocolate","pasta","vada pav","sandwich","noodles","Chicken Shawarma","Cheese Pizza","Pizza","Coconut Pudding","Tapioca Pudding","Vanilla Pudding","Chocolate Pudding","Cornbread Pudding"]
    Drinks=["coffee","tea","milk","shake","Apple Juice","Pineapple Juice","Orange Juice"]
    others=["curd","yogurt","burger","peanuts"]
    fruits=["banana","apple","grapes","carrots","Watermelon"]
    curry=["ayala curry","Matthi curry","Vegetable Khurma","Boiled Eggs","Vegetable Khurma","Gobi Manchurian","Gobi Fry","Butter Chicken","Pepper Chicken","Gobi Chicken","Crab Curry","Payar Curry","Cheese Paneer","Mango Pickle","Coconut Chutney","Kadala Curry","Egg Curry","Baby Spinach","Tomato","fish","sambar","avial","stew","pork","Aloo Gobi","Gobi Curry","Beef Curry","Paneer Curry","Fish Curry","Prawn Curry","Sweet Peas"]

    permeal = calories/3
    df = DataFrame(read_csv("foodData.csv"))
    l2 = []
    f1 = []
    f2 = []
    f3 = []
    f4 = []

    cholesterol=["cheese","burger","egg yolk","butter","chicken","cheese","ice cream"]
    thyroid=["raw cabbage","raw cauliflower","gluten containing foods","junk foods","high- sugar","green-tea"]
    diabetes=["sugar","oil,coconut(in moderation)","fried foods","mutton","parottas","snacks","soft drinks","egg yolk","salt(inlimit)","honey","dried fruits","mangoes","jackfruits"]
    pcos=["biscuits","cakes","bread","dried fruits","ice cream","yogurt","soda","milk","cheese","butter","soy products","caffeine"]
    hypertension=["maida","bread","noodles","pizza","burgers","chocolate","cakes","chips","coconut","milk","butter","achar"]

    if(diseases=="Cholesterol"):
        f4.append(cholesterol)
    elif(diseases=="Thyroid"):
        f4.append(thyroid)
    elif(diseases=="Diabetes"):
        f4.append(diabetes)
    elif (diseases == "PCOS"):
        f4.append(pcos)
    elif (diseases == "Hypertension" ):
        f4.append(hypertension)
    else:
        f4.append('')   
    def morn(permeal):
        morning=["Brown Bread","Kai pathiri","Malabar nice pathiri","Ada Dosa","Wheat Ada","Rice Rotti","Potato Rotti","idli","dosa","puttu","oats","salad","bread","idiyappam","appam","ada","vada","Poori","Methi Poori","Gobi Paratha"]
        df = DataFrame(read_csv("foodData.csv"))
        datas = []
        datas.append(df.loc[df['name'].isin(morning)])
        x = randint(0,len(datas[0])-1)
        calories = datas[0].iloc[x]["calories"]
        name = (datas[0].iloc[x]["name"])
        c1 = calories
        count = -1
        while( c1 <= permeal):
            c1 += calories
            count+=1
        ccurry = curry[randint(0,len(curry)-1)]
        f1 = {"name":name, "count":count+1 ,"curry":ccurry}
        return f1
    def aftern(permeal):
        afternoon=["Cucumber Salad","Tomato Salad","Spinach Salad","Fresh fruit salad","Porotta","salad","rice","chappati","Chicken Biriyani","Beef Biriyani","Mutton Biriyani","Vegetable Biriyani"]
        df = DataFrame(read_csv("foodData.csv"))
        datas = []
        datas.append(df.loc[df['name'].isin(afternoon)])
        x = randint(0,len(datas[0])-1)
        calories = datas[0].iloc[x]["calories"]
        name = (datas[0].iloc[x]["name"])
        c1 = calories
        count = -1
        while( c1 <= permeal):
            c1 += calories
            count+=1
        ccurry = curry[randint(0,len(curry)-1)]
        f1 = {"name":name, "count":count+1 ,"curry":ccurry}
        return f1
    def night(permeal):
        night=["Brown Bread","Cucumber Salad","Tomato Salad","Spinach Salad","Fresh fruit salad","Kai pathiri","Malabar nice pathiri","Rice Rotti","Potato Rotti","rice","pathiri","dosa","porotta","salad","rice","chappati","Chicken Biriyani","Beef Biriyani","Mutton Biriyani","Vegetable Biriyani","Poori","Methi Poori","Gobi Paratha"]
        df = DataFrame(read_csv("foodData.csv"))
        datas = []
        datas.append(df.loc[df['name'].isin(night)])
        x = randint(0,len(datas[0])-1)
        calories = datas[0].iloc[x]["calories"]
        name = (datas[0].iloc[x]["name"])
        c1 = calories
        count = -1
        while( c1 <= permeal):
            c1 += calories
            count+=1
        ccurry = curry[randint(0,len(curry)-1)]
        f1 = {"name":name, "count":count+1 ,"curry":ccurry}
        return f1

    f1 = morn(permeal)
    f2 = aftern(permeal)
    f3 = night(permeal)

    l2.append(f1)
    l2.append(f2)
    l2.append(f3)
    l2.append(f4)

    return l2



@login_required(login_url='/login/')
def health(request):
    current_user = request.user
    try:
        HealthModel.objects.get(username=current_user)
        return render(request, "dietmanager/home.html")
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
        global c
        calories = lr.predict([lib])
        l2 = joblib.load("calories_to_nutrients.pkl")
        values = l2.predict(calories)
        c = calories[0][0]
        v.calories = c
        v.carbs = values[0][0]
        v.proteins = values[0][1]
        v.fats = values[0][2]
        print(v.diseases)
        diet = getDiet(c,v.diseases)[:-1]
        avoidables = getDiet(c,v.diseases)[-1]
        v.diet = diet
        v.save()
        return render(request, "dietmanager/home.html",{"calories":calories[0][0],"carbs":values[0][0],"proteins":values[0][1],"fats":values[0][2],"diet":diet,"avoidable":avoidables})
    else:
        current_user = request.user
        try:
            v = HealthModel.objects.get(username=current_user)
            return render(request, "dietmanager/home.html",{"calories":v.calories,"carbs":v.carbs,"proteins":v.proteins,"fats":v.fats,"diet":v.diet})
        except:
            return render(request, "dietmanager/health1.html")

def store(request):

    user = request.user
    v=HealthModel.objects.get(username=user)
    
    st = StorageModel(username=user)
    if(st is None):
        st = StorageModel()
        st.username = user
        st.save()
    print(st)
    if request.POST:
        if(st.daily_intake1==0):
            st = StorageModel(username=user)
            daily_intake1 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake1 = daily_intake1
            v.calories += (v.calories-daily_intake1)
            v.save()
            st.save()
        elif(st.daily_intake2==0):
            daily_intake2 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake2 = daily_intake2
            v.calories += (v.calories-daily_intake2)
            v.save()
            st.save()
        elif(st.daily_intake3==0):
            daily_intake3 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake3 = daily_intake3
            v.calories += (v.calories-daily_intake3)
            st.save()
            v.save()
        elif(st.daily_intake4==0):
            daily_intake4 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake4 = daily_intake4
            v.calories += (v.calories-daily_intake4)
            st.save()
            v.save()
        elif(st.daily_intake5==0):
            daily_intake5 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake5 = daily_intake5
            v.calories += (v.calories-daily_intake5)
            st.save()
            v.save()
        elif(st.daily_intake6==0):
            daily_intake6 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake6 = daily_intake6
            v.calories += (v.calories-daily_intake6)
            st.save()
            v.save()
        elif(st.daily_intake7==0):
            daily_intake7 = int(request.POST['breakfast']) + int(request.POST["lunch"]) + int(request.POST["dinner"])
            st.daily_intake7 = daily_intake7
            v.calories += (v.calories-daily_intake7)
            st.save()
            v.save()
        return render(request, "dietmanager/home.html",{"calories":v.calories,"proteins":v.proteins,"carbs":v.carbs,"fats":v.fats})
    else:
        return render(request,"dietmanager/response.html")



@login_required(login_url='/login/')
def main(request):
    current_user = request.user
    obj = HealthModel.objects.all()
    return render(request, "dietmanager/home.html", {"user":current_user})

