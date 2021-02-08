from django.test import SimpleTestCase
from order.service import time_now
from datetime import time

class TestTime(SimpleTestCase):

    def test_time(self):
        t=time(11,1,0)
        answer=False
        self.assertEquals(time_now(t), answer)
        t=time(10,59,0)
        answer=True
        self.assertEquals(time_now(t), answer)
