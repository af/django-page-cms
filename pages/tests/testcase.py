from django.test import TestCase
from pages.models import Page, Content, PageAlias
from django.contrib.auth.models import User
from django.test.client import Client

class MockRequest:
    REQUEST = {'language': 'en'}
    GET = {}
    META = {}

class TestCase(TestCase):
    """Django page CMS test suite class"""
    fixtures = ['pages_tests.json']
    counter = 1

    def get_admin_client(self):
        client = Client()
        client.login(username='admin', password='b')
        return client

    def get_new_page_data(self, draft=False):
        """Helper method for creating page datas"""
        page_data = {'title':'test page %d' % self.counter,
            'slug':'test-page-%d' % self.counter, 'language':'en-us',
            'sites':[1], 'status': Page.DRAFT if draft else Page.PUBLISHED,
            # used to disable an error with connected models
            'document_set-TOTAL_FORMS':0, 'document_set-INITIAL_FORMS':0,
            }
        self.counter = self.counter + 1
        return page_data

    def new_page(self, content={'title':'test-page'}, language='en-us'):
        author = User.objects.all()[0]
        page = Page(author=author, status=Page.PUBLISHED,
            template='pages/examples/index.html')
        page.save()
        # necessary to clear old URL cache
        page.invalidate()
        for key, value in content.items():
            Content(page=page, language='en-us', type=key, body=value).save()
        return page

    def create_new_page(self, client=None, draft=False):
        if not client:
            client = self.get_admin_client()
        page_data = self.get_new_page_data(draft=draft)
        response = client.post('/admin/pages/page/add/', page_data)
        self.assertRedirects(response, '/admin/pages/page/')
        slug_content = Content.objects.get_content_slug_by_slug(
            page_data['slug'])
        return slug_content.page