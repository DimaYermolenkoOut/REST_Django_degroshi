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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main import views
from main.views import CategotyAPIList, TotalExpensesView
from django.urls import path



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'expenses', views.ExpenseViewSet)
router.register(r'categories', views.CategoryViewSet)
# router.register(r'total-expenses', views.TotalExpensesView, basename='total_expenses')

# print(router.urls)

urlpatterns = [

    path('admin/', admin.site.urls),

    # path('api/v1/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/v1/', CategotyAPIList.as_view()),
    # path('api/v1/<int:pk>/', CategotyAPIList.as_view()),
    path('', include(router.urls)),
    path('total-expenses/', TotalExpensesView.as_view(), name='total_expenses'),

]
urlpatterns +=router.urls


