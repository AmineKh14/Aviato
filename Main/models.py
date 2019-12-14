from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings    
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

ROLE = (
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('freelancer','Freelancer'),
    )

JOB = (
        ("plumber","Pulmber"),
        ("welder","Welder"),
        ("maneuver","Maneuver"),
        ("builder","Builder"),
        ("electrician","Electrician"),
        ("carpenter","Carpenter"),
        ("mover","Mover"),
        ("exterminator","Exterminator") 
    )

STATE = (
    ('Occupé','occupé'),
    ('Libre','libre')
)

class Utilisateur(AbstractUser):
    role = models.CharField(choices=ROLE,default='etudiant',max_length=10)
    banned=models.BooleanField(default=False)


class Profile (models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="profile")
    numero_telephone = models.IntegerField(null=True)
    job = models.CharField(choices=JOB,default='1cpi',max_length=4,null=True)
    bio = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,upload_to='profile_pics',default='profile_pics/default.png')
    state = models.BooleanField(choices=STATE)
    rating = models.IntegerField()
    ville = models.CharField(max_length=20)

class Historique(models.Model):
    client = models.OneToOneField(Utilisateur,on_delete=models.CASCADE,related_name="client")
    freelancer = models.OneToOneField(Utilisateur,on_delete=models.CASCADE,related_name="freelancer")
    dateD = models.DateField()
    dateF = models.DateField()


