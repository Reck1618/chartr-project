from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
