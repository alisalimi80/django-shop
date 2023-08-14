from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/',views.ProductsDetailView.as_view(),name='product_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)