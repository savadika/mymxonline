from django.db import models
from datetime import datetime

# Create your models here.


class CityDict(models.Model):
    """城市字段"""
    """城市名|描述|添加时间"""
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    """课程机构"""
    """
    名称|描述|结构标签|机构类别|点击数|收藏数|机构头像|机构地址|所在城市|学习人数|课程数|添加时间|
    必填项？非必填blank=True?可空null=True?默认default=''?外键Foreign?
    主要还是 verbose_name , max_legth ,default
    """
    name = models.CharField(max_length=100, verbose_name="名称")
    desc = models.TextField(
        max_length=2000,
        blank=True,
        default='',
        verbose_name="机构描述")
    tags = models.CharField(max_length=50, default='全国知名', verbose_name="机构标签")
    category = models.CharField(max_length=20,
                                choices=(("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高校")),
                                default="pxjg",
                                verbose_name="机构分类"
                                )
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    images = models.ImageField(
        upload_to='org/%Y/%m',
        max_length=100,
        verbose_name="机构头像")
    address = models.CharField(max_length=200, verbose_name="地址")
    city = models.ForeignKey(
        CityDict,
        on_delete=models.CASCADE,
        verbose_name="城市")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    course_nums = models.IntegerField(default=0, verbose_name="课程数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """教师"""
    """
    教师名称|所属机构|教龄|公司名称|公司职位|教育特点|点击数|收藏数|年龄|头像|添加时间|
    必填项？非必填blank=True?可空null=True?默认default=''?外键Foreign?
    主要还是 verbose_name , max_legth ,default
    """
    name = models.CharField(max_length=30, verbose_name="名字")
    org = models.ForeignKey(
        CourseOrg,
        on_delete=models.CASCADE,
        verbose_name="所属机构")
    work_years = models.IntegerField(default=0, verbose_name="教龄")
    work_company = models.CharField(max_length=100, verbose_name="工作公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    age = models.IntegerField(default=28, verbose_name="年龄")
    images = models.ImageField(
        upload_to='teacher/%Y/%m',
        max_length=300,
        verbose_name="头像")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
