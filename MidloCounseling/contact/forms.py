from django import forms
from contact.models import Interest, Comment

class InterestForm(forms.ModelForm):

    class Meta():
        model = Interest
        fields = ('title','author','first_name','last_name','text')
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.TextInput(attrs={'size':600,'class':'editable postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('post','responder')

        widgets = {
            'responder':forms.TextInput(attrs={'class':'textinputclass'}),
            'post':forms.TextInput(attrs={'size':600,'class':'editable'})
        }