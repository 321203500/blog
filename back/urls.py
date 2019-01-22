
from django.urls import path

from back import views

urlpatterns = [
    # 主页面
    path('index/', views.index, name='index'),
    # 文章页面
    path('articles/', views.articles, name='articles'),
    # 添加文章
    path('add_article', views.add_article, name='add_article'),
    # 删除文章
    path('del_article/<int:id>', views.del_article, name='del_article'),
    # 更新文章
    path('update_article/<int:id>', views.update_article, name='update_article'),
    # 栏目页面
    path('category/', views.category, name='category'),
    # 删除栏目
    path('del_category/<int:id>', views.del_category, name='del_category'),
    # 更新栏目
    path('update_category/<int:id>', views.update_category, name='update_category'),
    # # 添加栏目
    # path('add_category/', views.add_category, name='add_category'),
]
