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
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

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
