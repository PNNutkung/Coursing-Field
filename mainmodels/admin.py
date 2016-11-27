from django.contrib import admin

from django.contrib.auth.models import User
from .models import Course, Video, Category, FeaturedCourse, Comment, Review, Profile, Coupon
# Register your models here.
class VideoInline(admin.StackedInline):
    model = Video
    extra = 3

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Course Informations', {'fields': ['courseName', 'category']}),
        ('Course Pricing', {'fields': ['coursePrice', 'discountPercentage', 'discountPrice']}),
        ('Course Status', {'fields': ['isDelete', 'isPublish']}),
    ]
    inlines = [VideoInline]
    list_display = ('courseName', 'owner', 'isDelete', 'isPublish')
    search_fields = ['courseName']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['categoryName']
    list_display = ['categoryName']
    search_fields = ['categoryName']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('video', 'commentDesc', 'owner', 'isDelete')

class ReviewAdmin(admin.ModelAdmin):
    fields = ['reviewDesc', 'isDelete']
    list_display = ('course', 'owner', 'rating', 'isDelete')

class ProfileAdmin(admin.ModelAdmin):
    fields = ['profilePicture', 'balance', 'isBan']
    list_display = ('user', 'isBan')

class CouponAdmin(admin.ModelAdmin):
    fields = ['serial', 'value']
    list_display = ('serial', 'transaction')

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(FeaturedCourse)
