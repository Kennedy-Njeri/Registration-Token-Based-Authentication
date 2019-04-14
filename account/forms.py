from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order






class SignupForm(UserCreationForm):

    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def clean_email(self):
            data = self.cleaned_data['email']
            if User.objects.filter(email=data).count() > 0:
                raise forms.ValidationError("We have a user with this user email-id")
            return data




class OrderCreateForm(forms.ModelForm):

    class Meta:

        model = Order

        exclude = ('user',)

        fields = ['topic', 'instructions', 'urgency', 'pages', 'email']