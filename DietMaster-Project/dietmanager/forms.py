from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)

class HealthForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField()
    isMale = forms.BooleanField()
    isnotMale = forms.BooleanField()
    weight = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    height = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    isActive = forms.BooleanField()
    isnotActive = forms.BooleanField()
    isModeratelyActive = forms.BooleanField()