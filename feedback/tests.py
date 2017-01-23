from django.test import TestCase
from feedback.models import Feedback
from django.db import connections
from feedback.forms import SurveyFeedback
from selenium import webdriver
from django.test import LiveServerTestCase
from django.conf import settings

class LiveFeedbackTestCase(LiveServerTestCase):

    def test_textbox_length(self):
        driver = webdriver.Chrome("/Users/irving/Documents/ve/FeedbackDjango/chromedriver")
        driver.get('{0}/feedback'.format(self.live_server_url))

        text_box = driver.find_element_by_id('id_textFeedback')
        for i in range(0, settings.MAX_CHARS+1):
            text_box.send_keys('a')

        text_box = driver.find_element_by_id('id_textFeedback')
        length = len(text_box.get_attribute('value'))
        self.assertEqual(length, settings.MAX_CHARS)

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
            print ("database failed to connect "+e)

    def test_radio_required_valid(self):
        form_data = {'radioFeedback': 'very satisfied', 'textFeedback': ''}
        form = SurveyFeedback(data = form_data)
        self.assertTrue(form.is_valid())

    def test_radio_required_invalid(self):
        form_data = {'radioFeedback': '', 'textFeedback': ''}
        form = SurveyFeedback(data = form_data)
        self.assertFalse(form.is_valid())

    def test_text_max_valid(self):
        form_data = {'radioFeedback': 'very satisfied', 'textFeedback': 'testing less than 1200 characters.'}
        form = SurveyFeedback(data = form_data)
        self.assertTrue(form.is_valid())

    def test_text_max_invalid(self):
        form_data = {'radioFeedback': 'very satisfied', 'textFeedback': 'testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, testing more than 1200 characters, '}
        form = SurveyFeedback(data = form_data)
        self.assertFalse(form.is_valid())
