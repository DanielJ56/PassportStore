from django.db import models

# Create your models here.
class PERSON(models.Model):
    person_id = models.IntegerField()
    reserved_user_id = models.IntegerField(null=True)
    pronoun_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=30)
    #length of 0 is possible for gender, possible cause for issues.
    gender = models.CharField(max_length=1)
    
    passport_num_hash = models.TextField(max_length=4000)
    passport_num_salt = models.TextField(max_length=4000)
    
    passport_photo_ref = models.CharField(max_length=255)
    
    bio = models.TextField(max_length=2000,null=True)
    avatar_ref = models.CharField(max_length=255,null=True)
