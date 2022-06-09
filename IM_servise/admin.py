from django.contrib import admin
from .models import Products
from .models import Categories
from .models import Sub_Categoryes
from .models import Store
from .models import Suppliers

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Sub_Categoryes)
admin.site.register(Store)
admin.site.register(Suppliers)