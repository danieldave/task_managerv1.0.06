from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomRegistrationForm
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from.models import Task
            #from django.contrib.auth.models import User

class CustomRegistrationView(View):
    template_name = 'manager/registration.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('tasks')
        
        form = CustomRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new user with the submitted data
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # You can add additional logic here like sending a confirmation email, login, etc.
            return redirect('tasks')  # Define this URL in your urls.py

        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    template_name = 'manager/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(receiver=self.request.user)
        context['count'] = context['tasks'].filter(is_completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            #context['tasks'] = context['tasks'].filter(title__icontains=search_input)
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input

        return context 


class TaskDetail(LoginRequiredMixin,  DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'manager/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'sender', 'priority', 'attachments', 'receiver', 'due_date']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # Customize the label for the "due_date" field
        form.fields['due_date'].label = "Due Date (Format: YYYY-MM-DD)"

        return form

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['is_completed', 'comments', 'attachments', ]

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'manager/confirm_delete.html'

