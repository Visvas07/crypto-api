from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOrganizationOwner
from .models import Organization,CryptoPrice
from .serializers import OrganizationSerializer,CryptoPriceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
def check(request):
    return HttpResponse("Test")

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        content = {'message':'Hello World!'}
        return Response(content)
    

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by('created_at')
    serializer_class = OrganizationSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['created_at']
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Organization.objects.filter(owner=self.request.user).order_by('created_at')
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def get_permissions(self):
        if self.action in ['update','partial_update','delete']:
            self.permission_classes = [IsAuthenticated,IsOrganizationOwner]
        return super().get_permissions()
    
    

class CryptoPriceViewSet(viewsets.ModelViewSet):
    queryset = CryptoPrice.objects.all().order_by('timestamp')
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['symbol']
    search_fields = ['symbol']
    ordering_fields = ['price','timestamp']
    permission_classes = [IsAuthenticated]
    serializer_class = CryptoPriceSerializer
    def get_queryset(self):
        return CryptoPrice.objects.all().order_by('timestamp')
