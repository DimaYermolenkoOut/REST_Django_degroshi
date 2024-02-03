from django.contrib import admin

from main.models import Expense, Category

admin.site.register(Expense)
admin.site.register(Category)
admin.site.site_header = 'Degroshi'