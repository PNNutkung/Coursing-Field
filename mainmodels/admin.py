from django.contrib import admin

from .models import Course, Video
# Register your models here.
class VideoInline(admin.StackedInline):
    model = Video
    extra = 3

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Course Informations', {'fields': ['courseName', 'category']}),
        ('Course Pricing', {'fields': ['discountPercentage', 'discountPrice']}),
        ('Course Status', {'fields': ['isDelete', 'isPublish']}),
    ]
    inlines = [VideoInline]
    list_display = ('courseName', 'owner', 'isDelete', 'isPublish')
    search_fields = ['courseName']

admin.site.register(Course, CourseAdmin)
