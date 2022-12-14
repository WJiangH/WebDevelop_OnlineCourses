# Generated by Django 2.2 on 2022-02-24 16:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='课程名')),
                ('desc', models.CharField(max_length=50, verbose_name='课程描述')),
                ('learning_time', models.IntegerField(default=0, verbose_name='课程时长')),
                ('degree', models.CharField(choices=[('cj', ''), ('zj', ''), ('gj', '')], max_length=50, verbose_name='难度系数')),
                ('students', models.IntegerField(default=0, verbose_name='学生数目')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数目')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('category', models.CharField(default='后端开发', max_length=20, verbose_name='课程类别')),
                ('tag', models.CharField(default='', max_length=10, verbose_name='课程标签')),
                ('youneed_know', models.CharField(default='', max_length=300, verbose_name='课程须知')),
                ('teacher_tell', models.CharField(default='', max_length=300, verbose_name='老师语录')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('image', models.ImageField(upload_to='course/%Y/%m', verbose_name='封面图')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Teacher', verbose_name='讲师')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='章节名')),
                ('learning_time', models.IntegerField(default=0, verbose_name='学习时长')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
            options={
                'verbose_name': '章节信息',
                'verbose_name_plural': '章节信息',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='视频名')),
                ('learning_time', models.IntegerField(default=0, verbose_name='学习时长')),
                ('url', models.CharField(max_length=200, verbose_name='访问地址')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='章节')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('file', models.FileField(max_length=200, upload_to='course/resource/%Y/%m', verbose_name='下载地址')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程资源',
                'verbose_name_plural': '课程资源',
            },
        ),
    ]
