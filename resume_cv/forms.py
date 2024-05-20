from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, required=True, max_length=250)
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control'}))
    