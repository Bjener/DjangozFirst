from django.contrib import admin
from .models import Type, Goods,Good_type

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','type_name']
    ordering = ['id']

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ["goods_name","price"]


@admin.register(Good_type)
class Goods_TypeAdmin(admin.ModelAdmin):
    list_display = ["goods","type"]
