from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse("home")
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=255)
    #content = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    content = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default='Cricket')
    snippet = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("home")
    

    class Meta:
        verbose_name = 'Post'  # default: ModelName
        ordering = ['-date_posted']  # default: ['-pk']
        verbose_name_plural = 'Posts'

    
# User Profile Models
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=255, null=True, blank=True) # for social media
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("home")

# Comment models
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
    