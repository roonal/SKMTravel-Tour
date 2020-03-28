from django.contrib import admin
from .models import Company
from .models import PackagePlan, PackageActivities, Destination, Activities, Staff, StaffRole, Packages,\
    PackageType, PackageCostInfo, PackageReview
from . import models


class PackagesAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'total_days', 'package_type', 'difficulty')
    list_filter = ('package_id', 'total_days')
    search_fields = ('package_name',)
    fields = (
        ('package_name','total_days', 'price'),
        ('max_altitude', 'best_season'),
        ('img', 'difficulty'),
        ('company_id', 'package_type'),
        'overview'
    )


admin.site.register(Company)
admin.site.register(Packages, PackagesAdmin)
admin.site.register(Destination)
admin.site.register(Staff)
admin.site.register(PackagePlan)
admin.site.register(Activities)
admin.site.register(PackageActivities)
admin.site.register(StaffRole)
admin.site.register(PackageType)
admin.site.register(PackageCostInfo)
admin.site.register(PackageReview)










