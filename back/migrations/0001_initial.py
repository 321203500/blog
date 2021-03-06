# Generated by Django 2.1.5 on 2019-01-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('content', models.TextField()),
                ('kewords', models.CharField(max_length=20, null=True)),
                ('describe', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(upload_to='static/back/images/arclist')),
                ('is_public', models.BooleanField(default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'tb_articles',
            },
        ),
    ]
