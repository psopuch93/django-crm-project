from django.contrib import admin
from .models import Customer, Comment, Status, Headquarter
# Register your models here.

'''
admin.site.register(Customer)
admin.site.register(Comment)
'''

admin.site.register(Status)
admin.site.register(Headquarter)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ['name', 'tin', 'city']
    list_display = ['name', 'tin', 'city']
    list_filter = ['city']
    search_fields = ['name', 'tin']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['content', 'customer_id', ]
    list_display = ['content', 'date_created', 'customer_id', ]
    search_fields = ['customer_id', ]