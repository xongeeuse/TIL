from django.db import models


class TravelBucketList(models.Model):
    # 고유 식별자 (Primary Key)는 Django가 자동으로 'id' 필드를 생성해줌
    destination_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(blank=True)
    reason = models.TextField(null=True, blank=True)
    planned_visit_date = models.DateField(null=True, blank=True)

    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    ]

    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.destination_name
