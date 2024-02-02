from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import viewsets, permissions, generics

from .models import Expense, Category
from .serializers import GroupSerializer, UserSerializer, ExpenseSerializer, CategorySerializer


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





