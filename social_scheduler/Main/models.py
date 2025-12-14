from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class ScheduledPost(models.Model):
    PLATFORM_CHOICES = [
    ('TW','TWITTER'),
    ('TE','TELEGRAM'),
    ('IN','INSTAGRAM')
    ] 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    platfrom = models.CharField(choices=PLATFORM_CHOICES, max_length=2)
    scheduled_time = models.DateTimeField()
    status = models.CharField(default="Pending", max_length=10)

    def __str__(self):
        return f' {self.user.username}'
    

class Telegram(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    BOT_id = models.TextField()
    chat_id = models.TextField()
    content= models.TextField()
    scheduled_time = models.DateTimeField()
    photo  = models.ImageField(upload_to='photos/', blank=True, null=True)
    image_url = models.URLField(blank=True , null=True)
    status = models.CharField(default="Pending", max_length=20)
  


class Reddit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subreddit_name = models.CharField(max_length=20)
    title= models.TextField()
    body = models.TextField(blank=True , null=True)
    photo  = models.ImageField(upload_to='reddit_photos/', blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)
    scheduled_time = models.DateTimeField()
    status = models.CharField(default="Pending", max_length=20)




class RedditAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.TextField(default="default_user")
    refresh_token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ContentTemplate(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('article', 'Article'),
        ('social_post', 'Social Post'),
        ('email', 'Email'),
        ('product_description', 'Product Description'),
        ('blog', 'Blog Post'),
        ('other', 'Other')
    ]
    
    TONE_CHOICES = [
        ('professional', 'Professional'),
        ('casual', 'Casual'),
        ('persuasive', 'Persuasive'),
        ('informative', 'Informative'),
        ('humorous', 'Humorous'),
        ('formal', 'Formal'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES)
    topic = models.TextField()
    audience = models.TextField()
    tone = models.CharField(max_length=50, choices=TONE_CHOICES)
    style = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True, help_text="Comma-separated keywords")
    length = models.CharField(max_length=100, help_text="e.g., 500 words, 280 characters")
    format = models.TextField(blank=True, null=True, help_text="e.g., bullet points, headings, Q&A")
    objective = models.TextField(help_text="What should this content achieve?")
    generated_content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.content_type} - {self.topic[:30]}"


