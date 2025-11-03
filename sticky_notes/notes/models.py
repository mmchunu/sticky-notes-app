from django.db import models

class StickyNote(models.Model):
    title = models.CharField(max_length=100)   # Note title
    content = models.TextField()               # Note content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp when updated

    def __str__(self):
        return self.title
