from django.contrib import admin
from .models import MathClass, MathSection

# Реєстрація моделей для адміністративного інтерфейсу
admin.site.register(MathClass)
admin.site.register(MathSection)
