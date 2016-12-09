from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question
from .forms import SurveyFeedback
from .static.polls.scripts.py import dbConnect
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

    conn_string = "host='172.28.78.195' port='5432' dbname='feedback2' user='andrew' password='password'"

    form = SurveyFeedback()
    conn = dbConnect(conn_string)

    ## retrieves data from form ##
    satisfaction = form.satisfaction.data
    feedback = form.feedback.data
    date = datetime.now()

    ## validation ##
    if (feedbackValidation(feedback) or satisfactionValidation(satisfaction)):
        return redirect('/index')

    sendData(conn, satisfaction, date, feedback)

    conn.close()
    print("done")

    return render_template('polls/index.html')
