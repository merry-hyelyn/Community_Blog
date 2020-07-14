from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = "admin"  # 전부 다 가능 superuser
    STAFF = "staff"  # 글 삭제 댓글 삭제 가능 staff
    NORMAL_USER = "normal"  # 글 생성 댓글 생성 가능 just member(user)

    PERMISSION_CHOICES = (
        (
            ADMIN,
            "Admin",
        ),
        (
            STAFF,
            "Staff",
        ),
        (
            NORMAL_USER,
            "Normal",
        ),
    )

    ONE_STEP = "one"
    TWO_STEP = "two"
    THIRD_STEP = "third"
    STAFF_STEP = "zero"

    STEP_CHOICES = (
        (
            STAFF_STEP,
            "Zero",
        ),
        (
            ONE_STEP,
            "One",
        ),
        (
            TWO_STEP,
            "Two",
        ),
        (
            THIRD_STEP,
            "Third",
        ),
    )
    permission = models.CharField(max_length=7,
                                  choices=PERMISSION_CHOICES,
                                  default=NORMAL_USER)
    step = models.CharField(max_length=6,
                            choices=STEP_CHOICES,
                            default=ONE_STEP)
