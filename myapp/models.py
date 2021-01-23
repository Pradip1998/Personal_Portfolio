from django.db import models
from django.db import models
import datetime

# Create your models here.
class Education(models.Model):
    date=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    desc=models.TextField()

    def __str__(self):
        return self.course

class Experience(models.Model):
    date=models.CharField(max_length=100)
    framework=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    desc=models.TextField(max_length=100)
    def __str__(self):
        return self.framework


class Award(models.Model):
    date = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)

    def __str__(self):
        return self.title

class About(models.Model):
    desc = models.TextField()
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    projectcom=models.IntegerField()
    img = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name

class Number(models.Model):
    topic=models.CharField(max_length=100)
    num=models.IntegerField()
    def __str__(self):
        return self.topic



class Project(models.Model):
    title=models.CharField(max_length=50)
    work=models.CharField(max_length=50)
    imgg=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.work



class Query(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    mesg = models.TextField()

    class Meta:
        db_table = "myapp_query"

    def __str__(self):
        return self.name

class Catagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True,null=True)
    bwriteby = models.CharField(max_length=50)
    paragraph = models.TextField()
    desc = models.CharField(max_length=200)
    catagory = models.ManyToManyField(Catagory)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email = models.EmailField()
    cmnt=models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return '%s - %s' % (self.post_id,self.name)


class Skill(models.Model):
    skillname=models.CharField(max_length=100)
    skillper=models.IntegerField()
    lastweek=models.IntegerField()
    lastmonth=models.IntegerField()
    def __str__(self):
        return self.skillname

class Image(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name





