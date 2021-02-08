from django.test import SimpleTestCase
from django.urls import reverse, resolve
from order.views import order

class TestUrls(SimpleTestCase):

    def test_order_url_is_resolve(self):
        url=reverse('order')
        self.assertEquals(resolve(url).func, order)

       