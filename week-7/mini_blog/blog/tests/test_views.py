from django.test import TestCase

from ..views import BlogListView


class BlogListViewTest(TestCase):
    
    def test_blog_list_view_exists_at_the_expected_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)
