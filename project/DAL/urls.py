from django.urls import path, include

from .views import Register
from . import views

from django.contrib.auth import views as auth_views

from .views import EditProfileChangePassword, UserCreateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
    path('edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('change_password/', EditProfileChangePassword.as_view(), name='change_password'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('user_list/', views.UserListView.as_view(), name='user_list'),
    path('user_edit/<int:pk>/', views.UserUpdateView.as_view(), name='user_edit'),
    path('user_delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),

    path('article_list/', views.ArticleListView.as_view(), name='article_list'),
    path('article_create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article_edit/<int:pk>/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article_delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='article_delete'),

    path('session_limit/', views.session_limit, name='session_limit'),

    path('company_list/', views.CompanyListView.as_view(), name='company_list'),
    path('company_edit/<int:pk>/', views.CompanyUpdateView.as_view(), name='company_edit'),
    path('company_delete/<int:pk>/', views.CompanyDeleteView.as_view(), name='company_delete'),
    path('company/create/', views.CompanyCreateView.as_view(), name='company_create'),

    path('task_list/', views.TaskListView.as_view(), name='task_list'),
    path('task_create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task_edit/<int:pk>/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('task_delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),
]
