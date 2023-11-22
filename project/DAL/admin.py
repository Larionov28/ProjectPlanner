from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Region, Role, Article

admin.site.register(Region)
admin.site.register(Role)
admin.site.register(Article)

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'region', 'role')  # Определите поля, которые должны отображаться в списке
    list_filter = ('region', 'role')  # Добавьте фильтр по полю "region"
    search_fields = ('username', 'email')  # Добавьте поле для поиска
