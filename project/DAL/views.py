from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.views import View
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, CustomUserEditForm
from django.contrib import messages
from .models import User, Article, Task, Company
from .forms import ArticleForm, UserEditForm
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.shortcuts import render
from django.urls import reverse_lazy


class UserListView(View):
    template_name = 'registration/user_list.html'

    def get(self, request):
        if request.user.is_superuser or request.user.role.name == 'Админ' or request.user.role.name == 'Руководитель':
            users = User.objects.all()
            return render(request, self.template_name, {'users': users})
        else:
            return render(request, 'access_denied.html')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'registration/user_edit.html'
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'registration/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')


class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/user_create.html'
    success_url = reverse_lazy('user_list')


class ArticleListView(View):
    template_name = 'registration/article_list.html'

    def get(self, request):
        articles = Article.objects.all()
        return render(request, self.template_name, {'articles': articles})


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'registration/article_create.html'
    fields = '__all__'
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Устанавливаем текущего пользователя как автора
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'registration/article_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('article_list')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'registration/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')


class CompanyListView(View):
    template_name = 'registration/company_list.html'

    def get(self, request):
        if request.user.is_superuser or request.user.role.name == 'Админ' or request.user.role.name == 'Руководитель':
            companies = Company.objects.all()
            return render(request, self.template_name, {'companies': companies})
        else:
            return render(request, 'access_denied.html')


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'registration/company_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('company_list')


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'registration/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')


class CompanyCreateView(CreateView):
    model = Company
    template_name = 'registration/company_create.html'
    fields = '__all__'
    success_url = reverse_lazy('company_list')


class TaskListView(View):
    template_name = 'registration/task_list.html'

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, self.template_name, {'tasks': tasks})


class TaskCreateView(CreateView):
    model = Task
    template_name = 'registration/task_create.html'
    fields = '__all__'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Устанавливаем текущего пользователя как автора
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'registration/task_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'registration/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': CustomUserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            selected_region = form.cleaned_data['region']
            user = form.save(commit=False)
            user.region = selected_region
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class EditProfile(View):
    template_name = 'registration/edit_profile.html'

    def get(self, request):
        form = CustomUserEditForm(instance=request.user)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправьте пользователя на страницу профиля или другую страницу
        context = {'form': form}
        return render(request, self.template_name, context)


class EditProfileChangePassword(PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('edit_profile')

    def form_valid(self, form):
        messages.success(self.request, 'Пароль успешно изменен.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'Ошибка в поле {field}: {error}')
        return super().form_invalid(form)


def session_limit(request):
    return render(request, 'session_limit.html')


