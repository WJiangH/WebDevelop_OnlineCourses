import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource, CourseTag, BannerCourse
from xadmin.layout import Fieldset, Main, Side, Row, FormHelper
from import_export import resources

class GlobalSetting(object):
    site_title = 'Developed By Wenjiang Huang'
    site_footer = 'contact wenjiang0716@gmail.com'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# class CourseAdmin(object):
#     list_display = ['name', 'desc', 'detail', 'degree', 'learning_time', 'teacher', 'students']
#     search_fields = ['name', 'desc', 'detail', 'degree', 'students']
#     list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learning_time', 'students']
#     list_editable = ['degree', 'desc']

class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learning_time', 'teacher', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learning_time', 'students']
    list_editable = ['degree', 'desc']

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonInline(object):
    model = Lesson
    # style = "tab"
    extra = 0
    exclude = ["add_time"]


class CourseResourceInline(object):
    model = CourseResource
    style = "tab"
    extra = 1


class MyCourse(resources.ModelResource):

    class Meta:
        model = Course
        # fields = ('name', 'description',)
        # exclude = ()

class NewCourseAdmin(object):
    import_export_args = {'import_resource_class': MyCourse, 'export_resource_class': MyCourse}
    list_display = ['name', 'desc', 'show_image', 'go_to', 'detail', 'degree', 'learning_time', 'teacher', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learning_time', 'students']
    list_editable = ['degree', 'desc']
    readonly_fields = ["students", "add_time"]
    # exclude = ["click_nums", "fav_nums"]
    ordering = ["click_num"]
    model_icon = 'fa fa-address-book'
    inlines = [LessonInline, CourseResourceInline]
    style_fields = {
        "detail": "ueditor"
    }

    def queryset(self):
        qs = super().queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(teacher=self.request.user.teacher)
        return qs

    def get_form_layout(self):
        self.form_layout = (
            Main(
                Fieldset("讲师信息",
                         'teacher', 'course_org',
                         css_class='unsort no_title'
                         ),
                Fieldset("基本信息",
                         'name', 'desc',
                         Row('learning_time', 'degree'),
                         Row('category', 'tag'),
                         'youneed_know', 'teacher_tell', 'detail',
                         ),
            ),
            Side(
                Fieldset("访问信息",
                         'fav_num', 'click_num', 'students', 'add_time'
                         ),
            ),
            Side(
                Fieldset("选择信息",
                         'is_banner', 'is_classic'
                         ),
            )
        )
        return super(NewCourseAdmin, self).get_form_layout()


class ClassTagAdmin(object):
    list_display = ['course', 'tag', 'add_time']
    search_fields = ['course', 'tag']
    list_filter = ['course', 'tag', 'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_field = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_field = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'add_time']
    search_field = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'add_time']


xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Course, NewCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(CourseTag, ClassTagAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
