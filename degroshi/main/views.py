from django.http import HttpResponse
from main.tasks import hello_world_task
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import viewsets, permissions, generics


from .models import Expense, Category
from .serializers import GroupSerializer, UserSerializer, ExpenseSerializer, CategorySerializer

from django.db.models import Sum
from django.db.models.functions import TruncDay, TruncMonth, TruncYear
from datetime import datetime

from .serializers import ExpenseSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



class UserViewSet(viewsets.ModelViewSet):
    '''
    Кінцева точка API, яка дозволяє переглядати або редагувати користувачів.
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    '''
    Кінцева точка API, яка дозволяє переглядати та редагувати групи.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permissions_classes = [permissions.IsAuthenticated]

class CategotyAPIList(generics.ListCreateAPIView):
    '''
    Кінцева точка API, яка дозволяє переглядати та редагувати категорії.
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryViewSet(viewsets.ModelViewSet):
    '''
    Кінцева точка API, яка дозволяє переглядати та редагувати категорії.
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permissions_classes = [permissions.IsAuthenticated]


class ExpenseViewSet(viewsets.ModelViewSet):
    '''
    Кінцева точка API, яка дозволяє переглядати та редагувати витрати.
    '''
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permissions_classes = [permissions.IsAuthenticated]


class TotalExpensesView(APIView):
    #
    # def get_total_expenses(self):
    #     return Expense.objects.aggregate(total=Sum('amount'))['total']
    #
    # def get_expenses_by_category(self):
    #     return Expense.objects.values('category__name').annotate(total=Sum('amount'))
    #
    # def get_expenses_by_user(self):
    #     return Expense.objects.values('user__username').annotate(total=Sum('amount'))
    #
    # def get_expenses_by_day(self):
    #     return Expense.objects.annotate(day=TruncDay('date')).values('day').annotate(total=Sum('amount'))
    #
    # def get_expenses_by_month(self):
    #     return Expense.objects.annotate(month=TruncMonth('date')).values('month').annotate(total=Sum('amount'))
    #
    # def get_expenses_by_year(self):
    #     return Expense.objects.annotate(year=TruncYear('date')).values('year').annotate(total=Sum('amount'))
    #
    # def get(self, request):
    #     data = {
    #         'total_expenses': self.get_total_expenses(),
    #         'expenses_by_category': self.get_expenses_by_category(),
    #         'expenses_by_user': self.get_expenses_by_user(),
    #         'expenses_by_day': self.get_expenses_by_day(),
    #         'expenses_by_month': self.get_expenses_by_month(),
    #         'expenses_by_year': self.get_expenses_by_year()
    #     }
    #     return Response(data)

    def get_expenses_by_category():
        # Отримуємо суму витрат для кожної категорії
        expenses_by_category = Expense.objects.values('category__name').annotate(total_amount=Sum('amount'))

        # Перетворимо результат у потрібний формат для виведення
        expenses_data = [{'category_name': item['category__name'], 'total_amount': item['total_amount']} for item in
                         expenses_by_category]

        return expenses_data

    def get(self, request):
        data = {
            'expenses_by_category': self.get_expenses_by_category(),
        }
        return Response(data)


def celery_view(*args, **kwargs):
    hello_world_task.delay()
    return HttpResponse('ok')