from ast import IsNot
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Course
from .forms import CourseForm
# Create your views here.

class CourseUpdateView(View):
    template_name = 'courses/courses_form.html'
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id = id)
        return obj
    
    def get (self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseForm(instance= obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
    
    def post  (self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseForm(request.POST, instance = obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    # def post (self, request, *args, **kwargs):
    #     form = CourseForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         form = CourseForm()
    #     context = {'form' : self.form}             
    #     return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/courses_form.html'
    form = CourseForm()
    def get (self, request, *args, **kwargs):
        context = {'form' : self.form}             
        return render(request, self.template_name, context)

    def post (self, request, *args, **kwargs):
        form = CourseForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = CourseForm()
        context = {'form' : self.form}             
        return render(request, self.template_name, context)


class CourseView(View):
    template_name = 'courses/courses_detail.html'
    def get (self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id = id) 
            context['object'] = obj
        return render(request, self.template_name, context)
 
class CourseListView(View):
    template_name = 'courses/courses_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get (self, request, *args, **kwargs):
        context = {}
        context = {'object_list' : self.get_queryset()}
        return render(request, self.template_name, context)

class MyListView(CourseListView):
    queryset = Course.objects.filter(id = 1)

class CourseDetailView(View):
    template_name = 'courses/courses_detail.html'
    def get (self, request, *args, **kwargs):
        return render(request, self.template_name, {})

# def f_bv (request, *args, **kwargs):
#     return render(request, 'courses/about.html', {})


class CourseDeleteView(View):
    template_name = 'courses/courses_delete.html'
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id = id)
        return obj
    
    def get (self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)
    
    def post  (self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/list/')
        return render(request, self.template_name, context)