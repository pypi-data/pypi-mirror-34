from django.conf import settings
from django.urls.conf import path, include
from edc_base.views import AdministrationView
from edc_device.views import HomeView


app_name = 'edc_device'


if settings.APP_NAME == 'edc_device':
    urlpatterns = [
        path('accounts/', include('edc_base.auth.urls')),
        path('edc_base/', include('edc_base.urls')),
        path('administration/', AdministrationView.as_view(),
             name='administration_url')]
else:
    urlpatterns = []

urlpatterns += [
    path(r'', HomeView.as_view(), name='home_url'),
]
