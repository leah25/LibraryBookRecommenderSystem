from django.contrib import admin
from .models import Category, Book


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title','category', 'slug', 'author', 'field_of_study', 'stock', 'available', 'created_at', 'updated_at','shelf_no']
    list_filter = ['category','available', 'created_at', 'updated_at']
    list_editable = ['stock', 'available']
    

admin.site.register(Book, BookAdmin)
admin.site.site_header = "My Book Inventory ";
admin.site.site_title = "My Book Inventory ";
admin.site.index_title = "My library administration"