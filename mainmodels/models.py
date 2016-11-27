from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

def get_upload_path_thumbnail(instance, filename):
    name, ext = filename.split('.')
    file_path = 'thumbnails/{courseID}/{name}.{ext}'.format(
        courseID=instance.courseID, name=name, ext=ext
    )
    return file_path
def get_upload_path_preview(instance, filename):
    name, ext = filename.split('.')
    file_path = 'previews/{courseID}/{name}.{ext}'.format(
        courseID=instance.courseID, name=name, ext=ext
    )
    return file_path

def get_upload_path_video(instance, filename):
    name, ext = filename.split('.')
    file_path = 'videos/{courseID}/{name}.{ext}'.format(
        courseID=instance.course.courseID, name=name, ext=ext
    )
    return file_path

def get_upload_path_profilepicture(instance, filename):
    name, ext = filename.split('.')
    file_path = 'profilepictures/{userID}/{name}.{ext}'.format(
        userID=instance.user.id, name=name, ext=ext
    )
    return file_path

class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=200)
    def __str__(self):
        return self.categoryName

class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=50, default='Course name')
    courseShortDesc = models.CharField(max_length=50, default='Course short description')
    courseFullDesc = models.TextField(default='Course full description')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    courseThumbnail = models.ImageField(upload_to=get_upload_path_thumbnail, default='thumbnails/dummies/untitled.png')
    previewVideoFile = models.FileField(upload_to=get_upload_path_preview, default='previews/dummies/blankvideo.mp4')
    coursePrice = models.FloatField(default=0.00)
    createdDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)
    isPublish = models.BooleanField(default=False)
    discountPercentage = models.IntegerField(default=0)
    discountPrice = models.FloatField(default=0.00)

class FeaturedCourse(models.Model):
    featuredCourseID = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    expireDate = models.DateTimeField(auto_now=False, auto_now_add=False)

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    videoID = models.AutoField(primary_key=True)
    videoName = models.CharField(max_length=50, default='video name')
    videoFile = models.FileField(upload_to=get_upload_path_video, default='previews/dummies/blankvideo.mp4')
    videoDesc = models.CharField(max_length=250, default='video description')
    createdDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    isDelete = models.BooleanField(default=False)

class Comment(models.Model):
    commentID = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    commentDesc = models.CharField(max_length=250, default='your comment')
    commentDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    isDelete = models.BooleanField(default=False)

class Transaction(models.Model):
    transactionID = models.AutoField(primary_key=True)
    courseID = models.IntegerField(default=1)
    coursePrice = models.FloatField(default=0.00)
    takerID = models.IntegerField(default=1)
    takerBalanceBeforePurchased = models.FloatField(default=0.00)
    usedCoupon = models.BooleanField(default=False)
    transactionDate = models.DateTimeField(auto_now=False, auto_now_add=True)

class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    reviewDesc = models.CharField(max_length=255, default='review description')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    reviewedDate = models.DateTimeField(auto_now=False,auto_now_add=True)
    isDelete = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, default="Your bio")
    profilePicture = models.ImageField(upload_to=get_upload_path_profilepicture, default='thumbnails/dummies/untitled.png')
    address = models.CharField(max_length=255, default="Your address")
    birthDate = models.DateField(auto_now=False, auto_now_add=True)
    balance = models.FloatField(default=0.00)
    gender = models.CharField(max_length=1, default='M')
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
    orderNo = models.IntegerField(default=0)

class Coupon(models.Model):
    serial = models.CharField(primary_key=True,max_length=11)
    value = models.IntegerField()
    transaction = models.ForeignKey('Transaction',null=True, blank=True, default = None)
