from django.contrib import admin
from .models import Pass
# Register your models here.

class PassAdmin(admin.ModelAdmin):
    list_display = ('site', 'username', 'password', 'owner')
    search_fields = ('username', 'site',)
    list_filter = ('username', 'site',)
    list_display_links = ('username', 'site',)
    fields = ('owner', 'site', 'username', 'password')

admin.site.register(Pass, PassAdmin)