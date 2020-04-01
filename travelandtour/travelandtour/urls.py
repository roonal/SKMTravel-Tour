
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('tourpackages/', include('tourpackages.urls')),

    path('reset-password', auth_views.PasswordResetView.as_view(template_name='user-auth/password_reset_form.html'), name='password_reset'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user-auth/password_change.html'), name='password_change'),

    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='user-auth/password_change_done.html'),
         name='password_change_done'),

    path('reset-password/done', auth_views.PasswordResetDoneView.as_view(
        template_name='user-auth/password_reset_done.html'), name='password_reset_done'),

    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user-auth/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view
    (template_name='user-auth/password_reset_complete.html'), name='password_reset_complete'),


]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

