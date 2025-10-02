from django.contrib import admin
from .models import User, Product, Category

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "role", "is_active", "is_staff")
    search_fields = ("email", "full_name")
    list_filter = ("role", "is_active")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "seller", "category")  # use actual field names
    search_fields = ("title", "description")
    list_filter = ("seller", "category")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
