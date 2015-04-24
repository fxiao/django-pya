# -*- coding: utf-8 -*-
# 公共类
from django.db import models
from django.core.cache import cache


class CacheModel(models.Model):
    # 缓存操作模型

    def get_caache_name(self):
        return self.__name__

    def save(self, *args, **kwargs):
        super(CacheModel, self).save(*args, **kwargs)
        self.cache_model_del()

    def cache(self, key, value=None, default=None, timeout=0, version=None):
        if value is None:
            return cache.get(key, default=default, version=version)

        cache.set(key, value, timeout=timeout, version=version)

        cache_log = cache.get(self.get_caache_name(), default=[])
        if key not in cache_log:
            cache.set(self.get_caache_name(), cache_log.append(key))

    # ------------------------------------------ End def cache()

    def cache_model_del(self):
        cache_log = cache.get(self.get_caache_name(), default=[])
        for key in cache_log:
            cache.delete(key)

# -------------------------------------------------- End class CacheModel


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4
