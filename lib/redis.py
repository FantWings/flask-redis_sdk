import redis
from flask import current_app


class Redis(object):
    """静态方法，初始化Redis实例"""
    @staticmethod
    def _get_r():
        host = current_app.config['REDIS_HOST']
        port = current_app.config['REDIS_PORT']
        db = current_app.config['REDIS_DB']
        r = redis.StrictRedis(host, port, db)
        return r

    @classmethod
    def write(cls, key, value, expire=None):
        """
        将键值对写入Redis
        :params key: 键
        :params value: 值
        :params expire: 过期时间（默认为配置文件中的过期时间）
        """
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = current_app.config['REDIS_EXPIRE']
        r = cls._get_r()
        return r.set(key, value, ex=expire_in_seconds)

    @classmethod
    def read(cls, key):
        """
        利用键来获取Redis内对应的值，如果该值不存在，则返回None
        :params key: 键
        :return: 值 or None
        """
        r = cls._get_r()
        value = r.get(key)
        return value.decode('utf-8') if value else value

    @classmethod
    def hset(cls, name, key, value):
        """
        写入哈希表，用于为哈希表中的字段赋值
        :params name: 名称
        :params key: 键
        :params value: 值
        :return: 1 = 设置成功，0 = 已覆盖旧数据
        """
        r = cls._get_r()
        vaule = r.hset(name, key, value)
        return value

    @classmethod
    def hmset(cls, name, *value):
        """
        同时将多个 field-value（键值对）设置到哈希表中。
        :params name: 哈希表名称
        :params value: 字典（{'a':'1','b':'2'}）
        :return: 布尔值
        """
        r = cls._get_r()
        value = r.hmset(name, *value)
        return value

    @classmethod
    def hget(cls, name, key):
        """
        返回哈希表中指定字段的值，如果该值不存在，则返回None
        :params name: 哈希表名称
        :params key: 键
        :return: 值 or None
        """
        r = cls._get_r()
        value = r.hget(name, key)
        return value.decode('utf-8') if value else value

    @classmethod
    def hgetall(cls, name):
        """
        返回哈希表中所有字段和值，如果该值不存在，则返回None
        :params name: 哈希表名称
        :return: 字典
        """
        r = cls._get_r()
        return r.hgetall(name)

    @classmethod
    def delete(cls, *names):
        """
        删除给定键对应的值
        :params names: 键 or ['键']
        :return: 0 = 给定值不存在, 1 = 删除成功
        """
        r = cls._get_r()
        return r.delete(*names)

    @classmethod
    def hdel(cls, name, key):
        """
        删除哈希表 key 中的一个或多个指定字段，如果该字段不存在则忽略
        :params name: 哈希表名称
        :params key: 键
        """
        r = cls._get_r()
        r.hdel(name, key)

    @classmethod
    def expire(cls, name, expire=None):
        """
        更新或设置给定字段的过期时间（单位:秒）
        :params name: 键
        :params expire: 过期时间
        """
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = current_app.config['REDIS_EXPIRE']
        r = cls._get_r()
        r.expire(name, expire_in_seconds)
