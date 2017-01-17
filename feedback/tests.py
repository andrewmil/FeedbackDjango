from django.test import TestCase
from feedback.models import Feedback
from django.db import connections
from feedback.forms import SurveyFeedback


# Create your tests here.

class FeedbackTestCase(TestCase):
    def test_dbconnect(self):
        try:
            db_conn = connections['default']
            try:
                c = db_conn.cursor()
            except OperationalError:
                connected = False
            else:
                connected = True
        except Exception as e:
            print "database failed to connect "+e

    def test_dbinsertion(self):
        #Insert data into form
        form_data = {'radioFeedback': 'satisfied', 'textFeedback': 'test db insertion'}
        #Insert data into database
        satisfaction = form.cleaned_data['radioFeedback']
        comment = form.cleaned_data['textFeedback']
        date = datetime.now()
        f = Feedback(surveyid=1, satisfaction=satisfaction, timeentered=date, comment=feedback)
        f.save()
        #Check data has been inserted correctly
        Feedback.objects.order_by('timeentered')[0:1].get()

    def test_radio_required_valid(self):
        form_data = {'radioFeedback': 'very satisfied', 'textFeedback': ''}
        form = SurveyFeedback(data = form_data)
        self.assertTrue(form.is_valid())

    def test_radio_required_invalid(self):
        form_data = {'radioFeedback': '', 'textFeedback': ''}
        form = SurveyFeedback(data = form_data)
        self.assertFalse(form.is_valid())

    def test_text_max_valid(self):
        form_data = {'radioFeedback': 'very satisfied', 'textFeedback': 'test less than 1200 characters'}
        form = SurveyFeedback(data = form_data)
        self.assertTrue(form.is_valid())

    def test_text_max_invalid(self):
        form_data = {'radioFeedback': 'very satisfied', 'textFeedback': 'testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, '}
        form = SurveyFeedback(data = form_data)
        self.assertFalse(form.is_valid())
