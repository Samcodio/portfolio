from django.contrib import admin
from .models import TechstackBackend, TechstackFrontend, TechstackDatabases, TechstackTools, Projects

# Register your models here.


admin.site.register(TechstackBackend)
admin.site.register(TechstackFrontend)
admin.site.register(TechstackDatabases)
admin.site.register(TechstackTools)
admin.site.register(Projects)
