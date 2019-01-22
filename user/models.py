from django.db import models


# 定义后台用户表模型
class User(models.Model):
    username = models.CharField(max_length=10, unique=True, null=False)
    password = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_user'
