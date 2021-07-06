from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=400)
    image = models.ImageField(upload_to='user_image')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + '' + str(self.date)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userImage = models.ImageField(upload_to='user_image', default='hello.jpg')
    bio = models.CharField(max_length=200, blank=True)
    connection = models.CharField(max_length=100, blank=True)
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)


class Like(models.Model):
    user = models.ManyToManyField(User, related_name='likingUser',blank=True)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.post)

    @classmethod
    def liked(cls, post, liking_user):
        obj, create = cls.objects.get_or_create(post=post)
        obj.user.add(liking_user)
        obj.likes += 1
        obj.save()

    @classmethod
    def disliked(cls, post, disliking_user):
        obj, create = cls.objects.get_or_create(post=post)
        obj.user.remove(disliking_user)
        obj.likes -= 1
        obj.save()
