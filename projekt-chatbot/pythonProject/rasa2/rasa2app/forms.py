from django.forms import ModelForm
from django import forms
from .models import Question

class SendForm(ModelForm):
    q_text = forms.CharField(label="Twoja wiadomość:")
    class Meta:
        model = Question
        fields = ['q_text']
