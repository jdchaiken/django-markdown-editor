from django.test import TestCase
from app.models import Post

class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title='My title',description='blurb', wiki='Post Body')
        self.assertEqual(post.title,'My title')
        self.assertEqual(post.description,'blurb')
        self.assertEqual(post.wiki,'Post Body')