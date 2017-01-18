from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SurveyFeedback
from .models import Feedback
# Create your views here.


def index(request):

    form = SurveyFeedback(request.POST)
    return render(request, 'feedback/index.html', {'form': form})


def database_Send(request):
    from datetime import datetime

    if request.method == 'POST':
        form = SurveyFeedback(request.POST)
        if form.is_valid(): # All validation rules pass
            # retrieving form data ##
            satisfaction = form.cleaned_data['radioFeedback']
            feedback = form.cleaned_data['textFeedback']
            date = datetime.now()
        else:
            return HttpResponseRedirect('/index/')

    print('sending data to database')
    f = Feedback(surveyid=1, satisfaction=satisfaction, timeentered=date, comment=feedback)
    f.save()

    print("done")
    return render(request, 'feedback/confirm.html')
