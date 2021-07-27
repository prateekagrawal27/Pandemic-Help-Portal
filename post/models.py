from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.fields import CharField

# Create your models here.

class mypost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    post_title = models.CharField(max_length=264, verbose_name="Enter Post Title")
    slug = models.SlugField(max_length=264, unique=True)
    City= models.CharField(max_length=264, verbose_name="Enter Your City",
    validators=[RegexValidator('^[A-Z]*$',
                               'Only uppercase letters allowed.')])
    Full_Adress= models.CharField(max_length=264, verbose_name="Enter Full adress") 
    phone_number = models.CharField(max_length=10,
    validators=[RegexValidator('^[0-9]*$', 'Only 0-9 are allowed!')]
    )
    post_text = models.TextField(verbose_name="Write about your requirement/service here")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    service_provider = models.BooleanField(default=False)
    #service_name=models.ForeignKey()
    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.post_title
# Create your models here.
class service_name(models.Model):
    name= models.CharField(max_length=150, verbose_name="Specify Service")

class Cities(models.Model):
    name=CharField(max_length=200,verbose_name="name of city")