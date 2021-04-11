from django.test import SimpleTestCase
from django.urls import path, reverse, resolve
from budget.views import project_detail, project_list, ProjectCreateView


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolve(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func, project_list)

    def test_add_url_is_resolve(self):
        url = reverse('add')
        # print(url) .func.view_class /add/ cause its ClassBase
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_detail_url_is_resolve(self):
        url = reverse('detail', args=['pk'])
        # print(url) .func.view_class /add/ cause its ClassBase
        self.assertEquals(resolve(url).func, project_detail)
