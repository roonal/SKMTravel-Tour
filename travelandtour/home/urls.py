from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    # path('<pk>/', views.package_details, name="package_details"),
    path('package-details/<slug>/', views.package_details_final, name="package_details"),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)