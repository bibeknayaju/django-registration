from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    project = models.CharField(max_length=355)
    message = models.TextField()

    def __str__(self):
        return self.name


class FileUpload(models.Model):
    file = models.ImageField(upload_to="uploads/")
    # date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name
