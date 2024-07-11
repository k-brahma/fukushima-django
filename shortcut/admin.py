from django.contrib import admin

from shortcut.models import Example


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('operation', 'result', 'description')
