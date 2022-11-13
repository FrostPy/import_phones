from django.contrib import admin
from phones.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug']


admin.site.register(Phone, PhoneAdmin)
