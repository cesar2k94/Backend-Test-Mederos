from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import welcome, register, login, logout

class TestUrls(SimpleTestCase):

    def test_welcome_url(self):
        url=reverse('welcome')
        self.assertEquals(resolve(url).func, welcome)

    def test_register_url(self):
        url=reverse('register')
        self.assertEquals(resolve(url).func, register)
    
    def test_login_url(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func, login)
    
    def test_logout_url(self):
        url=reverse('logout')
        self.assertEquals(resolve(url).func, logout)

       