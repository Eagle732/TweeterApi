from django import forms

class TweetKeyWords(forms.Form):
    keyWords = forms.CharField(max_length=125,
                    widget=forms.TextInput(attrs={'placeholder': 'eg:    #facebook , #twitter'}))
