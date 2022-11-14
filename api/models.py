from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
# Create your models here.

class Questions(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images", null=True)
    created_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    @property
    def question_answers(self):
        return self.answers_set.all().annotate(u_count=Count('upvote')).order_by('-u_count')

    def __str__(self):
        return self.title

class Answers(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    upvote = models.ManyToManyField(User,related_name="upvote")

    def __str__(self):
        return self.answer

    @property
    def votecount(self):
        return self.upvote.all().count()

# from api.models import Questions, Answers
# from django.contrib.auth.models import User                                                
# usr = User.objects.get(id=1)
# Questions.objects.create(title='django', description='django architecture?', user=usr)
# usr.questions_set.create(title='django', description='django architecture?')
# qs = Questions.objects.filter(user=usr)
# usr.questions_set.all()
# Answers.objects.create(question=3,answer='both',user=usr)
# ques = Questions.objects.get(id=3)
# ques.answers_set.create(answer='both',user=usr)
# ques.answers_set.all()
# ans = Answers.objects.get(id=4)
# ans.upvote.add(usr)
# ans.upvote.all()

