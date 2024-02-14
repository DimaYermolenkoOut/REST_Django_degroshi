from datetime import datetime, timedelta
from django.contrib import admin
from django.db import models

from main.models import Expense, Category
from main.views import TotalExpensesView

# admin.site.register(Category)
admin.site.site_header = 'Degroshi'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_expenses')

    def total_expenses(self, obj):
        # Получаем общие расходы для данной категории, используя представление API
        total_expenses_data = TotalExpensesView.get_expenses_by_category()
        # Ищем общие расходы для данной категории в полученных данных
        category_expenses = next((item['total_amount'] for item in total_expenses_data if item['category_name'] == obj.name), 0)
        return category_expenses

    total_expenses.short_description = 'Total Expenses'


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description','category', 'amount', 'date','total_expenses_week')
    list_select_related = ('category', 'user')


    def category(self, obj):
        return obj.category.name

    category.short_description = 'Category'
    category.admin_order_field = 'category'


    def total_expenses_week(self, request):
        # Отримуємо поточну дату
        today = datetime.now().date()
        # Обчислюємо дату, що знаходиться за тиждень назад
        week_ago = today - timedelta(days=7)
        # Фільтруємо витрати за останній тиждень
        expenses_week = Expense.objects.filter(date__gte=week_ago, date__lte=today)
        # Обчислюємо загальну суму витрат за останній тиждень
        total_week = expenses_week.aggregate(total=models.Sum('amount'))['total']
        return str(total_week) if total_week is not None else "0"

    total_expenses_week.short_description = 'Total Expenses This Week'


# admin.site.register(Expense, ExpenseAdmin)
