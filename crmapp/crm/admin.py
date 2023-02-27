from django.contrib import admin
from .models import Customer, Comment, Status, Location
# Register your models here.

'''
admin.site.register(Customer)
admin.site.register(Comment)
'''

admin.site.register(Status)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ['street', 'city', 'apt_number', 'is_hq', 'customer_id']
    list_display = ['street', 'city', 'apt_number', 'is_hq']
    list_filter = ['city']
    search_fields = ['city', 'apt_number']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ['name', 'tin']
    list_display = ['name', 'tin']
    search_fields = ['name', 'tin']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['content', 'location_id']
    list_display = ['content', 'date_created', 'location_id']
    search_fields = ['location_id' ]