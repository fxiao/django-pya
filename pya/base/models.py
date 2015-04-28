# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from base.utils import CacheModel


class Template(CacheModel):
    name = models.CharField(u"名称", max_length=50)
    slug = models.SlugField(u"标记", unique=True)
    active = models.BooleanField(u"状态", default=True)
    position = models.IntegerField(u"排序", default=1000)

    class Meta:
        ordering = ("position",)
        verbose_name = u"模板"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.slug,)

# -------------------------------------------------- End class Template


class Setting(CacheModel):
    code = models.CharField(u"代码", max_length=32)
    key = models.CharField(u"标记", max_length=64)
    value = models.TextField(u"值")
    serialized = models.BooleanField(u"serialized")

    class Meta:
        ordering = ("code",)
        verbose_name = u"系统配置"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.code

# -------------------------------------------------- End class Setting

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4
