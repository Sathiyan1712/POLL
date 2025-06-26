from django import forms
from home.models import Poll

class VoteForm(forms.Form):
    CHOICES = (
        (1, "Option 1"),
        (2, "Option 2"),
        (3, "Option 3"),
    )
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

class PollForm(forms.ModelForm):
    delete_password = forms.CharField(widget=forms.PasswordInput, label="Delete Password")
    class Meta:
        model = Poll
        fields = ['statement', 'option1', 'option2', 'option3', 'delete_password']
        widgets = {
            'statement': forms.TextInput(attrs={'placeholder': 'Enter your question here', 'class': 'form-control'}),
            'option1': forms.TextInput(attrs={'placeholder': 'Option 1', 'class': 'form-control'}),
            'option2': forms.TextInput(attrs={'placeholder': 'Option 2', 'class': 'form-control'}),
            'option3': forms.TextInput(attrs={'placeholder': 'Option 3', 'class': 'form-control'}),
        }

# home/forms.py (add this too)

class DeletePollForm(forms.Form):
    delete_password = forms.CharField(widget=forms.PasswordInput, label="Enter Delete Password")

