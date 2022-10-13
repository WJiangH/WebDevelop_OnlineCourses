# Generated by Django 2.2 on 2022-02-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220224_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '个人信息', 'verbose_name_plural': '个人信息'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=11, unique=True, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(default='', max_length=50, verbose_name='昵称'),
        ),
    ]
