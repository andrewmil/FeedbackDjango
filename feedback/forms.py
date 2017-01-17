from django import forms

class SurveyFeedback(forms.Form):
    CHOICES = [('very satisfied', 'very satisfied'), ('satisfied', 'satisfied'), ('neither', 'neither'), ('dissatisfied', 'dissatisfied'), ('very dissatisfied', 'very dissatisfied')]
    radioFeedback = forms.ChoiceField(label='How satisfied were you with the service you just received?', choices=CHOICES, widget=forms.RadioSelect(), required=True)
    textFeedback = forms.CharField(label='Survey Feedback', max_length=1200, required=False, widget=forms.TextInput(attrs={'onKeyDown':'return setTimeout(remainingChars, 10);'}))
