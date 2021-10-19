from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from country_utils.fields import CountryField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employment = models.CharField(max_length=30, blank=True)
    country = CountryField(blank=False, default='SE')
    region = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.category)


class File(models.Model):
    file = models.CharField(max_length=50)


class TypeRecord(models.Model):
    typerecord = models.CharField(max_length=50)

class Handling(models.Model):
    authorid = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    typerecordid = models.ForeignKey(TypeRecord, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    subjecthandling = models.CharField(max_length=50)
    solution = models.CharField(max_length=50)


class Offer(models.Model):
    authorid = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, default='Как жить дальше!!!')
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, default='Бишкек')
    text = models.TextField()
    audiooffer = models.CharField(max_length=50, default='ФАЙЛ')
    files = models.FileField(upload_to='offer/', null=True, blank=True)
