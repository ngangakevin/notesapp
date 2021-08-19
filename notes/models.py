from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length= 128, null=True, blank= True)
    content = models.TextField(null=True, blank=True)

    last_updated_on = models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title
