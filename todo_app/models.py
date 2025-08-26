from django.db import models


# create table todo(
    # id int primary key auto_increment,
    # title varchar(200)
    #)   This code and below code are same for table 

# if there is any change in models.py, run following:
# 1. python manage.py makemigrations
# 2. python manage.py migrate

# Create your models here.
class Todo(models.Model):       #pascalcase
    title = models.CharField(max_length=200)   #varchar, char

# if we add function no need makemigration and migrate
    def __str__(self):
        return self.title



