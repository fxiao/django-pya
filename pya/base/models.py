# -*- coding: utf-8 -*-
from django.db import models

class Store(models.Model):
    name = models.CharField(u"名称", max_length=50)
    slug = models.SlugField(u"标记", unique=True)
    url = models.URLField(u"链接", max_length=255, unique=True)
    ssl = models.URLField(u"加密链接", max_length=255, unique=True)
    position = models.IntegerField(u"排序", default=1000)

    class Meta:
        ordering = ("position",)
        verbose_name = u"商店"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

# -------------------------------------------------- End class Store


class Setting(models.Model):
    store = models.ForeignKey(Store, verbose_name=u"商店")
    code = models.CharField(u"代码", max_length=32)

# -------------------------------------------------- End class Setting

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4
