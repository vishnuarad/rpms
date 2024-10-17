from django.db import models

# Create your models here.
class teacher(models.Model) :
    email=models.EmailField()
    password=models.CharField(max_length=20)
class researchpapers(models.Model) :
    tname=models.CharField(max_length=30)
    tdept=models.CharField(max_length=20)
    tid=models.CharField(max_length=10)
    temail=models.CharField(max_length=30)
    ptitle=models.CharField(max_length=100)
    pdate=models.CharField(max_length=30)
    pdesc=models.CharField(max_length=100)
    pnat=models.CharField(max_length=20)
    ptype=models.CharField(max_length=20)
    pssn=models.CharField(max_length=20)
    pfield=models.CharField(max_length=30)
    plink=models.CharField(max_length=400)
