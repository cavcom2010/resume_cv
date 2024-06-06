from django import forms
from .models import Testimonial

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, required=True, widget=forms.TextInput())
    message = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={'placeholder': 'Message required*',
                                                                          'rows':10})
                                                                          )


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'profession','image', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name*'}),
            'profession': forms.TextInput(attrs={'placeholder': 'Profession*'}),
            'text': forms.Textarea(attrs={'placeholder': 'Testimonial*'}),
        }


        labels = {
            'name': 'Name',
            'profession': 'Profession',
            'text': '',
            'image': '',
        }

        # help_texts = {
        #     'name': '',
        #     'profession': '',
        #     'text': '',
        #     'image': '',
        # }
