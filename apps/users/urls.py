import django
from django.views.generic import TemplateView
from apps.users.views import UserInfoView, UploadImageView, ChangePwdView, ChangeMobileView, MyFavOrgView, \
    MyFavTeacherView, MyFavCourseView, MyMessageView
from django.contrib.auth.decorators import login_required

if django.VERSION >= (3, 1, 0):
    from django.urls import re_path as url
else:
    from django.conf.urls import url

urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name='info'),
    url(r'^image/upload/$', UploadImageView.as_view(), name='image'),
    url(r'^update/pwd/$', ChangePwdView.as_view(), name="update_pwd"),
    url(r'^update/mobile/$', ChangeMobileView.as_view(), name="update_mobile"),

    url(r'^mycourse/$',
        login_required(TemplateView.as_view(template_name="usercenter-mycourse.html"), login_url="/login/"),
        {"current_page": "mycourse"}, name="mycourse"),

    url(r'^myfavorg/$', MyFavOrgView.as_view(), name="myfavorg"),
    url(r'^myfav_teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),
    url(r'^myfav_course/$', MyFavCourseView.as_view(), name="myfav_course"),
    url(r'^messages/$', MyMessageView.as_view(), name="messages"),
]
