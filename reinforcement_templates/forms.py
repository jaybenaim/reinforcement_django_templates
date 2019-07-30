from django import forms 

class newForm(forms.Form):
    email = forms.CharField(label="email", max_length=255)
    username = forms.CharField(label="username", max_length=255)
    pin = forms.CharField(label="pin", max_length=255)
    website = forms.CharField(label="website", max_length=255)
    address = forms.CharField(label="address", max_length=255)
    alias = forms.CharField(label="alias", max_length=255)
    
    