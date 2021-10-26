from django import forms
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50, label="Istifadeci adi")
    password=forms.CharField(max_length=50, label="Parol", widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=50, label="Parolu tesdiqleyin", widget=forms.PasswordInput)
def clean(self):
    username = self.cleaned_data.get("username")
    password = self.cleaned_data.get("password")
    confirm = self.cleaned_data.get("confirm")
    if password and confirm and password != confirm:
        raise forms.ValidationError("Parollar uygun gelmir")
    values = {
        "username": username,
        "password": password
    }
    return values
class LoginForm(forms.Form):
    username=forms.CharField(label="istifadeci adi")
    password=forms.CharField(label="Parol", widget=forms.PasswordInput)
