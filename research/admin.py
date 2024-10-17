from django.contrib import admin

# Register your models here.
from research.models import teacher,researchpapers

admin.site.register(teacher)
admin.site.register(researchpapers)

