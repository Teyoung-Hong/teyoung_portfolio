from django.db import models
from django.utils import timezone

class Post(models.Model):

    SECTION_CHOICES = (
      ('skills','skills'),
      ('works','works'),
      ('coming','coming'),
    )

    GENRE_CHOICES = (
      ('language','language'),
      ('programming','programming'),
      ('else','else'),
    )

    title = models.CharField("タイトル", max_length=255, blank=False, null=False, default="")
    section = models.CharField('セクション', max_length=255, blank=False, null=False, default="coming", choices=SECTION_CHOICES)
    genre = models.CharField('ジャンル', max_length=255, blank=False, null=False, default="else", choices=GENRE_CHOICES)
    desc = models.CharField("説明", max_length=255, blank=False, null=False, default="説明が入ります")


    def __str__(self):
      return self.title


class Contact(models.Model):
    name = models.CharField("氏名", max_length=50)
    email = models.EmailField(max_length=200)
    message = models.CharField("本文", max_length=5000)

    def __str__(self):
        return '%s sent message %s' % (self.name, self.message)
