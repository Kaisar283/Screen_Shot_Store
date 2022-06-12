from django.db import models


class Sales_History(models.Model):
    product_id = models.IntegerField(blank=False, null=False)
    barcode = models.CharField(blank=False, max_length=13)
    product_name = models.CharField(max_length=50, blank=False)
    sale_price = models.IntegerField(blank=False, null=False)
    date = models.DateField(blank=True, auto_now_add=True, editable=False)


