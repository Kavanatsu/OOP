from django.contrib import admin
from catalog.models import *
from catalog.forms import ApplicationForm
class ApplicationAdmin(admin.ModelAdmin):
    form = ApplicationForm
    list_display = ('name', 'date', 'username', 'status')
    fields = ('status', 'img', 'comment')
    list_filter = ('status', 'categories')


admin.site.register(User)
admin.site.register(Categorise)
admin.site.register(Application, ApplicationAdmin)


