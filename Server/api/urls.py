
from django.urls import path
from .views import *

urlpatterns = [
    # 学生
    path('students/', StudentListCreate.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
    path('students/<int:pk>/schedule/', StudentScheduleView.as_view()),
    
    # 教师
    path('teachers/', TeacherListCreate.as_view()),
    path('teachers/<int:pk>/', TeacherDetail.as_view()),
    
    # 课程
    path('courses/', CourseListCreate.as_view()),
    path('courses/<int:pk>/', CourseDetail.as_view()),
]
