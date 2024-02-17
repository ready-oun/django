from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "age", "gender"]
    list_filter = ["age", "gender"]
    search_fields = ["name", "description"]