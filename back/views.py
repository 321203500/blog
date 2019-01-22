import random

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from back.forms import ArticlesForm, AddColumnForm, UpdateColumnForm
from back.models import Articles, Column
from user.models import User


def index(request):
    user = User.objects.get(pk=1)
    return render(request, 'back/index.html', {'user': user})


def articles(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        all_articles = Articles.objects.filter(is_delete=0)
        count = len(all_articles)
        articles = []
        for article in all_articles:
            column = Column.objects.get(id=article.a_column_id)
            name = column.column_name
            articles.append([article, name])
        pg = Paginator(articles, 8)
        articles = pg.page(page)
        return render(request, 'back/article.html', {'articles': articles, 'count': count})


def add_article(request):
    if request.method == 'GET':
        user = User.objects.get(pk=1)
        first_level = Column.objects.filter(pid_id=None)
        column_list = []
        for item in first_level:
            secone_level = Column.objects.filter(pid_id=item.id)
            data = [item, secone_level]
            column_list.append(data)
        return render(request, 'back/add_article.html', {'user': user, 'column_list': column_list})
    if request.method == 'POST':
        # 获取表单提交数据，并保存到数据库，跳转文章界面
        article = ArticlesForm(request.POST, request.FILES)
        if article.is_valid():
            title = article.cleaned_data['title']
            content = article.cleaned_data['content']
            keywords = article.cleaned_data['keywords']
            describe = article.cleaned_data['describe']
            tags = article.cleaned_data['tags']
            # image = article.cleaned_data['image']
            is_public = article.cleaned_data['is_public']
            a_column_id = int(article.cleaned_data['category'])
            image = str(random.randint(1, 14)) + '.jpg'
            Articles.objects.create(title=title,
                                    content=content,
                                    keywords=keywords,
                                    describe=describe,
                                    tags=tags,
                                    image=image,
                                    is_public=is_public,
                                    a_column_id=a_column_id)
            return HttpResponseRedirect(reverse('back:articles'))
        else:
            errors = article.errors
            return render(request, 'back/add_article.html', {'errors': errors})


def del_article(request, id):
    if request.method == 'GET':
        article = Articles.objects.filter(pk=id).first()
        article.is_delete = 1
        article.save()
        return HttpResponseRedirect(reverse('back:articles'))


def update_article(request, id):
    if request.method == 'GET':
        first_level = Column.objects.filter(pid_id=None)
        column_list = []
        for item in first_level:
            secone_level = Column.objects.filter(pid_id=item.id)
            data = [item, secone_level]
            column_list.append(data)
        article = Articles.objects.filter(pk=id).first()
        return render(request, 'back/update_article.html', {'article': article, 'column_list': column_list})
    if request.method == 'POST':
        # 获取表单提交修改后的数据，并保存到数据库，跳转文章界面
        article = ArticlesForm(request.POST, request.FILES)
        if article.is_valid():
            title = article.cleaned_data['title']
            content = article.cleaned_data['content']
            keywords = article.cleaned_data['keywords']
            describe = article.cleaned_data['describe']
            tags = article.cleaned_data['tags']
            # image = article.cleaned_data['image']
            image = str(random.randint(1, 14)) + '.jpg'
            is_public = article.cleaned_data['is_public']
            a_column_id = article.cleaned_data['category']
            # 更新文章数据
            Articles.objects.filter(pk=id).update(title=title,
                                                  content=content,
                                                  keywords=keywords,
                                                  describe=describe,
                                                  tags=tags,
                                                  image=image,
                                                  is_public=is_public,
                                                  a_column_id=a_column_id)
            return HttpResponseRedirect(reverse('back:articles'))
        else:
            errors = article.errors
            return render(request, 'back/update_article.html', {'errors': errors})


def category(request):
    if request.method == 'GET':
        columns = Column.objects.all()
        column_count = len(columns)
        return render(request, 'back/category.html', {'columns': columns, 'column_count': column_count})
    if request.method == 'POST':
        # 获取表单提交修改后的数据，并保存到数据库，跳转栏目界面
        column = AddColumnForm(request.POST, request.FILES)
        if column.is_valid():
            column_name = column.cleaned_data['name']
            another_name = column.cleaned_data['alias']
            c_describe = column.cleaned_data['describe']
            c_keywords = column.cleaned_data['keywords']
            pid_id = column.cleaned_data.get('fid', None)
            # 更新文章数据
            Column.objects.create(column_name=column_name,
                                  another_name=another_name,
                                  c_describe=c_describe,
                                  c_keywords=c_keywords,
                                  pid_id=pid_id)
        return HttpResponseRedirect(reverse('back:category'))


def del_category(request, id):
    if request.method == 'GET':
        Column.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('back:category'))


def update_category(request, id):
    if request.method == 'GET':
        columns = Column.objects.all()
        del_column = Column.objects.get(pk=id)
        return render(request, 'back/update_category.html', {'columns': columns, 'del_column': del_column})
    if request.method == 'POST':
        # 获取表单提交修改后的数据，并保存到数据库，跳转文章界面
        column = UpdateColumnForm(request.POST, request.FILES)
        if column.is_valid():
            column_name = column.cleaned_data['name']
            another_name = column.cleaned_data['alias']
            c_describe = column.cleaned_data['describe']
            c_keywords = column.cleaned_data['keywords']
            pid_id = column.cleaned_data.get('fid', None)
            # 更新文章数据
            Column.objects.filter(pk=id).update(column_name=column_name,
                                                another_name=another_name,
                                                c_describe=c_describe,
                                                c_keywords=c_keywords,
                                                pid_id=pid_id)
            return HttpResponseRedirect(reverse('back:category'))
        else:
            errors = column.errors
            return render(request, 'back/update_article.html', {'errors': errors})
