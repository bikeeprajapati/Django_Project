from django import forms

class userForm(forms.Form):
    num1=forms.CharField(label="value1")
    num2= forms.CharField(label="value2")