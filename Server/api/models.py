
from django.contrib.gis.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.JSONField()  # 格式：{"days": ["Mon", "Wed"], "time": "14:00-16:00"}
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('graduated', 'Graduated'),
        ('suspended', 'Suspended'),
    ]
    
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    office_location = models.PointField(srid=4326)  # 使用WGS84坐标系
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name
