from django.test import TestCase
import requests

# Create your tests here.
class SiteTestCase(TestCase):
    '''
    Testing tests :)
    '''
    
    def test_site_ok(self):
        '''
        Is localhost up?
        '''

        site = requests.get('http://localhost:8000')

        self.assertEqual(site.status_code, 200)
    
    def test_site_has_input(self):
        '''
        Is there input field?
        '''

        site = requests.get('http://localhost:8000')

        self.assertIn('input', site.text)
    
    
        
    