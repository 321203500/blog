from django.db import models


class Column(models.Model):
    column_name = models.CharField(max_length=10, unique=True)
    another_name = models.CharField(max_length=10, unique=True)
    c_describe = models.CharField(max_length=100)
    c_keywords = models.CharField(max_length=30, null=True)
    pid = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'tb_column'


class Articles(models.Model):
    # 文章标题
    title = models.CharField(max_length=30, unique=True)
    # 文章内容
    content = models.TextField()
    # 文章关键字
    keywords = models.CharField(max_length=20, null=True)
    # 文章描述
    describe = models.CharField(max_length=255)
    # 文章标签
    tags = models.CharField(max_length=20, null=True)
    # 文章图片
    image = models.ImageField(upload_to='static/back/images/arclist', null=True)
    # 文章是否公开
    is_public = models.BooleanField(null=False, default=1)
    # 文章创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 文章更新时间
    update_time = models.DateTimeField(auto_now=True)
    # 文章所属栏目
    a_column = models.ForeignKey(Column, null=True, on_delete=models.PROTECT)
    # 文章是否处于软删除状态
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'tb_articles'
