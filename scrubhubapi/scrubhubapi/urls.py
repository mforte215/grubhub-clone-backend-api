from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import FoodItemViewSet, OrderItemViewSet, OrderViewSet, UserView, FullOrderItemDetailView
from django.contrib import admin
admin.autodiscover()

router = DefaultRouter()

router.register(r'meals', FoodItemViewSet)
router.register(r'orderitems', OrderItemViewSet)
router.register(r'orders', OrderViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('user/', UserView.as_view()),
    path('orderitemdetail/', FullOrderItemDetailView.as_view()),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]