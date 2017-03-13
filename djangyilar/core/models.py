from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
        
class Email(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=256)
    # content = models.CharField(max_length=4000)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.contact_name
        
    def __str__(self):
        return self.contact_name
        
    class Meta:
        ordering = ['-created_date']