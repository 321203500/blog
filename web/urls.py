
from django.urls import path
from django.contrib.staticfiles.urls import static

from myblog.settings import MEDIA_URL, MEDIA_ROOT
from web import views

urlpatterns = [
    # index主页
    path('index/', views.index, name='index'),
    # 文章详情
    path('article/<int:id>', views.article_detail, name='article_detail'),
    # 栏目/分类详情
    path('column/<int:id>', views.column_detail, name='column_detail'),
    # 我的相册页面
    path('share/', views.share, name='share'),

    path('about/', views.about, name='about'),
    path('gbook/', views.gbook, name='gbook'),
    path('info/', views.info, name='info'),
    path('infopic/', views.infopic, name='infopic'),
    path('alist/', views.alist, name='alist'),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
