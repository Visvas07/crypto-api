from django.urls import path,include
from .views import Home,OrganizationViewSet,CryptoPriceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'organizations',OrganizationViewSet)
router.register(r'crypto-prices',CryptoPriceViewSet)

urlpatterns=[
    path('',Home.as_view()),
    path('api/',include(router.urls))

]