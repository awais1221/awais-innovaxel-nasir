from django.urls import path
from .views import CreateShortURL, RetrieveOrignalURL, UpdateShortURL, DeleteShortURL, URLStats, form_interface, homepage


urlpatterns = [
    # path('', homepage, name = 'homepage'),
    path('shorten/', CreateShortURL.as_view(), name = 'create_short_url'),
    path('shorten/<str:code>/', RetrieveOrignalURL.as_view(), name='retrieve_url'),
    path('shorten/<str:code>/update/', UpdateShortURL.as_view(), name='update_url'),
    path('shorten/<str:code>/delete/', DeleteShortURL.as_view(), name='delete_url'),
    path('shorten/<str:code>/stats/', URLStats.as_view(), name='url_stats'),
    path('', form_interface, name='frontend'),


]
