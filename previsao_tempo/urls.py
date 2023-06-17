from django.urls import path
from . import view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # outras rotas...
    path('weather/forecast/', view.weather_forecast, name='weather_forecast'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

