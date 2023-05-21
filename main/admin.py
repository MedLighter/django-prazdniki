from django.contrib import admin

from main.models import Application, Catalogs, Order_info, Orders


admin.site.register(Orders)
admin.site.register(Application)
admin.site.register(Catalogs)
admin.site.register(Order_info)