from django.db import models


class NewsType(models.Model):
    tid = models.AutoField(primary_key=True)
    tName = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'NewsType'



class NewsInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    tid = models.ForeignKey(NewsType, on_delete=models.CASCADE)
    nTitle = models.CharField(max_length=200)
    nAuthor = models.CharField(max_length=20)
    nContent = models.CharField(max_length=1000)
    nPubDateTime = models.DateTimeField(auto_now_add=True)
    NStatus = models.BooleanField()
    class Meta:
        db_table = 'NewsInfo'


class Login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'Login'
