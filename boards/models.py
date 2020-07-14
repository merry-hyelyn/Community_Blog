from django.db import models
from users.models import User
from core.models import AbstractTimeStamp


class Board(AbstractTimeStamp):
    name = models.CharField(max_length=20)  # 게시판 이름
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)  # 게시판 생성자
    path = models.CharField(max_length=20)  # 게시판 url 경로 /hyelyn

    def __str__(self):
        return self.name