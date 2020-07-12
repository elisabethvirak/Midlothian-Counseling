from django import forms
from contact.models import Interest, Comment

class InterestForm(forms.ModelForm):

    class Meta():
        # first_name = forms.CharField(max_length = 200)
        # last_name = forms.CharField(max_length = 200)
        # phone = forms.CharField(max_length = 10)
        # email = forms.EmailField(max_length = 200)
        # text = forms.CharField(widget=forms.Textarea)
        # subject = forms.CharField(max_length=100)
        # message = forms.CharField(widget=forms.Textarea)
        # sender = forms.EmailField()
        # cc_myself = forms.BooleanField(required=False)
        model = Interest
        fields = ('first_name','last_name','phone','email','text')
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.TextInput(attrs={'size':600,'class':'editable interestcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('interest','responder')

        widgets = {
            'responder':forms.TextInput(attrs={'class':'textinputclass'}),
            'interest':forms.TextInput(attrs={'size':600,'class':'editable'})
        }