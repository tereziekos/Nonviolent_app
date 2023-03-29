from django.db import models
from django.contrib.auth.models import User

class FeelingGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"<FeelingGroup: {self.name}>"

class Feeling(models.Model):
    name = models.CharField(max_length=50)
    when_needs_met = models.BooleanField(default=False)
    when_needs_not_met = models.BooleanField(default=False)
    group = models.ForeignKey(FeelingGroup, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class FeelingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s session at {self.session_datetime}"



class FeelingSelection(models.Model):
    feeling_session = models.ForeignKey(FeelingSession, on_delete=models.CASCADE)
    feeling = models.ForeignKey(Feeling, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.feeling_session} - {self.feeling.name}"


