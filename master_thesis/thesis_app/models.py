from django.db import models
from django.utils import timezone
from django.conf import settings
from django_countries.fields import CountryField
from django_countries import countries 
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices import *
from unittest.util import _MAX_LENGTH


# ---------------------------------------------- Personal Information ------------------------
class step_1(models.Model):
    #------------------------- Fields ------------------------
    title = models.CharField(
        max_length = 20, 
        editable=False,
        default = 'step1'
    )
    
    user_id = models.ForeignKey(
        User,
        default = 1,
        on_delete=models.CASCADE
        
    )
    
    gender = models.CharField(
        choices = Gender_choices,
        max_length = 20,
        verbose_name = 'gender',
        default=None,
        blank=False
    )
    
    age = models.CharField(
        choices = Age_choices,
        max_length = 40,
        verbose_name = 'age',
        default=None,
        blank=False
    )
    
    country = CountryField(multiple = False,
                           default=None,
                            blank=False)
    
    imaginative = models.CharField(
        choices = Imaginative_choices,
        max_length = 20,
        verbose_name = 'imaginative',
        default=None,
        blank=False
       
    )
    organized = models.CharField(
        choices = Organized_choices,
        max_length = 20,
        verbose_name = 'organized',
        default=None,
        blank=False
       
    )
    enthusiastic  = models.CharField(
        choices = Enthusiastic_choices,
        max_length = 20,
        verbose_name = 'enthusiastic',
        default=None,
        blank=False
      
    )
    kind = models.CharField(
        choices = kind_choices,
        max_length = 20,
        verbose_name = 'kind',
        default=None,
        blank=False
       
    )
    calm = models.CharField(
        choices = Calm_choices,
        max_length = 20,
        verbose_name = 'calm',
        default=None,
        blank=False
    
    )
    
    class Meta:
        verbose_name= 'Personal_info'
        ordering = ['user_id']
        db_table = 'Personal_information'
    def __str__(self):
        return self.title
    
    
        
# ---------------------------------------------- Features Selection --------------------------
class step_2(models.Model):
    title = models.CharField(
        max_length = 20, 
        editable=False,
        default = 'step2'
    )
    
    user_id = models.ForeignKey(
        User,
        default = 1,
        on_delete=models.CASCADE
    )
    
    features = MultiSelectField(choices=features_choices,
                                 min_choices=3,
                                 max_length=200)
    class Meta:
        verbose_name= 'features'
        ordering = ['user_id']
        db_table = 'Features'
    def __str__(self):
        return self.title

# ----------------------------------------------  countries name -------------------------------
class country_name(models.Model):

    
    country_name = models.CharField(
        blank=False,
        max_length = 50,
        default = country_name[0][0],
        choices = country_name
    )

    def __str__(self):
        return self.country_name
    
    class Meta:
        db_table = 'Countries'
    

# ----------------------------------------------  user rating -------------------------------
class user_rate(models.Model):
    title = models.CharField(
        max_length = 20,
        editable = False,
        default = 'user_rate'
    )
    
    user_id = models.ForeignKey(
        User,
        default = 1,
        related_name='current_user',
        on_delete=models.CASCADE
    )
    
    countries_name_id = models.ForeignKey(
        country_name,
        default=1,
        blank=False,
        on_delete = models.CASCADE
    )
    country_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],blank=False, default=0)
    

    
    def __str__(self):
        return "{}_{}".format(self.user_id.username,self.countries_name_id.country_name)
    
    class Meta:
        unique_together = (('countries_name_id', 'user_id'),)
        verbose_name = "user_rate"
        db_table = 'user_ratings'

    

# -------------- Test ------------------
class UsabilitySurvey(models.Model):
    #------------------------- Fields ------------------------
    title = models.CharField(
        max_length = 20, 
        editable=False,
        default = 'UsabilitySurvey'
    )
    
    user_id = models.ForeignKey(
        User,
        default = 1,
        on_delete=models.CASCADE
        
    )
    
    usage_frequency = models.CharField(
        choices = usage_frequency,
        max_length = 20,
        verbose_name = 'usage_frequency',
        default=None,
        blank=False
    )
    
    
    system_complexity = models.CharField(
        choices = system_complexity,
        max_length = 20,
        verbose_name = 'system_complexity',
        default=None,
        blank=False
    )
    
    usage_ease = models.CharField(
        choices = usage_ease,
        max_length = 20,
        verbose_name = 'usage_ease',
        default=None,
        blank=False
    )
    need_help = models.CharField(
        choices = need_help,
        max_length = 20,
        verbose_name = 'need_help',
        default=None,
        blank=False
    )
    
    functions_integrated = models.CharField(
        choices = functions_integrated,
        max_length = 20,
        verbose_name = 'functions_integrated',
        default=None,
        blank=False
    )
    system_inconsistency = models.CharField(
        choices = system_inconsistency,
        max_length = 20,
        verbose_name = 'system_inconsistency',
        default=None,
        blank=False
    )
    learn_to_use = models.CharField(
        choices = learn_to_use,
        max_length = 20,
        verbose_name = 'learn_to_use',
        default=None,
        blank=False
    )
    
    system_inconvenient = models.CharField(
        choices = system_inconvenient,
        max_length = 20,
        verbose_name = 'system_inconvenient',
        default=None,
        blank=False
    )
    
    confident_level = models.CharField(
        choices = confident_level,
        max_length = 20,
        verbose_name = 'confident_level',
        default=None,
        blank=False
    )
    
    learning_before = models.CharField(
        choices = learning_before,
        max_length = 20,
        verbose_name = 'learning_before',
        default=None,
        blank=False
    )
    
    comment = models.CharField(max_length = 250,blank  = True)
    
    email = models.EmailField(max_length = 150,blank  = True)
    
    
    
    class Meta:
        verbose_name= 'UsabilitySurvey'
        ordering = ['user_id']
        db_table = 'UsabilitySurvey'
    def __str__(self):
        return self.title
