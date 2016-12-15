from django.test import TestCase
from polls.models import Feedback

# Create your tests here.

class FeedbackTestCase(TestCase):
    def test_dbconnect(self):
        
