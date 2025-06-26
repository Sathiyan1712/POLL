
from django.db import models

# Create your models here.

class Poll(models.Model):
    statement = models.CharField(max_length=255)
    option1 = models.CharField(max_length=55)
    vote1 = models.IntegerField(default = 0)
    option2 = models.CharField(max_length=55)
    vote2 = models.IntegerField(default = 0)
    option3 = models.CharField(max_length=55)
    vote3 = models.IntegerField(default = 0)
    delete_password = models.CharField(max_length=128, blank=True)


from django.contrib.auth.models import User

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} voted on {self.poll.statement}"
    
    class Meta:
        unique_together = ('user', 'poll')  # Prevents duplicate votes
