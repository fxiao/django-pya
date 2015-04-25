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


class Currency(CacheModel):
    name = models.CharField(u"名称", max_length=50)
    code = models.CharField(u"代码", max_length=32)
    symbol_left = models.CharField(u"左符号", max_length=12)
    symbol_right = models.CharField(u"右符号", max_length=12)
    decimal_place = models.IntegerField(u"小数位", default=2)

    exchange_rate = models.FloatField(u"汇率", default=1.00000,
                                      help_text=u"如果这是您的默认货币，请将它设置为1.00000")
    date_modified = models.DateTimeField(u"修改时间", default=timezone.now)
    position = models.IntegerField(u"排序", default=1000)

    class Meta:
        ordering = ("position",)
        verbose_name = u"货币"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

# -------------------------------------------------- End class Currency


class Store(CacheModel):
    name = models.CharField(u"名称", max_length=50)
    slug = models.SlugField(u"标记", unique=True)
    url = models.URLField(u"链接", max_length=255, blank=True, null=True)

    address = models.CharField(u"地址", max_length=255, blank=True, null=True)
    image = models.ImageField(u"店标", upload_to="images/store_icon",
                              blank=True, null=True)

    open_time = models.CharField(u"营业时间", max_length=255,
                                 blank=True, null=True)
    position = models.IntegerField(u"排序", default=1000)

    meta_title = models.CharField(u"Meta Tag 标题",
                                  max_length=255, blank=True, null=True)
    meta_description = models.CharField(u"Meta Tag 描述",
                                        max_length=255, blank=True, null=True)
    meta_keyword = models.CharField(u"Meta Tag 关键字",
                                    max_length=255, blank=True, null=True)
    template = models.ForeignKey("Template", verbose_name=u"模板")
    currency = models.ForeignKey("Currency", verbose_name=u"货币")

    stock_display = models.BooleanField(u"显示库存", default=False)
    stock_checkout = models.BooleanField(u"缺货结账", default=False,
                                         help_text=u"如果用户订购的商品缺货，仍然允许结账。")

    class Meta:
        ordering = ("position",)
        verbose_name = u"商店"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

# -------------------------------------------------- End class Store


class StorePost(CacheModel):
    store = models.ForeignKey(Store, verbose_name=u"商店")
    content = models.CharField(u"内容", max_length=2000)

    date_added = models.DateTimeField(u"添加时间", auto_now_add=True)

    class Meta:
        ordering = ("date_added",)
        verbose_name = u"商店附言"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content

# -------------------------------------------------- End class StorePost


class Setting(CacheModel):
    store = models.ForeignKey(Store, verbose_name=u"商店")
    code = models.CharField(u"代码", max_length=32)

# -------------------------------------------------- End class Setting

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4
