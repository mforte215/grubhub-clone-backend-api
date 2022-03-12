from tokenize import Token
from django.http import Http404, HttpRequest
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.views import APIView
from app.models import CustomUser, FoodItem, Order, OrderItem
from app.serializers import CustomUserSerializer, FoodItemSerializer, OrderItemSerializer, OrderSerializer, OrderDetailsSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = CustomUserSerializer

    def get(self, request, format=None):
        user = self.request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


class CustomUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        user = self.request.user
        return user

class FullOrderItemDetailView(APIView):
        permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
        serializer_class = OrderDetailsSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['orderid']

        def get(self, request, format=None):
            order_items = OrderItem.objects.all()
            serializer = OrderDetailsSerializer(order_items)
            return Response(serializer.data)

class FoodItemViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = Order.objects.all().order_by('-order_at')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order_by']
    ordering_fields = ['order_at']

class OrderItemViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['orderid']
    

