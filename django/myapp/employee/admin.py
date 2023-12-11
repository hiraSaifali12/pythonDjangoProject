from django.contrib import admin
from .models import employee,testimonial
# Register your models here.


class employeeAdmin(admin.ModelAdmin):
    list_display=('name','working','employee_id','phone',)
    list_editable=('working','employee_id',)
    search_fields=('name','phone',)
    list_filter=('working',)

admin.site.register(employee,employeeAdmin)
admin.site.register(testimonial)