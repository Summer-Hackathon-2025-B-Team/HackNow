from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Course
from .forms import CreateCourseForm

class ListCourseView(ListView):
    template_name = 'course/index.html'
    model = Course

class CreateCourseView(CreateView):
    form_class = CreateCourseForm
    template_name = 'course/create.html'
    model = Course
    success_url = reverse_lazy("course:index")
