from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('product_page/', views.product_page, name='product_page'),
    path('productdetails/<str:product_name>',
         views.product_details, name='product_details'),
    path('category/<str:category_name>',
         views.category_specific, name='category_specific'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
