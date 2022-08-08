from django.test import TestCase

from blog.models import Author, Comment, Post 
# Create your tests here.

class AuthorModelTest(TestCase):
    # model fields have the correct label
    author = Author.objects.get(id=3)
    
    def get_field_label(self, field):
        return self.author._meta.get_field(field).verbose_name
    
    def get_field_max_length(self, field):
        return self.author._meta.get_field(field).max_length
    
    def test_firstname_label(self):
        self.assertEqual(self.get_field_label('first_name'), 'first name')
    
    def test_lastname_label(self):
        self.assertEqual(self.get_field_label('last_name'), 'last name')
    
    def test_username_label(self):
        self.assertEqual(self.get_field_label('username'), 'username')
    
    def test_password_label(self):
        self.assertEqual(self.get_field_label('password'), 'password')
    
    def test_bio_label(self):
        self.assertEqual(self.get_field_label('bio'), 'bio')
    
    def test_email_addres_label(self):
        self.assertEqual(self.get_field_label('email'), 'email address')
    
    # model fields have the correct length
    def test_username_length(self):
        self.assertEqual(self.get_field_max_length('username'), 150)
        
    def test_firstname_length(self):
        self.assertEqual(self.get_field_max_length('first_name'), 150)
    
    def test_lastname_length(self):
        self.assertEqual(self.get_field_max_length('last_name'), 150)
        
    def test_email_length(self):
        self.assertEqual(self.get_field_max_length('email'), 254)
        
    # model have the expected object name 
    # (e.g. __str__() returns the expected value)
    def test_model_str(self):
        name = f'{self.author.first_name} {self.author.last_name}'
        self.assertEqual(self.author.__str__(), name)


class CommentModelTest(TestCase):
    # model fields have the correct label
    comment = Comment.objects.get(id=1)
    
    def get_field_label(self, field):
        return self.comment._meta.get_field(field).verbose_name
    
    def test_description_label(self):
        self.assertEqual(self.get_field_label('description'), 'description')
    
    def test_comment_author(self):
        self.assertEqual(self.get_field_label('comment_author'), 'comment author')
    
    def test_comment_time(self):
        self.assertEqual(self.get_field_label('comment_time'), 'comment time')
    
    # model fields are mostly referenced from another table
    
    # model have the expected object name 
    # (e.g. __str__() returns the expected value)
    def test_model_str(self):
         self.assertEqual(self.comment.__str__(), self.comment.description)
 

class PostModelTest(TestCase):
    # model fields have the correct label
    post = Post.objects.get(id=1)
    
    def get_field_label(self, field):
        return self.post._meta.get_field(field).verbose_name
    
    def get_field_max_length(self, field):
        return self.post._meta.get_field(field).max_length
    
    def test_title_label(self):
        self.assertEqual(self.get_field_label('title'), 'title')
        
    def test_content_label(self):
        self.assertEqual(self.get_field_label('content'), 'content')
    
    def test_post_date_label(self):
        self.assertEqual(self.get_field_label('post_date'), 'published date')
    
    def test_author_label(self):
        self.assertEqual(self.get_field_label('author'), 'author')
    
    def test_slug_label(self):
        self.assertEqual(self.get_field_label('slug'), 'slug')
        
    # model fields have the correct length
    def test_title_length(self):
        self.assertEqual(self.get_field_max_length('title'), 200)
        
    def test_slug_length(self):
        self.assertEqual(self.get_field_max_length('slug'), 200)
    
    # model have the expected object name 
    # (e.g. __str__() returns the expected value)
    def test_model_str(self):
         self.assertEqual(self.post.__str__(), self.post.title)

    # Model have the expected URL for individual Blog
    def test_get_absolute_url(self):
        slug = self.post.slug
        self.assertEqual(self.post.get_absolute_url(), '/blog/blogs/'+slug)