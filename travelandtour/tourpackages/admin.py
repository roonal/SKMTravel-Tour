from django.contrib import admin
from .models import EducationalTour, Booking, AboutNepal, Blog, Gallery, CustomizeTrip, UserRequest
from django.contrib.auth.models import Group
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_name', 'blog_by', 'blog_verification')
    list_filter = ('blog_name', 'blog_verification')
    search_fields = ('blog_name',)
    actions = ('check_blog', 'uncheck_blog')

    def check_blog(self, request, queryset):
        count = queryset.update(blog_verification=True)
        self.message_user(request, '{} Blog have been verified successfully.'.format(count))
    check_blog.short_description = "Verify The Selected Blogs"

    def uncheck_blog(self, request, queryset):
        count = queryset.update(blog_verification=False)
        self.message_user(request, '{} Blog have been unverified successfully.'.format(count))
    uncheck_blog.short_description = "unverify The Selected Blogs"


admin.site.register(EducationalTour)
admin.site.register(Booking)
admin.site.register(AboutNepal)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Gallery)
admin.site.register(CustomizeTrip)
admin.site.register(UserRequest)



admin.site.unregister(Group)

#chaging admin header
admin.site.site_header = "Shree Krishna Mankamana Travel & Tour"
admin.site.site_title = "SKM"
admin.site.index_title = "Welcome to SKM Admin Site"
