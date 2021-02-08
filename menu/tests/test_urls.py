from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menu.views import menu,administrator, modify_menu

class TestUrls(SimpleTestCase):

    def test_menu_url_is_resolve(self):
        url=reverse('menu')
        self.assertEquals(resolve(url).func, menu)

    def test_administrator_url(self):
        url=reverse('administrator')
        self.assertEquals(resolve(url).func, administrator)
    
    def test_modify_menu_url(self):
        url=reverse('modify_menu')
        self.assertEquals(resolve(url).func, modify_menu)

       