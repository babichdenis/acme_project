from django.contrib import admin

from .models import Birthday

admin.site.empty_value_display = "Не задано"


class PostInline(admin.StackedInline):
    model = Birthday
    extra = 0

@admin.register(Birthday)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday'
    )
