from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.
class Music_Lover(models.Model):
    person=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.person.username}'

class Music(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=300)
    audio=models.FileField()
    person=models.ForeignKey(Music_Lover,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.name} by {self.person.person.username}'


class Folder_repo(models.Model):
    Type = (
    ('private', 'Private'),
    ('public', 'Public'),
    ('protected', 'Protected'),
    )
    folder_type = models.CharField(choices=Type, default='PRIVATE', max_length=15)
    music_lover = models.ForeignKey(Music_Lover, related_name="musiclover", on_delete=models.CASCADE)
    music = models.ForeignKey(Music, related_name="music", on_delete=models.CASCADE)

class Email(models.Model):
    email=models.EmailField(primary_key=True,unique=True)  
    def __str__(self) -> str:
        return self.email


class Email_Folder_conn(models.Model):
    emails=models.ManyToManyField(Email,related_name="EmailFolder")
    protect=models.ForeignKey(Folder_repo,related_name="protected",on_delete=models.CASCADE)


    

 
@receiver(post_save, sender=User)
def create_music_lover(sender, instance, created, **kwargs):
    if created:
        Music_Lover.objects.create(person=instance)
post_save.connect(create_music_lover,sender=User)
@receiver(post_save, sender=User)
def create_email(sender, instance, created, **kwargs):
    if created:
        Email.objects.create(email=instance.email)
post_save.connect(create_email,sender=User)