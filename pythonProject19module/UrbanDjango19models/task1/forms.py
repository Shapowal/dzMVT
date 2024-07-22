from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='повторите пароль', widget=forms.PasswordInput)
    age = forms.IntegerField(label='возраст')