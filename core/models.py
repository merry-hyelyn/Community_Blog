from django.db import models


# 추상 클래스 -> 상속만
class AbstractTimeStamp(models.Model):
    """Abstract TimeStamp Model
    Inherit:
        Model
    Fields:
        created_at : DateTimeField (UnEditable)
        updated_at : DateTimeField (Editable)
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True