
from django.db import models

class Info(models.Model):
    uname = models.TextField()
    upassword = models.TextField()

class Meta():
    db_table = 'emp_info'
