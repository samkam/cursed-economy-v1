from django.db import models
from django.conf import settings
#from django.contrib import auth

class Curse(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    title_text = models.CharField(max_length=80)
    curse_text = models.CharField(max_length=600)

    def __str__(self):
        return "{}:{}".format(self.author, self.title_text)

class VoteRecord(models.Model):
    curse1 = models.ForeignKey(Curse, related_name="curse1", on_delete=models.CASCADE)
    curse2 = models.ForeignKey(Curse, related_name="curse2", on_delete=models.CASCADE)
    votes_id1 = models.IntegerField(default=0)
    votes_id2 = models.IntegerField(default=0)

# Create your models here.
