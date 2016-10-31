from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=200)

class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=50)
    courseShortDesc = models.CharField(max_length=50)
    courseFullDesc = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    courseThumbnail = models.ImageField(upload_to='thumbnails/')
    previewVideoFile = models.FileField(upload_to='previews/')
    coursePrice = models.FloatField()
    createdDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isDelete = models.BooleanField()
    discountPercentage = models.IntegerField()
    discountPrice = models.FloatField()

class FeaturedCourse(models.Model):
    featuredCourseID = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    expireDate = models.DateTimeField(auto_now=False, auto_now_add=False)

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def get_upload_path(instance, filename):
        name, ext = filename.split('.')
        file_path = 'videos/{courseID}/{name}.{ext}'.format(
            courseID=instance.course.courseID, name=name, ext=ext
        )
        return file_path
    videoID = models.AutoField(primary_key=True)
    videoName = models.CharField(max_length=50)
    videoFile = models.FileField(upload_to=get_upload_path)
    videoDesc = models.CharField(max_length=250)
    createdDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    isDelete = models.BooleanField()

class Comment(models.Model):
    commentID = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    commentDesc = models.CharField(max_length=250)
    commentDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    isDelete = models.BooleanField()

class Transaction(models.Model):
    transactionID = models.AutoField(primary_key=True)
    courseID = models.IntegerField()
    coursePrice = models.FloatField()
    takerID = models.IntegerField()
    takerBalanceBeforePurchased = models.FloatField()
    usedCoupon = models.BooleanField()
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # taker = models.ForeignKey(User, on_delete=models.CASCADE)
    transactionDate = models.DateTimeField(auto_now=False, auto_now_add=True)


# class CourseInCategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    reviewDesc = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField()
    reviewedDate = models.DateTimeField(auto_now=False,auto_now_add=True)
    isDelete = models.BooleanField()

# class Coupon(models.Model):
#     couponSerial = models.IntegerField(primary_key=True)
#     couponDesc = models.CharField(max_length=250)
#     value = models.IntegerField()
#     percent = models.IntegerField()
#     createdDate = models.DateTimeField(auto_now=False, auto_now_add=True)
#     isUsed = models.BooleanField()

# class TakenCourse(models.Model):
#     takenCourseID = models.AutoField(primary_key=True)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     taker = models.ForeignKey(User, on_delete=models.CASCADE)

# class CoursePreview(models.Model):
#     coursePreviewID = models.AutoField(primary_key=True)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     previewVideo = models.FileField(upload_to='previews/')
#     isDelete = models.BooleanField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, default="")
    profilePicture = models.ImageField(upload_to='profilepics/')
    address = models.CharField(max_length=255, default="")
    birthDate = models.DateField(auto_now=False, auto_now_add=True)
    balance = models.FloatField()
    gender = models.CharField(max_length=1)
    # balance = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    isBan = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class OrderVideoInCourse(models.Model):
    orderVideoInCourseID = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    orderNo = models.IntegerField()