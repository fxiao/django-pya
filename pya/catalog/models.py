# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(u"名称", max_length=255)
    parent = models.ForeignKey("self", verbose_name=u"父分类",
                               blank=True, null=True)
    image = models.ImageField(u"图片", upload_to="images", blank=True, null=True)

    description = models.TextField(u"描述", blank=True, null=True)
    meta_title = models.CharField(u"Meta Tag 标题",
                                  max_length=255, blank=True, null=True)
    meta_description = models.CharField(u"Meta Tag 描述",
                                        max_length=255, blank=True, null=True)
    meta_keyword = models.CharField(u"Meta Tag 关键字",
                                    max_length=255, blank=True, null=True)

    top = models.BooleanField(u"导航栏显示", default=True)
    column = models.IntegerField(u"分类列排显示", default=0)
    position = models.IntegerField(u"排序", default=1000)
    active = models.BooleanField(u"状态", default=True)

    date_added = models.DateTimeField(u"添加时间", auto_now_add=True)
    date_modified = models.DateTimeField(u"修改时间", default=timezone.now)

    class Meta:
        ordering = ("position",)
        verbose_name = u"分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        if self.parent is not None:
            return u"%s -> %s" % (self.parent.__unicode__(), self.name,)

        return self.name
# -------------------------------------------------- End class Category


class Manufacturer(models.Model):
    name = models.CharField(u"名称", max_length=50, unique=True)
    image = models.ImageField(u"图片", upload_to="images", blank=True, null=True)
    position = models.IntegerField(u"排序", default=1000)

    description = models.TextField(u"描述", blank=True, null=True)
    meta_title = models.CharField(u"Meta Tag 标题", max_length=255)
    meta_description = models.CharField(u"Meta Tag 描述", max_length=255)
    meta_keyword = models.CharField(u"Meta Tag 关键字", max_length=255)

    active = models.BooleanField(u"状态", default=True)

    date_added = models.DateTimeField(u"添加时间", auto_now_add=True)
    date_modified = models.DateTimeField(u"修改时间", auto_now=True)

    class Meta:
        ordering = ("position", "name", )
        verbose_name = u"品牌"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
# -------------------------------------------------- End class Manufacturer
