from django import forms
from django.forms import ModelForm
from .models import *


class QueryForm(ModelForm):
    full_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Full Name', 'size': 40}))
    email = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Email', 'size': 40}))
    phoneNumber = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Number', 'size': 40}))
    message = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Tell Us About Your Query And We Will Call You Back', 'cols': 42, 'row': 20}))

    class Meta:
        model = Query
        fields = "__all__"


class HomeQuery(ModelForm):
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Email'}))

    class Meta:
        model = HomeQuery
        fields = "__all__"
