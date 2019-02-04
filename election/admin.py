from django.contrib import admin

from .models import Conseil, Bureau

@admin.register(Bureau)
class BureauAdmin(admin.ModelAdmin):
    pass

# Register your models here.
