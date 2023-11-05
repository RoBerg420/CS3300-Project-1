from django.contrib import admin
from .models import Student
from .models import Portfolio
from .models import Project

# Register your models here.
admin.site.register(Student)
admin.site.register(Portfolio)
admin.site.register(Project)

