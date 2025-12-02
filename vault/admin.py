from django.contrib import admin
from .models import Pass
# Register your models here.

class PassAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'owner')
    search_fields = ('username', )
    list_filter = ('username',)
    list_display_links = ('username',)
    fields = ('owner', 'username', 'password')

admin.site.register(Pass, PassAdmin)