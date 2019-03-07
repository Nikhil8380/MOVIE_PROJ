from django.db import models
from django.contrib.auth.models import User


class Movies(models.Model):
    REGION = (
        ('Bollywood', 'Bollywood'),
        ('Hollywood', 'Hollywood'),
        ('Tollywood', 'Tollywood')
    )

    admin=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=20,unique=True)
    image=models.ImageField(upload_to='media2/prof_pic')
    Region=models.CharField(choices=REGION,max_length=30)
    rating=models.IntegerField()
    Release_year=models.DateTimeField()
    summary=models.TextField()
    Lead_Actor=models.CharField(max_length=15)
    Lead_Actress=models.CharField(max_length=15)
    director=models.CharField(max_length=15)
    Producer=models.CharField(max_length=15)

    class Meta:
        ordering = ('-Release_year',)



# Create your models here.
