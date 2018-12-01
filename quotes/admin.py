from django.contrib import admin
from .models import Quote
# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    """Django admin ModelAdmin for data model Quote"""
    list_display = ('id','name','company','submitted','quotedate','quoteprice')
    list_filter = ('submitted','quotedate')
    readonly_fields = ('submitted',)
    fieldsets = (
        (None, {
            'fields': ('name','email','description')
        }),
        ('Contact information', {
            'classes':('collapse',),
            'fields':('position','company','address','phone','web')
        }),
        ('Job Information', {
            'classes':('collapse',),
            'fields':('sitestatus','priority','jobfile','submitted')
        }),
        ('QuoteAdmin', {
            'classes':('collapse',),
            'fields':('quotedate','quoteprice','username')
        }),
    )

admin.site.register(Quote,QuoteAdmin)
