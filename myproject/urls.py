# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import create_record, RecordViewSet

router = DefaultRouter()
router.register(r'records', RecordViewSet)

urlpatterns = [
    path('create/', create_record, name='create_record'),
    path('', include(router.urls)),
]
