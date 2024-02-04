from datetime import datetime, timedelta
from django.contrib import admin
from main.models import Expense, Category

admin.site.register(Category)
admin.site.site_header = 'Degroshi'


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date')

    def total_expenses_week(self, request):
        # Отримуємо поточну дату
        today = datetime.now().date()
        # Обчислюємо дату, що знаходиться за тиждень назад
        week_ago = today - timedelta(days=7)
        # Фільтруємо витрати за останній тиждень
        expenses_week = Expense.objects.filter(date__gte=week_ago, date__lte=today)
        # Обчислюємо загальну суму витрат за останній тиждень
        total_week = expenses_week.aggregate(total=models.Sum('amount'))['total']
        return total_week

    total_expenses_week.short_description = 'Total Expenses This Week'


admin.site.register(Expense, ExpenseAdmin)
