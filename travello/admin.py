from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Destination, Item, Customer, Calculation

# Register your models here
admin.site.site_header = 'KRISHNA KANCHAN BANGLES'


class InLineItem(admin.TabularInline):
    model = Item
    extra = 1
    max_num = 20


class DestinationAdmin(admin.ModelAdmin):
    inlines = [InLineItem]
    list_display = ('title', 'last_modified', 'created', 'bill_type')
    list_display_links = ('created',)
    list_editable = ('title',)
    list_filter = ('created', 'bill_type')
    search_fields = ('title',)

    fieldsets = (
        (None, {

            'fields': (
                'title', 'unique_id', 'customer', ('bill_type', 'hsn_code'), ('invoice_no', 'dated'), ('challan_no', 'date'),
                ('transport', 'vehicle_no'))

        }),
    )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_modified', 'created')
    list_display_links = ('created',)
    list_editable = ('title',)
    list_filter = ('created',)
    search_fields = ('title',)

    fieldsets = (
        (None, {

            'fields': ('title', 'name', 'address', 'mobile_no', ('city', 'state'), 'gst_no')

        }),
    )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Calculation)
admin.site.register(Destination, DestinationAdmin)
admin.site.unregister
