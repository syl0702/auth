from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
    # article_set = 특정 유저가 쓴 글을 볼 수 있는 세트
    # comment_set = 