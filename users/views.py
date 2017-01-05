from django.shortcuts import render
from Models import Course, Comment, User
from django.views.generic import View
from django.forms import forms
from forms import CreateForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.conf.urls import url
from django.views.generic import TemplateView
from django.views import View

from django.http import HttpResponse, JsonResponse

from django.http import Http404
from django.views.generic.detail import DetailView

# local imports

from django.core.files import File
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'index.html')


def sub(request):
    user = User.objects.get(pk=1)
    course = Course.objects.get(id=3)
    user.courses.add(course)
    return redirect('/')


def index1(request):
    return render(request, 'index2.html')


def createcourse(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            return redirect(reverse("Course", kwargs={"pk": course.pk}))
    else:
        form = CreateForm()
    return render(request, 'createcourses.html', {'form': form})


def Login(request):
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors.append('Enter login')

        password = request.POST.get('password')
        if not password:
            errors.append('Enter password')

        user = authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('/course/')
        else:
            errors.append('Incorrect login or password')
        return render(request, 'index1.html', {'errors': errors, 'username': username})

    return render(request, 'index1.html', {'errors': errors})


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def Registration(request):
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors.append('Enter login')

        if len(str(username)) < 5:
            errors.append('So small login (5)')

        password = request.POST.get('password')
        if len(str(password)) < 6:
            errors.append('So small password (6)')

        password2 = request.POST.get('password2')
        if password != password2:
            errors.append('Different passwords')

        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        if (not username) or (not password) or (not password2) or (not first_name) or (not last_name):
            errors.append('Fill all fields')
        else:
            if len(errors) == 0:
                users = User.objects.filter(username=username)
                if len(users) != 0:
                    errors.append('Login used')
                    return render(request, 'registrations1.html', {'errors': errors, 'username': username,
                                                                   'last_name': last_name, 'first_name': first_name})
                else:
                    u = User()
                    u.username = username
                    u.password = make_password(password)
                    u.last_name = last_name
                    u.first_name = first_name
                    u.is_staff = False
                    u.is_active = True
                    u.is_superuser = False
                    u.save()
            return HttpResponseRedirect('/course/')

        return render(request, 'registrations1.html', {'errors': errors, 'username': username,
                                                       'last_name': last_name, 'first_name': first_name})

    return render(request, 'registrations1.html', {'errors': errors})


class Online(TemplateView):
    template_name = 'Course.html'

    def get_context_data(self, **kwargs):
        Courses = Course.objects.all()
        context = dict(Courses=Courses)
        return context


class Test(TemplateView):
    template_name = 'Login.html'

    def get_context_data(self, **kwargs):
        iol = User.objects.all()
        context = dict(User=iol)
        return context

class PostView(DetailView):
    model = Course
    context_object_name = 'Course'
    template_name = 'OneCourse.html'

    def get_object(self):
        object = super(PostView, self).get_object()
        if not self.request.user.is_authenticated():
            raise Http404
        return object
