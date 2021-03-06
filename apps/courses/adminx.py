# _*_ encoding:utf-8 _*_
_author_ = 'baisy'
_date_ = '2018/1/7 13:43'

import xadmin

from .models import Course, Lesson, CourseResource, Video

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'learn_time', 'students']
    search_fields = ['name', 'desc', 'detail', 'students']
    list_filter = ['name', 'desc', 'detail', 'learn_time', 'students']

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
