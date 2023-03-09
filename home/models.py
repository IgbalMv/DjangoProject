from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.IntegerField(choices=[(1,'Suggestion'),(2,'Complaint')])
    messages = models.TextField(null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.subject}'


