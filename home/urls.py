#home/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewset

# router = DefaultRouter()
# router.register('items', ItemViewset) #items là prefix của url, nếu dki là 'items' 
# thì url sẽ là http://localhost:8000/api/items/
# ItemViewset là viewsets mà tạo để xử lý yêu cầu đến Item

urlpatterns = [
    #path('', include(router.urls)),
]
