from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
#from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
     # Fields and methods go here
    PRIORITY_CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
#    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    attachments = models.FileField(upload_to='task_attachments/', null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
#    task_assignor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_tasks')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_tasks')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_tasks')
# pylint: disable=E0307
    def __str__(self):
        return self.title
  
    class Meta:
        ordering = ['-created_at', 'is_completed']



class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    home_address = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    office = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

def __str__(self):
    return self.username