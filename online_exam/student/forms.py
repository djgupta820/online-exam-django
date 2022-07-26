from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    roll_number = forms.CharField()
    course = forms.CharField()
    semester = forms.IntegerField()
    joined = forms.DateField()
    password = forms.PasswordInput()
    


    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "course", "semester", "joined", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        
        if commit:
            user.save()
        return user
