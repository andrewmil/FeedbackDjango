from django.test import TestCase
from polls.models import Feedback
from django.db import connections
from polls.forms import SurveyFeedback

# Create your tests here.

class FeedbackTestCase(TestCase):
    def test_dbconnect(self):
        db_conn = connections['default']
        try:
            c = db_conn.cursor()
        except OperationalError:
            connected = False
        else:
            connected = True

    def test_formValidation(self):
        
