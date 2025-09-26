# admin.py
from django.contrib import admin
from .models import Portfolio, Experience, Awards, Skills

admin.site.register(Portfolio)
admin.site.register(Experience)
admin.site.register(Awards)
admin.site.register(Skills)
