from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail

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


user_list = []


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'selected_package', 'booking_verification')
    list_filter = ('name', 'selected_package', 'booking_verification')
    search_fields = ('selected_package',)
    actions = ('check_booking',)

    def check_booking(self, request, queryset):
        count = queryset.update(booking_verification=True)
        self.message_user(request, '{} Booking have been verified successfully.'.format(count))

        reviewed_packages = Booking.objects.filter(booking_verification=True)
        if reviewed_packages is not None:
            user_list.append('Ronal Niraula')
            for rev_pack in reviewed_packages:
                for abc in user_list:
                    if abc != rev_pack.name:
                        user_list.append(rev_pack.name)
                        email_from = settings.EMAIL_HOST_USER
                        subject = 'Approval of Tour Booking Request'
                        message = 'Dear {}, your booking request for the package {} has been approved successfully.' \
                                  ' You will be provided detailed information about the {} and other notification within few hours.' \
                                      .format(rev_pack.name, rev_pack.selected_package, rev_pack.selected_package) + \
                                  'Thank you for choosing Shree Krishna Mankamana Travel and Tour'

                        email = rev_pack.email
                        recipient = [email]

                        send_mail(subject, message, email_from, recipient, fail_silently=False)
    check_booking.short_description = "Verify The Selected Booking Request"


admin.site.register(EducationalTour)
admin.site.register(Booking, BookingAdmin)
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
