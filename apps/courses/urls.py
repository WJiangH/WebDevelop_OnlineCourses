import django
from captcha import views

#from apps.operations.views import AddFavView
from apps.courses.views import CourseListView, CourseDetailView, CourseLessonView, CourseCommentsView, VideoView
if django.VERSION >= (3, 1, 0):
    from django.urls import re_path as url
else:
    from django.conf.urls import url

urlpatterns = [
                url(r'^list/', CourseListView.as_view(), name='list'),
                url(r'^(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="detail"),
                url(r'^(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name="lesson"),
                url(r'^(?P<course_id>\d+)/comments/$', CourseCommentsView.as_view(), name="comments"),
                url(r'^(?P<course_id>\d+)/video/(?P<video_id>\d+)$', VideoView.as_view(), name="video"),
]
