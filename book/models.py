from django.db import models


# Create your models here.
# 图书类(一类)
# 必须继承Model类才能成为模型类
class BookInfo(models.Model):
    '''图书模型类'''
    # CharField说明是一个字符串,max_length指定最大长度
    btitle = models.CharField(max_length=20)  # 图书名称
    # DataField说明是日期类型
    bpub_data = models.DateField()  # 出版日期

    def __str__(self):
        return self.btitle


# 英雄人物类(多的类)
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄名
    # BooleanField说明是bool类型,default指定默认值,False代表男
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)  # 备注
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)  # 关系属性(建立图书类与英雄人物类之间的一对多之间的关系)

    def __str__(self):
        return self.hname
