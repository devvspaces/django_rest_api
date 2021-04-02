from django.test import TestCase

from django.auth.models import get_user_model

from postings.models import BlogPost


User = get_user_model()


class BlogPostTest(TestCase):
	def setUp(self):
		user = User(username='ayomide', email='test@test.com')
		user.set_password('ajfljaldfjaldjfkajdf')
		user.save()

		blog_post = BlogPost.objects.create(title='New test title', content='adjlajdfjadlkfj')

	def test_user_post_count(self):
		