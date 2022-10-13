from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger
from django.db.models import Q

from apps.courses.models import Course, CourseTag, CourseResource, Video
from apps.operations.models import UserFavorite, UserCourses, CourseComments
from django.contrib.auth.mixins import LoginRequiredMixin


class VideoView(View):
    login_url = '/login/'

    def get(self, request, course_id, video_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.click_num += 1
        course.save()

        video = Video.objects.get(id=int(video_id))
        # 用户是否关联课程
        user_course = UserCourses.objects.filter(user=request.user, course=course)
        if not user_course:
            user_course = UserCourses(user=request.user, course=course)
            user_course.save()
            course.students += 1
            course.save()

        # 学习过该课程的所有同学
        user_courses = UserCourses.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_courses = UserCourses.objects.filter(user_id__in=user_ids).order_by('-course__click_num')[:5]
        related_courses = [user_course.course for user_course in all_courses if user_course.id != course.id]

        course_resources = CourseResource.objects.filter(course=course)

        return render(request, 'course-play.html', {
            'course': course,
            'course_resources': course_resources,
            'related_courses': related_courses,
            'video': video,
        })


class CourseCommentsView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.click_num += 1
        course.save()

        comments = CourseComments.objects.filter(course=course)

        # 查询用户是否已经关联了该课程
        user_courses = UserCourses.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourses(user=request.user, course=course)
            user_course.save()

            course.students += 1
            course.save()

        # 学习过该课程的所有同学
        user_courses = UserCourses.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_courses = UserCourses.objects.filter(user_id__in=user_ids).order_by("-course__click_num")[:5]
        # related_courses = [user_course.course for user_course in all_courses if user_course.course.id != course.id]
        related_courses = []
        for item in all_courses:
            if item.course.id != course.id:
                related_courses.append(item.course)

        course_resources = CourseResource.objects.filter(course=course)

        return render(request, "course-comment.html", {
            "course": course,
            "course_resources": course_resources,
            "related_courses": related_courses,
            "all_comments": comments,
        })


class CourseLessonView(LoginRequiredMixin, View):
    login_url = '/login/'
    '''
    获取课程章节信息
    '''

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.click_num += 1
        course.save()

        # 用户是否关联课程
        user_course = UserCourses.objects.filter(user=request.user, course=course)
        if not user_course:
            user_course = UserCourses(user=request.user, course=course)
            user_course.save()
            course.students += 1
            course.save()
        # 学习过该课程的所有同学
        user_courses = UserCourses.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_courses = UserCourses.objects.filter(user_id__in=user_ids).order_by('-course__click_num')[:5]
        related_courses = [user_course.course for user_course in all_courses if user_course.id != course.id]

        course_resources = CourseResource.objects.filter(course=course)

        return render(request, 'course-video.html', {
            'course': course,
            'course_resources': course_resources,
            'related_courses': related_courses,
        })


# Create your views here.
class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        '''
        获取课程详情
        '''
        has_fav_course = False
        has_fav_org = False

        course = Course.objects.get(id=int(course_id))
        course.click_num += 1
        course.save()

        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        tags = course.coursetag_set.all()
        tag_list = [tag.tag for tag in tags]

        course_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course__id=course.id)[:3]
        related_courses = set()
        for course_tag in course_tags:
            related_courses.add(course_tag.course)

        return render(request, "course-detail.html", {
            "course": course,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,
            "related_courses": related_courses
        })


class CourseListView(View):
    def get(self, request, *args, **kwargs):
        all_courses = Course.objects.order_by('-add_time')
        hot_courses = Course.objects.order_by('-click_num')[:3]

        #搜索关键词
        keywords = request.GET.get('keywords', '')
        s_type = 'course'
        if keywords:
            all_courses = all_courses.filter(Q(name__icontains=keywords)|Q(desc__icontains=keywords)|Q(detail__icontains=keywords))


        sort = request.GET.get("sort", "")
        if sort == "students":
            all_courses = all_courses.order_by("-students")
        elif sort == "hot":
            all_courses = all_courses.order_by("-click_num")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, per_page=3, request=request)
        courses = p.page(page)
        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_courses': hot_courses,
            'keywords':keywords,
            's_type':s_type,

        })
