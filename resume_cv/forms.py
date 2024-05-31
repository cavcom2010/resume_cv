from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, required=True, widget=forms.TextInput())
    message = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={'placeholder': 'Message required*',
                                                                          'rows':10})
                                                                          )
