from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)


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


class Proposal(models.Model):
    authorid = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    typerecordid = models.ForeignKey(TypeRecord, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    handlingid = models.ForeignKey(Handling, on_delete=models.CASCADE)
    subjectproposal = models.CharField(max_length=50)
    text = models.TextField()
