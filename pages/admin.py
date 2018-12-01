from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    """Django admin ModelAdmin for data model Page"""
    list_display = ('page_name','update_date')
    ordering = ('page_name',)
    search_fields = ('page_name',)


admin.site.register(Page, PageAdmin)
