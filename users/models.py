from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.utils import  timezone
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.utils.text import slugify

def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])
user_logged_in.connect(update_last_login)


class Profiles(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user=models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    phone=models.CharField(max_length=20,verbose_name=_("phone"))
    slug=models.SlugField(blank=True, null=True) 
    image=models.ImageField(upload_to='profile/',blank=True, null=True)
    adress=models.CharField(max_length=100)
    join_date=models.DateTimeField(verbose_name=_("Created At"), default=datetime.now)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    def save(self ,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        else:
            self.slug=slugify(self.user.username)
        super(Profiles, self).save(*args, **kwargs)
        
    def __str__(self):
        return 'user ---->  ' +  str(self.user) +'role ---->  ' + self.role
    def create_profile(sender ,*args, **kwargs): # type: ignore
        if kwargs['created']:
            user_profile=Profiles.objects.create(user=kwargs['instance'])    
    post_save.connect(create_profile , sender=User)
    
    
class Result(models.Model):
    user = models.ForeignKey(Profiles,on_delete=models.CASCADE) # type: ignore
    quiqexamreqsult = models.ForeignKey('main.QuickExams',verbose_name=_("Quick Exams Result"),on_delete=models.CASCADE,blank=True, null=True) # type: ignore
    fullexamreqsult = models.ForeignKey('main.FullExams',verbose_name=_("Full Exams Result"),on_delete=models.CASCADE,blank=True, null=True) # type: ignore
    Resultss=models.TextField(max_length=20,verbose_name=_("Result"))
    
    def clean(self):
        if self.quiqexamreqsult is None and self.fullexamreqsult is None:
            raise ValidationError("Please select either Quick Exam Result or Full Exam Result.")
        elif self.quiqexamreqsult is not None and self.fullexamreqsult is not None:
            raise ValidationError("You cannot select both Quick Exam Result and Full Exam Result.")

    
    def __str__(self):
        return str(self.user)
