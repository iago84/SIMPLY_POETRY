from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.
class V_PROMO(models.Model):
    video = EmbedVideoField()

class POEM(models.Model):
    text=models.TextField('Poem')
    date_create=models.DateTimeField(auto_now=True)
    auth=models.CharField('Author',max_length=180)
    my_feeling=models.TextField('My feel')


class YOURFEELS(models.Model):
    name = models.CharField('Name:', max_length=100)
    y_feels = models.TextField('Your feelings')
    date_create = models.DateTimeField(auto_now=True)
    own_poem = models.ForeignKey(POEM, on_delete=models.DO_NOTHING)
