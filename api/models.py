from django.db import models

from api.base_models import ModelWithExtraInfo


class Student(ModelWithExtraInfo):
    user_id = models.PositiveIntegerField()
    name = models.CharField(max_length=60, default='')
    school = models.CharField(max_length=100, default='')
    specialty = models.CharField(max_length=60, default='')
    email = models.EmailField()

    created_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Teacher(ModelWithExtraInfo):
    user_id = models.PositiveIntegerField()
    name = models.CharField(max_length=60, verbose_name='头像')
    avatar = models.ImageField(verbose_name='头像')
    school_degree = models.TextField(verbose_name='学校学位信息')
    intro = models.TextField(verbose_name='介绍')
    rank = models.PositiveIntegerField(default=0, verbose_name='排名, 0表示不展示')

    created_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class SuccessRecord(ModelWithExtraInfo):
    """
    录取成功记录
    """
    user_id = models.PositiveIntegerField()
    name = models.CharField(max_length=60, verbose_name='头像')
    school = models.CharField(max_length=100, default='')
    specialty = models.CharField(max_length=60, default='')
    background = models.CharField(max_length=60, default='')
    rank = models.PositiveIntegerField(default=0, verbose_name='排名, 0表示不展示')

    created_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class ThirdUserBinding(models.Model):
    """
    第三方用户绑定
    """
    user_id = models.PositiveIntegerField()
    union_id = models.CharField(max_length=60)

    created_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

