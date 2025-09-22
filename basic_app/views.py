from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    DateDetailView,
    DeleteView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
)
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Task
from django.urls import reverse_lazy

# Create your views here.

# ===========================
# Authentication Views
# ===========================
@login_required
def user_logout(request):
    #"""
    #Logs out the current authenticated user
    #and redirects them to the home page.
    #"""
    logout(request)
    return redirect("basic_app:index")





def user_login(request):
    # """
    #Handles user login:
    #- If POST request, authenticate username and password.
    #- If user exists and active, log them in and redirect to index.
    #- Otherwise, return an error message.
    #- If GET request, render login form.
    #"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect("basic_app:index")
            else:
                return HttpResponse("The user is not active")
        else:
            return HttpResponse("The user is not exist")
    else:
        return render(request, "basic_app/login.html")


# class TaskListView(ListView):

# ===========================
# Generic Views
# ===========================
class IndexView(TemplateView):
    template_name = "basic_app/index.html"
    
    
class TaskListView(ListView):
    #"""
    #Displays a list of tasks for the currently logged-in user.
    #Only tasks belonging to the current user are retrieved.
    #"""
    model = Task

    def get_queryset(self):
        tasks = Task.objects.filter(user=self.request.user)
        return tasks

    context_object_name = "tasks"


class DeleteTaskView(DeleteView):
    #"""
    #Deletes a task.
    #After deletion, redirects to the task list page.
    #"""
    model = Task
    success_url = reverse_lazy("basic_app:task_list")


class TaskCreateView(CreateView):
    #"""
    #Allows the user to create a new task.
    #- Only logged-in users can create tasks.
    #- Automatically assigns the task to the current user.
    #"""
    model = Task
    fields = ("title", "description", "status")
    template_name = "basic_app/task_form.html"

    def form_valid(self, form):
        #"""
        #Automatically set the user of the task to the currently logged-in user.
        #"""
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("basic_app:task_list")


class TaskUpdateView(UpdateView):
    #"""
    #Allows the user to update an existing task.
    #After update, redirects to the task list page.
    #"""
    model = Task
    fields = ("title", "description", "status")
    success_url = reverse_lazy("basic_app:task_list")
