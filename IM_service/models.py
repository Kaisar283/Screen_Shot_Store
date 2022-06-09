from django.db import models
from django.utils.translation import gettext_lazy as _


class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True, null=False, blank=False)
    category_name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    discription = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return f"{self.category_id} | {self.category_name}"


class Sub_Categoryes(models.Model):
    s_category_id = models.IntegerField(primary_key=True, unique=True,)
    s_category_name = models.CharField(max_length=30, blank=False, unique=True)
    category_id = models.ForeignKey('Categories', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Sub_Category')
        verbose_name_plural = _('Sub_categories')

    def __str__(self):
        return f"{self.s_category_id} | {self.s_category_name}"


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True, blank=False, null=False,)
    product_name = models.CharField(max_length=60)
    barcode = models.CharField(unique=True, max_length=13, blank=False)
    quantity = models.SmallIntegerField(blank=True)
    unit_price = models.IntegerField(blank=False)
    sale_price = models.IntegerField(blank=False)
    supplier_id = models.ForeignKey('Suppliers', on_delete=models.DO_NOTHING)
    category_id = models.ForeignKey('Categories', on_delete=models.DO_NOTHING)
    s_category_id = models.ForeignKey('Sub_Categoryes', on_delete=models.DO_NOTHING)
    store_id = models.ForeignKey('Store', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f"{self.product_id} | {self.product_name} | {self.barcode}"


class Suppliers(models.Model):
    supplier_id = models.SmallIntegerField(blank=False, null=False, primary_key=True)
    supplier_name = models.CharField(max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')

    def __str__(self):
        return f"{self.supplier_id} | {self.supplier_name}"


class Store(models.Model):
    name_store = models.CharField(max_length=20, blank=False, unique=True)
    address_store = models.TextField(blank=True)

    verbose_name = _('Store')
    verbose_name_plural = _('Stores')

    def __str__(self):
        return f"{self.name_store}"