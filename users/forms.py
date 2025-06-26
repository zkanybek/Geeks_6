from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=3, required=True, widget=forms.PasswordInput())
    password_confirm = forms.CharField(min_length=3, required=True, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, required=True)
    password = forms.CharField(min_length=3, required=True, widget=forms.PasswordInput())

    # Раскомментируйте, если хотите проверять наличие пользователя здесь:
    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get("username")
    #     if not User.objects.filter(username=username).exists():
    #         raise forms.ValidationError("User does not exist")
    #     return cleaned_data
