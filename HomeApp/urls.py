from django.urls import path
from . import views
from django.conf.urls.static import static
from HomeProject import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/brand/<int:brand_id>/', views.edit_brand, name='edit_brand'),
    path('edit/color/<int:color_id>/', views.edit_color, name='edit_color'),
    path('edit/car/<int:car_id>/', views.edit_car, name='edit_car'),
    path('create_car/', views.create_car, name='create_car'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns 