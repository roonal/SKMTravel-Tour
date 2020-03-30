from django.contrib import admin
from .models import EducationalTour, Booking, AboutNepal, Blog, Gallery, CustomizeTrip, UserRequest
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(EducationalTour)
admin.site.register(Booking)
admin.site.register(AboutNepal)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(CustomizeTrip)
admin.site.register(UserRequest)



admin.site.unregister(Group)

#chaging admin header
admin.site.site_header = "Shree Krishna Mankamana Travel & Tour"
admin.site.site_title = "SKM"
admin.site.index_title = "Welcome to SKM Admin Site"
