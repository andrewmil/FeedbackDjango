from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question
from .forms import SurveyFeedback
from .static.polls.scripts.py.dbConnect import *
from .static.polls.scripts.py.validation import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SurveyFeedback(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = SurveyFeedback()

    return render(request, 'polls/index.html', {'form': form})

def database_Send(request):
    import psycopg2
    import sys
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
    conn_string = "host='172.28.46.20' port='5432' dbname='feedback2' user='andrew' password='password'"
    conn = dbConnect(conn_string)

    ## validation ##
    if (feedbackValidation(feedback) or satisfactionValidation(satisfaction)):
         return redirect('/polls/')

    sendData(conn, satisfaction, date, feedback)

    conn.close()
    print("done")

    return HttpResponseRedirect('/polls/')
