from django.db import models
from django.utils import timezone

# Create your models here.

class UserLog(models.Model):
    user = models.ForeignKey('auth.User')
    operation = models.CharField(max_length = 200)
    detail = models.TextField
    operation_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def _str_(self):
        return self.operation