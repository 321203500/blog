from django.shortcuts import render

from back.models import Articles, Column


def index(request):
    if request.method == 'GET':
        articles = Articles.objects.filter(is_delete=0)
        columns = Column.objects.filter()
        columns_list = []
        for column in columns:
            count = len(Articles.objects.filter(a_column_id=column.id))
            columns_list.append([count, column])
        return render(request, 'web/index.html', {'articles': articles, 'columns_list': columns_list})


def article_detail(request, id):
    if request.method == 'GET':
        articles = Articles.objects.filter(is_delete=0)
        columns = Column.objects.filter()
        columns_list = []
        for column in columns:
            count = len(Articles.objects.filter(a_column_id=column.id))
            columns_list.append([count, column])
        article = Articles.objects.get(pk=id)
        return render(request, 'web/article_detail.html', {'article': article, 'articles': articles, 'columns_list': columns_list})


def column_detail(request, id):
    if request.method == 'GET':
        articles = Articles.objects.filter(is_delete=0)
        columns = Column.objects.filter()
        columns_list = []
        for column in columns:
            count = len(Articles.objects.filter(a_column_id=column.id))
            columns_list.append([count, column])
        column_articles = Articles.objects.filter(a_column_id=id)
        return render(request, 'web/column_detail.html', {'articles': articles, 'columns_list': columns_list, 'column_articles': column_articles})


def share(request):
    return render(request, 'web/share.html')


def about(request):
    if request.method == 'GET':
        articles = Articles.objects.filter(is_delete=0)
        columns = Column.objects.filter()
        columns_list = []
        for column in columns:
            count = len(Articles.objects.filter(a_column_id=column.id))
            columns_list.append([count, column])
        return render(request, 'web/about.html', {'articles': articles, 'columns_list': columns_list})


def gbook(request):
    if request.method == 'GET':
        articles = Articles.objects.filter(is_delete=0)
        columns = Column.objects.filter()
        columns_list = []
        for column in columns:
            count = len(Articles.objects.filter(a_column_id=column.id))
            columns_list.append([count, column])
        return render(request, 'web/gbook.html', {'articles': articles, 'columns_list': columns_list})


def info(request):
    if request.method == 'GET':
        articles = Articles.objects.filter(is_delete=0)
        columns = Column.objects.filter()
        columns_list = []
        for column in columns:
            count = len(Articles.objects.filter(a_column_id=column.id))
            columns_list.append([count, column])
        return render(request, 'web/info.html', {'articles': articles, 'columns_list': columns_list})


def infopic(request):
    if request.method == 'GET':
        articles = Articles.objects.filter(is_delete=0)
        columns = Column.objects.filter()
        columns_list = []
        for column in columns:
            count = len(Articles.objects.filter(a_column_id=column.id))
            columns_list.append([count, column])
        return render(request, 'web/infopic.html', {'articles': articles, 'columns_list': columns_list})


def alist(request):
    if request.method == 'GET':
        articles = Articles.objects.filter(is_delete=0)
        columns = Column.objects.filter()
        columns_list = []
        for column in columns:
            count = len(Articles.objects.filter(a_column_id=column.id))
            columns_list.append([count, column])
        return render(request, 'web/list.html', {'articles': articles, 'columns_list': columns_list})
