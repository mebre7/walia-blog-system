from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'd-grid gap-3'
        self.helper.layout = Layout(
            Field('username', css_class='form-control form-control-lg', placeholder='Choose a username'),
            Field('email', css_class='form-control form-control-lg', placeholder='your@email.com'),
            Field('password1', css_class='form-control form-control-lg', placeholder='Create a strong password'),
            Field('password2', css_class='form-control form-control-lg', placeholder='Confirm your password'),
        )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'd-grid gap-3'
        self.helper.layout = Layout(
            Field('username', css_class='form-control form-control-lg', placeholder='Your username'),
            Field('first_name', css_class='form-control form-control-lg', placeholder='First name'),
            Field('last_name', css_class='form-control form-control-lg', placeholder='Last name'),
            Field('email', css_class='form-control form-control-lg', placeholder='you@example.com'),
        )


