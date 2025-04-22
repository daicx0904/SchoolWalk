
from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    office_location = serializers.JSONField(
        source='office_location.coords',
        read_only=True
    )
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'
        extra_kwargs = {
            'office_location': {'write_only': True}
        }
