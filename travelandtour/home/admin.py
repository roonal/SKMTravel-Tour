from django.contrib import admin
from .models import Company
from .models import PackagePlan, PackageActivities, Destination, Activities, Staff, StaffRole, Packages,\
    PackageType, PackageCostInfo, PackageReview
from . import models


class PackagesAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'total_days', 'package_type', 'difficulty')
    list_filter = ('package_id', 'total_days')
    search_fields = ('package_name',)
    prepopulated_fields = {'slug_field': ('package_name',)}
    fields = (
        ('package_name', 'total_days', 'price'),
        ('max_altitude', 'best_season'),
        ('img', 'difficulty'),
        ('company_id', 'package_type'),
        ('staff_id', 'slug_field'),
        'overview',
        ('featured_package', 'best_selling_package')
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_by', 'review_verification', 'review_date')
    list_filter = ('package_id', 'ratings')
    search_fields = ('package_id', 'ratings',)
    actions = ('check_review',)

    def check_review(self, request, queryset):
        count = queryset.update(review_verification=True)
        self.message_user(request, '{} package review have been verified successfully.'.format(count))
    check_review.short_description = "Verify The Selected Review"


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
admin.site.register(PackageReview, ReviewAdmin)










