from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Course
from .forms import CourseForm

class ListCourseView(ListView):
    template_name = 'course/index.html'
    model = Course
    ordering = ["-created_at"]

class CreateCourseView(CreateView):
    form_class = CourseForm
    template_name = 'course/create.html'
    model = Course
    success_url = reverse_lazy("course:index")

class EditCourseView(UpdateView):
    form_class = CourseForm
    template_name = 'course/edit.html'
    model = Course
    success_url = reverse_lazy("course:index")
