from django.db import models
from django.contrib.auth.models import User

class Question(models.Model): # 데이터 베이스 모델
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField()
    def __str__(self):
        return self.subject

class Answer(models.Model):
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()
    # 다른 테이블의 한 레코드가 삭제되면, 그 레코드의 PK를 FK로 가진 다른 테이블의 레코드로 같이(연쇄) 삭제된다.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)