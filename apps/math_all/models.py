from django.db import models

class MathClass(models.Model):
    name = models.CharField(max_length=100)

class MathSection(models.Model):
    class_name = models.ForeignKey(MathClass, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()
