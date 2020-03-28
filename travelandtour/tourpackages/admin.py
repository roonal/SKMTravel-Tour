from django.contrib import admin
from .models import EducationalTour, Booking, AboutNepal, Blog, Gallery, CustomizeTrip

# Register your models here.

admin.site.register(EducationalTour)
admin.site.register(Booking)
admin.site.register(AboutNepal)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(CustomizeTrip)

#chaging admin header
admin.site.site_header = "Shree Krishna Mankamana Travel & Tour"
admin.site.site_title = "SKM"
admin.site.index_title = "Welcome to SKM Admin Site"
