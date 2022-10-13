import django
from captcha import views

# from apps.organizations.views import OrgView, UserAskView, OrgHomeView, OrgTeacherView, OrgCourseView, OrgDescView
from apps.operations.views import AddFavView, CommentView

if django.VERSION >= (3, 1, 0):
    from django.urls import re_path as url
else:
    from django.conf.urls import url

urlpatterns = [
                url(r'^fav/', AddFavView.as_view(), name='fav'),
                url(r'^comment/', CommentView.as_view(), name='comment'),
]
