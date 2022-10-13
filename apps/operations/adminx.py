import xadmin

from apps.operations.models import UserAsk, CourseComments, UserFavorite, UserCourses, UserMessage, Banner



class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index']

class UserAskAdmin(object):
    list_display = ['user', 'mobile', 'course', 'add_time']
    search_fields = ['user', 'mobile', 'course']
    list_filter = ['user', 'mobile', 'course', 'add_time']


class UserCommentAdmin(object):
    list_display = ['user', 'course', 'comment', 'add_time']
    search_fields = ['user', 'course', 'comment']
    list_filter = ['user', 'course', 'comment', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserCoursesAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']

    def save_models(self):
        obj = self.new_obj
        if not obj.id:
            obj.save()
            course = obj.course
            course.students += 1
            course.save()


class UserMessageAdmin(object):
    list_display = ['user', 'has_read', 'add_time']
    search_fields = ['user', 'has_read']
    list_filter = ['user', 'has_read', 'add_time']

xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourses, UserCoursesAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, UserCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
