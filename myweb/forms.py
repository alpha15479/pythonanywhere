from django.forms import ModelForm
from django import forms
from myweb.models import Comment

class MyCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'text', 'notes']


searchchoices = (
        (1 ,'name'),
    )

class SearchForm(forms.Form):


    SearchBy = forms.ChoiceField(choices=searchchoices)
    keyword = forms.CharField(max_length=100)