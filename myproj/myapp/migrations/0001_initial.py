# Generated by Django 4.2.2 on 2023-07-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buy_tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('id_tech', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(max_length=200)),
                ('nickname', models.TextField(max_length=200, unique=True)),
                ('avatar', models.ImageField(upload_to='C:/Users/Stud1/Documents/Sekrier/djangotest/myproj/myapp/static/img')),
                ('specialization', models.TextField(max_length=2000, verbose_name=True)),
                ('experience', models.TextField(max_length=2000)),
                ('service', models.TextField(max_length=2000)),
                ('price', models.TextField(max_length=100)),
            ],
        ),
    ]
