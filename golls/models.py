from django.db import models

# Create your models here.

class Golls(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

    
    class Meta:
        db_table = 'golls'

 
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hire_date = models.DateField()

    class Meta:
        db_table = 'teachers'
    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    class Meta:
        db_table = 'courses'
    def __str__(self):
        return self.title   
    
class Test(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    
    class Meta:
        db_table = 'tests'
    def __str__(self):
        return self.title       