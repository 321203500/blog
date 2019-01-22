
from django.urls import path

from user import views

urlpatterns = [
    # 注册界面
    path('register/', views.register, name='register'),
    # 登录界面
    path('login/', views.login, name='login'),
    # 登出
    # path('logout/', views.logout, name='logout'),
]
