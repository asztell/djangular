from django.contrib import admin

from .models import Email


class EmailModelAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'contact_name', 'contact_email']
    list_display_links = ['created_date']
    list_editable = ['contact_name']
    list_filter = ['created_date', 'contact_name', 'contact_email']
    search_fields = ['created_date', 'contact_name', 'contact_email']

    class Meta:
        model = Email
        # fields = "__all__"

admin.site.register(Email, EmailModelAdmin)