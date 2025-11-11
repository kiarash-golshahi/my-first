from .models import Order
from django.contrib import admin

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['orderer_user', 'ordered_product', 'registration_date']
    list_filter = ['orderer_user', 'ordered_product']
    ordering = ['-registration_date']
    readonly_fields = [field.name for field in Order._meta.get_fields()] # All fields in this model are readonly for the admin.
    search_fields = ['orderer_user', 'ordered_product']

    def has_add_permission(self, request):
        return False # Admin can't add orders.
