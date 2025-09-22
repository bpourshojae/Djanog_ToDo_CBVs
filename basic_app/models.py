from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# UserInfo model extends the default Django User model
# It stores additional information like profile picture and website
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model (one-to-one relationship)
    profile_pic = models.ImageField(upload_to='basic_app',blank=True) # Optional profile image 
    user_website = models.URLField(blank=True)  # Optional personal website URL
    
    def __str__(self):
        return self.user.username  # Returns the username for easy identification
    
# Task model represents a single task in the to-do list    
class Task(models.Model):
    title = models.CharField(max_length=256,blank=False)    # Task title (required)
    description = models.TextField(blank=False)  # Task description (required)
    status = models.BooleanField(default=False, blank=True)  # Task completion status (True = Done, False = Pending)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Link to the User who owns this task
    
    def __str__(self):
        return self.title  # Returns the task title for easy identification
    
    def get_absolute_url(self):
        return reverse('basic_app:task_list')