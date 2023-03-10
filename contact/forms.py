from django import forms

class ContactForm(forms.Form):
    choices = ([1, 'Suggestion'], [2, 'Complaint'])
    name = forms.CharField(max_length = 30, widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder': 'Username'
    }))
    email = forms.CharField(max_length = 30, widget = forms.EmailInput(attrs = {
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    subject = forms.ChoiceField(choices = choices, widget = forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'subject'
    }))
    messages = forms.CharField(widget = forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Messages'
    }))