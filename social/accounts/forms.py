from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
    def clean_username(self):
        username = self.cleaned_data.get('username')

        for char in username:
            if char in "@#$":
                raise forms.ValidationError("Username shouldn't contain this symbols: '@' '#' or '$'")

        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and not email.endswith("gmail.com"):
            raise forms.ValidationError("Email should end with 'gmail.com'")

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if password and len(password) < 8:
            raise forms.ValidationError('Password should contain at least 8 character')

        return password

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'age', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }