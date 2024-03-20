"""
URL configuration for degroshi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import djoser
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main import views
from main.views import TotalExpensesView, celery_view
from main.views import CategotyAPIList, TotalExpensesView
from django.urls import path

from .yasg import urlpatterns as doc_urls


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'expenses', views.ExpenseViewSet)
router.register(r'categories', views.CategoryViewSet)
# router.register(r'total-expenses', views.TotalExpensesView, basename='total_expenses')

# print(router.urls)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # path(r'^auth/', include('djoser.urls')),


    # path('api/v1/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/v1/', CategotyAPIList.as_view()),
    # path('api/v1/<int:pk>/', CategotyAPIList.as_view()),
    path('', include(router.urls)),
    path('total-expenses/', TotalExpensesView.as_view(), name='total_expenses'),
    # path('expenses_by_day/', TotalExpensesView.as_view(), name='expenses_by_day'),
    # path('expenses_by_user/', TotalExpensesView.as_view(), name='expenses_by_user'),

    path('total-expenses/', views.TotalExpensesView.as_view(), {'get': 'get_total_expenses'}),
    # URL для общих расходов
    path('expenses-by-day/', views.TotalExpensesView.as_view(), {'get': 'get_expenses_by_day'},
         name='expenses_by_day'),  # URL для расходов по дням
    path('expenses-by-user/', views.TotalExpensesView.as_view(), {'get': 'get_expenses_by_user'},
         name='expenses_by_user'),  # URL для расходов по пользователям
    path('celery/', celery_view, name='celery'),
    path('celery_debag/', views.celery_debag, name='celery_debag'),
]
urlpatterns +=router.urls
urlpatterns += doc_urls


