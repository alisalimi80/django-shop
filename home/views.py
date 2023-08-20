from django.shortcuts import render , get_object_or_404 , redirect
from django.views import View
from .models import Product
from bucket import bucket
from django.contrib import messages
from . import tasks

# Create your views here.
class HomeView(View):
	def get(self,request):
		products = Product.objects.filter(available=True)
		return render(request,'home/home.html',{'products':products})

class ProductsDetailView(View):
	def get(self,request,slug):
		product =  get_object_or_404(Product,slug=slug)
		return render(request,'home/product_detail.html',{'product':product})

class BucketView(View):
	template_name = 'home/bucket.html'

	def get(self,request):
		objects = bucket.get_objects()
		return render (request,self.template_name,{'objects':objects})
	
class DeleteObjBucket(View):
	def get(self,request,key):
		tasks.delete_object.delay(key)
		messages.success(request,'your object will be delete soon','info')
		return redirect('home:bucket')
		

class DownloadObjBucket(View):
	def get(self,request,key):
		tasks.download_object.delay(key)
		messages.success(request,'your object will be downlod soon.','info')
		return redirect('home:bucket')