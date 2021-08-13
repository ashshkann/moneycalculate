from django import forms

class Login_form(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Input Your Username', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': 'Input Your Password', 'class': 'form-control'})
    )