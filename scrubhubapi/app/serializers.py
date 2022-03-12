from rest_framework import serializers
from app.models import CustomUser, FoodItem, OrderItem, Order

class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')

class FoodItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'description', 'price', 'image_url']

class FoodItemIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodItem
        fields = ['id']


class OrderDetailsSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    fooditemid = FoodItemSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = '__all__'


    def create(self, validated_data):
        print('Printing Validated Data')
        print(validated_data)
        return super().create(validated_data)




class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    
    class Meta:
        model = Order
        fields = '__all__'