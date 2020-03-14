from django import forms
from django.contrib.auth.models import User
from mammoth.models import UserProfile, Pattern

class PatternForm(forms.ModelForm):

    title = forms.CharField(max_length=Pattern.TITLE_MAX_LENGTH)

    class Meta:
        model = Pattern
        fields = ('title', 'picture','description',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)