from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import SurveyFeedback
from .models import Feedback
from .static.polls.scripts.py.dbConnect import *
from .static.polls.scripts.py.validation import *
# Create your views here.

def index(request):

    form = SurveyFeedback(request.POST)
    return render(request, 'polls/index.html', {'form': form})

def database_Send(request):
    from datetime import datetime

    if request.method == 'POST':
        form = SurveyFeedback(request.POST)
        if form.is_valid(): # All validation rules pass
            ## retrieving form data ##
            satisfaction = form.cleaned_data['radioFeedback']
            feedback = form.cleaned_data['textFeedback']
            date = datetime.now()
        else:
            return HttpResponseRedirect('/index/')

    print('sending data to database')
    f = Feedback(surveyid=1, satisfaction=satisfaction, timeentered=date, comment=feedback)
    f.save()

    ## validation ##
    if (feedbackValidation(feedback) or satisfactionValidation(satisfaction)):
         return redirect('/polls/')

    print("done")

    return HttpResponseRedirect('/polls/')
