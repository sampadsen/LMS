from django.db import models

# Create your models here.
class userdetails(models.Model):
    SI_NO=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    id_1=models.IntegerField(max_length=100)

    class Meta:
        db_table='UserInfo'


        

class bookdata(models.Model):
    s_code=models.IntegerField(max_length=100)
    b_code=models.CharField(max_length=100)
    issue_date=models.CharField(max_length=100)
    return_date=models.CharField(max_length=100)

    class Meta:
        db_table='BookInfo'