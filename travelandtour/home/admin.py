from django.contrib import admin
from .models import Company
from .models import PackagePlan, PackageActivities, Destination, Activities, Staff, StaffRole, Packages,\
    PackageType, PackageCostInfo, PackageReview

admin.site.register(Company)
admin.site.register(Packages)
admin.site.register(Destination)
admin.site.register(Staff)
admin.site.register(PackagePlan)
admin.site.register(Activities)
admin.site.register(PackageActivities)
admin.site.register(StaffRole)
admin.site.register(PackageType)
admin.site.register(PackageCostInfo)
admin.site.register(PackageReview)








