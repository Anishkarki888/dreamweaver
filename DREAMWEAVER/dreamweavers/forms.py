from django import forms

class userForms(forms.Form):
    name=forms.CharField()
    reason=forms.CharField()
    email=forms.CharField()
    phone=forms.CharField()