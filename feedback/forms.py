from django import forms
from django.conf import settings

class SurveyFeedback(forms.Form):
    CHOICES = [('Very Satisfied', 'Very Satisfied'), ('Satisfied', 'Satisfied'), ('Neither', 'Neither'), ('Dissatisfied', 'Dissatisfied'), ('Very Dissatisfied', 'Very Dissatisfied')]
    radioFeedback = forms.ChoiceField(label='How satisfied were you with the service you just received?', choices=CHOICES, widget=forms.RadioSelect(), required=False)
    textFeedback = forms.CharField(label='Survey Feedback', max_length=settings.MAX_CHARS, required=False, widget=forms.Textarea(attrs={'rows': 10, 'cols': 80, 'onKeyDown':'return setTimeout(remainingChars('+str(settings.MAX_CHARS)+'), 100);'}))
