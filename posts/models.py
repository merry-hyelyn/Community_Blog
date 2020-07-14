from django.db import models
from core.models import AbstractTimeStamp
from boards.models import Board
from users.models import User


# Create your models here.
class Post(AbstractTimeStamp):
    TRUE = "true"
    FALSE = "false"

    SECRET_CHOICES = (
        (TRUE, "true"),
        (FALSE, "false"),
    )

    title = models.CharField(max_length=20)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    secret = models.CharField(max_length=10,
                              choices=SECRET_CHOICES,
                              default=FALSE)

    def __str__(self):
        return self.title