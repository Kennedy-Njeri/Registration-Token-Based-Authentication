from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    list_display = ("user", "topic", "instructions", "urgency", "pages")




admin.site.register(Order, OrderAdmin)

