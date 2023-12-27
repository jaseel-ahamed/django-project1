from django.db import models

class Contact(models.Model):
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    contact_message = models.TextField()

    def __str__(self):
        return self.contact_name
