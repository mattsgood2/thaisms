from django.contrib import admin
from .models import Menu
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ['food_name', 'slug', 'price', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('food_name',)}

admin.site.register(Menu, MenuAdmin)


# class MenuAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("food_name",)}
