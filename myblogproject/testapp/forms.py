from django import forms
from django.contrib.auth.models import  User
# for sample
class sharebyemail(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

from testapp.models import comments
class commentsform(forms.ModelForm):
    class Meta:
        model=comments
        fields=('name','email','body')

class signupform(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
