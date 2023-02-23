```python
# unique_together 속성이 사라지고 UniqueConstraint 사용권장 공식문서

from django.db import models

class Model(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['field1', 'field2'], name='please_write_down_the_name_of_the_constraint'),
        ]


from django.db import models

class Customer(models.Model):
    age = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name='age_gte_18'),
        ]
```
