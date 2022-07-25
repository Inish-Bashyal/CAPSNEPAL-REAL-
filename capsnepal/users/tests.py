import imp
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from users.views import register_name,login_user,logout,update_password,update_user,show_user_details,delete_user

# Create your tests here.
class Testurls(SimpleTestCase):
    
    def test_case_register_name_urls(self):
        urls = reverse('register_user')
        self.assertEquals(resolve(urls).func,register_name)
        
    def test_case_login_user_urls(self):
        urls = reverse('login_user')
        self.assertEquals(resolve(urls).func,login_user)
        
    def test_case_logout_urls(self):
        urls = reverse('logout')
        self.assertEquals(resolve(urls).func,logout)
        
        
    # def test_case_delete_user_urls(self):
    #     urls = reverse('delete_user')
    #     self.assertEquals(resolve(urls).func,delete_user)
        
    def test_case_show_user_details_urls(self):
        urls = reverse('show_user_details')
        self.assertEquals(resolve(urls).func,show_user_details)
        
    def test_case_update_user_urls(self):
        urls = reverse('update_user/<id>')
        self.assertEquals(resolve(urls).func,update_user/id)
        
    # def test_case_update_password_urls(self):
    #     urls = reverse('update_password')
    #     self.assertEquals(resolve(urls).func,update_password)