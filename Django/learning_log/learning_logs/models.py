from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text: models.CharField = models.CharField(max_length=200)
    date_added: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text