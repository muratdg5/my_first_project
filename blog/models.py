from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class IndexHero(models.Model):
    text=models.CharField(max_length=200)
    text_one=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    button1=models.CharField(max_length=100)
    is_home=models.BooleanField()

class IndexSection(models.Model):
    text=models.CharField(max_length=200)
    description=models.TextField()
    text_one=models.CharField(max_length=200)
    text_two=models.CharField(max_length=200)
    text_three=models.CharField(max_length=200)
    description_one=models.TextField()
    image=models.ImageField(upload_to='index')
    is_home=models.BooleanField()

    

class IndexCounts(models.Model):
    name_student=models.CharField(max_length=100)
    name_student_sayi=models.IntegerField()
    name_courses=models.CharField(max_length=100)
    name_courses_sayi=models.IntegerField()
    name_trainers=models.CharField(max_length=100)
    name_trainers_sayi=models.IntegerField()
    is_home=models.BooleanField()
    

class IndexWhysection(models.Model):
    name=models.CharField(max_length=200)
    content=models.TextField()
    button1=models.CharField(max_length=100)
    is_home=models.BooleanField()



class Courses(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    content=models.CharField(max_length=200)
    description=RichTextField()
    name=models.CharField(max_length=100)
    like=models.IntegerField()
    like_two=models.IntegerField()
    image=models.ImageField(upload_to='courses')
    image_teacher=models.ImageField(upload_to='trainers')
    is_home=models.BooleanField()
    slug=models.SlugField(null=True, blank=True, unique=True, db_index=True)    

    
   

    def __str__(self):
        return f"{self.title}"

    def save(self, *args,**kwargs):
        self.slug =slugify(self.title)
        super().save(*args,**kwargs)

class Trainers(models.Model):
    name=models.CharField(max_length=100)
    job=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='trainers')
    is_home=models.BooleanField()

class Testimonials(models.Model):
    name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='testimonials')
