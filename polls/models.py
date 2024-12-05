from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    name = models.CharField(verbose_name="Название опроса", max_length=300)
    published = models.DateTimeField(auto_now_add=True)

    def user_voted(self, user):
        user_votes = user.vote_set.all()
        done = user_votes.filter(question=self)
        if done.exists():
            return False
        return True

    def __str__(self):
        return self.name


class Choice(models.Model):
    class Meta:
        verbose_name = 'Варианты овтетов'
        verbose_name_plural = 'Варианты ответов'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=200)
    votes = models.IntegerField(verbose_name="Кол-во голосов", default=0)

    def __str__(self):
        return self.name

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.name[:15]} - {self.choice.name[:15]} - {self.user.username}'
