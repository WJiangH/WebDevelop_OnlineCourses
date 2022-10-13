from django.db import models
from DjangoUeditor.models import UEditorField

from apps.users.models import BaseModel
from apps.users.models import UserProfile
# Create your models here.

'''
实体：
课程机构（名字，描述，标签，机构类别，点击数，收藏数，图片，地址，学习人数，课程数量）# 对所在地区（城市）设置外键 以便以后添加
课程讲师（姓名，工作年限，所在公司，公司职位，教学特点，点击数，收藏数，年龄，头像）

'''


class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u'城市名')
    desc = models.CharField(max_length=200, verbose_name=u'描述')

    class Meta:
        verbose_name = '所在城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, default='skjg', verbose_name='机构名称')
    desc = UEditorField(verbose_name="描述", width=500, height=300, imagePath="organizations/ueditor/images/",
                        filePath="organizations/ueditor/files/", default="")
    tag = models.CharField(default='全国知名', max_length=10, verbose_name='机构标签')
    category = models.CharField(choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')), max_length=4, default='pxjg',
                                verbose_name='机构类别')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(upload_to='org/%Y/%m', max_length=100, verbose_name=u'logo')
    address = models.CharField(max_length=150, verbose_name='机构地址')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='所在城市')
    student_num = models.IntegerField(default=0, verbose_name='学生数目')
    course_num = models.IntegerField(default=0, verbose_name='课程数目')

    is_auth = models.BooleanField(default=True, verbose_name='是否认证')
    is_gold = models.BooleanField(default=True, verbose_name='是否金牌')

    def courses(self):
        courses = self.course_set.filter(is_classic=True)[:3]
        return courses

    class Meta:
        verbose_name = '授课机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True, verbose_name="用户")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name='所在机构')
    name = models.CharField(max_length=20, verbose_name='讲师名称')
    work_year = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='所在公司')
    work_position = models.CharField(max_length=50, verbose_name='公司职位')
    points = models.CharField(max_length=50, verbose_name='教学特点')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    age = models.IntegerField(default=18, verbose_name='年龄')
    image = models.ImageField(upload_to='teacher/%Y/%m', max_length=50, verbose_name='头像')

    class Meta:
        verbose_name = '授课讲师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def course_nums(self):
        courses = self.course_set.all().count()
        return courses
