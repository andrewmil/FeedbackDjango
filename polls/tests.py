from django.test import TestCase
from polls.models import Feedback
from django.db import connections
from polls.forms import SurveyFeedback

# Create your tests here.

class FeedbackTestCase(TestCase):
    def test_dbconnect(self):

        try:
            db_conn = connections['default']
            c = db_conn.cursor()
        except OperationalError:
            connected = False
        else:
            connected = True

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
