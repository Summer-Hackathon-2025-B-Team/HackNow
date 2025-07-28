from django.shortcuts import render
from django.views.generic import ListView
from .models import Course

class ListCourseView(ListView):
    template_name = 'course/index.html'
    model = Course
