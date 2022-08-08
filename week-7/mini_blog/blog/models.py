from distutils.command.upload import upload
from multiprocessing.dummy import Manager
from multiprocessing.managers import BaseManager
from time import strftime
from django.contrib.auth.models import User 
from django.db import models
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.

class ActiveObject(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)
    
    
class DeletedObject(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = True)
    


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True, verbose_name='published date')
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='author_posts')
    featured_image = models.ImageField(upload_to='blog/', null=True, blank=True)
    slug = models.SlugField(max_length=200,null=True, blank=True)
    is_deleted = models.BooleanField(default=False, verbose_name="Soft delete")
    
    active_objects = ActiveObject()
    deleted_objects = DeletedObject()
    
    objects = models.Manager()
    
    def __str__(self):
        return self.title    
    
    def save(self):
        self.slug = slugify(self.title)
        return super().save()
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('post-detail', args=[self.slug])
    
    def get_published_date(self):
        new_date = self.post_date.strftime("%b. %d, %Y")
        return new_date
    
    def get_post_excerpt(self):
        return f'{self.content[:200]}...'   
    
    

class Author(User):
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='authors/', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'author'
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def save(self):
        self.slug = slugify(self.username)
        return super().save()
    
    def number_of_posts(self):
        return self.post_set.count()
    
    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})
    
    # def save(self):
    #     self.is_staff = True
    #     return super().save()
    

class Comment(models.Model):
    description = models.TextField()
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    objects = models.Manager()
    active_comments = ActiveObject()
    
    def __str__(self) -> str:
        return self.description
    
    # def get_absolute_url(self):
    #     return reverse('post-detail', args=[self.post.slug])
    
    def short_description(self):
        return f'{self.description[:75]}...'
    
    # class Meta:
    #     ordering = ['-comment_time']
    