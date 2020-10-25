from django.db import models
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    notes = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.title} - {self.text} - {self.notes}'
