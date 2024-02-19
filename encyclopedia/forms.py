from django import forms

class entryform(forms.Form):
    title=forms.CharField(label='Title of page')
    content=forms.CharField(label='Contents of page',widget=forms.Textarea())


