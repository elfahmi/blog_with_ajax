from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)

    def __str__(self):
        return self.comment
