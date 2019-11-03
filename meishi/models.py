from django.db import models

class Type(models.Model):
    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = '商品类别'
    type_name = models.CharField(max_length=50,verbose_name="类名")

    def __str__(self):
        return self.type_name

class Goods(models.Model):
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
    goods_name = models.CharField(max_length=50,verbose_name="类名")
    image = models.ImageField(upload_to="media/image")

    price = models.FloatField()
    is_delete = models.IntegerField(default=1)

class Good_type(models.Model):
    class Meta:
        verbose_name = '商品类别表'
        verbose_name_plural = '商品类别表'
    goods = models.ForeignKey(to="Goods",on_delete=models.CASCADE)
    type = models.ForeignKey(to="Type",on_delete=models.CASCADE)