from django import forms

class register(form.Form):
    name = forms.CharField(lable='name', max_length=25, required=True)
    mail= forms.EmailField(lable='mail')