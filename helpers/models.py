from django.db import models


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #Django doesn't have these fields by default
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True
        ordering = ['-created_at'] #sort objects in ascending order