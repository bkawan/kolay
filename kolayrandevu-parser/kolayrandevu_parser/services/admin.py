from django.contrib import admin

# Register your models here.

from .models import Service, BusinessServiceRel,Category

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(BusinessServiceRel)
