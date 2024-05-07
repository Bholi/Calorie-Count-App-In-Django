from django.contrib import admin
from .models import Item,Consume
# Register your models here.
admin.site.register(Item)

class ConsumerAdmin(admin.ModelAdmin):
    list_display =('item_name','user')
admin.site.register(Consume,ConsumerAdmin)