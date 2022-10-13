from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher, CourseOrg
from DjangoUeditor.models import UEditorField

# Create your models here.


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='讲师')
    course_org = models.ForeignKey(CourseOrg, null=True, blank=True, on_delete=models.CASCADE, verbose_name='授课机构')
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=50, verbose_name='课程描述')
    learning_time = models.IntegerField(default=0, verbose_name='课程时长')
    degree = models.CharField(choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=50, verbose_name='难度系数')
    students = models.IntegerField(default=0, verbose_name='学生数目')
    fav_num = models.IntegerField(default=0, verbose_name="收藏数目")
    notice = models.CharField(default='', verbose_name='课程通告', max_length=200)
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name='课程类别')
    tag = models.CharField(default='', max_length=10, verbose_name='课程标签')
    youneed_know = models.CharField(default='', max_length=300, verbose_name='课程须知')
    teacher_tell = models.CharField(default='', max_length=300, verbose_name='老师语录')
    is_classic = models.BooleanField(default=False, verbose_name='是否经典')
    detail = UEditorField(verbose_name="课程详情", width=500, height=300, imagePath="courses/ueditor/images/",
                          filePath="courses/ueditor/files/", default="")
    image = models.ImageField(upload_to='course/%Y/%m', max_length=100, verbose_name='封面图')
    is_banner = models.BooleanField(default=False, verbose_name="是否广告位")

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def lesson_nums(self):
        return self.lesson_set.all().count()

    def show_image(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<img src='{}'>".format(self.image.url))

    show_image.short_description = "图片"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='/course/{}'>跳转</a>".format(self.id))

    go_to.short_description = "跳转"


class CourseTag(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程名')
    tag = models.CharField(max_length=100, verbose_name='标签')

    class Meta:
        verbose_name = '课程标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    learning_time = models.IntegerField(default=0, verbose_name='学习时长')

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    learning_time = models.IntegerField(default=0, verbose_name=u'学习时长')
    url = models.CharField(max_length=1000, verbose_name=u'访问地址')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name=u'名称')
    file = models.FileField(upload_to='course/resource/%Y/%m', max_length=200, verbose_name='下载地址')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
