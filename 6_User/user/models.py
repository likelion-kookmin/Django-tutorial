from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    코드를 보기전에 생각해 보아요!
    가장 중요한 username, passw요ord 는 어디에 있을까요?
    혹시 상속이 뭔지 아시나??
    """
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)




