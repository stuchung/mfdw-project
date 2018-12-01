from django import forms
from django.forms import ModelForm
from .models import Quote

class QuoteForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Quote
        fields = [
            'name','position','company','address','phone','email','web',
            'description','sitestatus','priority','jobfile'
        ]

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(QuoteForm, self).clean()
        return cleaned_data
