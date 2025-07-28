from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        (0, '未着手'),
        (1, '進行中'),
        (2, '完了'),
    ]

    team_id = models.ForeignKey('Team', on_delete=models.CASCADE)
    assignee_id = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    priority = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
