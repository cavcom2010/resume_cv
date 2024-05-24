from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, required=True, widget=forms.TextInput(attrs={'class': 'form-group d-flex flex-column-reverse'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Message required*',
                                                                          'rows':5, 'id':'cf-message'})
                                                                          )
