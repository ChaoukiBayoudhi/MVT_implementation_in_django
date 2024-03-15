from django.contrib import admin

from .models import Product,Provider,Command,Client,Address

# Register your models here.
admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(Command)
admin.site.register(Client)
admin.site.register(Address)
