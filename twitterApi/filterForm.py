from django import forms

class tweetFilter(forms.Form):
    fromDate = forms.DateField(required=False,widget=forms.DateInput(attrs={'placeholder':'10/25/2006'}))
    toDate = forms.DateField(required=False,widget=forms.DateInput(attrs={'placeholder':'10/25/2006'}))
    less_retweet = forms.IntegerField(required=False)
    greater_retweet = forms.IntegerField(required=False)
    less_followers = forms.IntegerField(required=False)
    greater_followers = forms.IntegerField(required=False)
    contains_char = forms.CharField(required=False)
    Text_startWith = forms.CharField(required=False)
    Text_endtWith = forms.CharField(required=False)
    Name_starttWith = forms.CharField(required=False)
    Name_endWith = forms.CharField(required=False)
