from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

bucket_urls = [
    path('', views.BucketView.as_view(), name='bucket'),
    path('delete_obj/<str:key>',views.DeleteObjBucket.as_view(),name = 'delete_obj_bucket'),
    path('download_obj/<str:key>',views.DownloadObjBucket.as_view(),name = 'download_obj_bucket'),
]

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
    path('category/<slug:category_slug>/', views.HomeView.as_view(), name='category_slug'),
    path('bucket/', include(bucket_urls), name='bucket'),
    path('<slug:slug>/',views.ProductsDetailView.as_view(),name='product_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
